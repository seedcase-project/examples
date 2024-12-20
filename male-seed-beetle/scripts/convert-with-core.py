import polars as pl
import re
from pathlib import Path

#Transform from tab sep to comma sep
with open('../data-raw/data.csv', 'r') as tsv:

    with open('../data-raw/data1.csv', 'w') as csv:

        for line in tsv:

            content = re.sub("\t", ",", line) 

            csv.write(content)

Path('../data-raw/data.csv').unlink()

Path('../data-raw/data1.csv').rename('../data-raw/data.csv')

df = pl.read_csv('../data-raw/data.csv')

#Convert categorical values to characters

block_mapping = {1:"Block 1", 2:"Block 2", 3:"Block 3"}

df = df.with_columns(
    BLOCK = pl.col("BLOCK").replace_strict(block_mapping, return_dtype=pl.Utf8)
)
df.write_csv('../data-raw/data.csv')

#Update from scream to lowercase, as that will create snake_case in this file
#df = pl.read_csv('../data-raw/data.csv')

column_names = {col: col.lower() for col in df.columns}

df = df.rename(column_names)

df.write_csv('../data-raw/data.csv')

#Find the columns with type string, then check for pure numerical 
# values as that may indicate that there is a conversion error
for col, dtype in zip(df.columns, df.dtypes):
    if dtype == pl.Utf8:
        print(f"{col}: {dtype}")

        for value in df[col]:
            if value.isdigit():
                print(f"Numerical value found in column {col}: {value}")
                #TODO Need to rework this bit

# Update abbreviated values to full text
treatment_map = {"V":"Virgin", "M":"Mating"}

df = df.with_columns(
    treatment=pl.col("treatment").replace_strict(treatment_map)
)
df.write_csv('../data-raw/data.csv')
