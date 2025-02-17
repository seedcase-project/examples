import polars as pl
import re
from pathlib import Path

#Transform from tab sep to comma sep
with open('../data-raw/data.tsv', 'r') as tsv:

    with open('../data-raw/data-ready.csv', 'w') as csv:
        for line in tsv:
            content = re.sub("\t", ",", line) 
            csv.write(content)

df = pl.read_csv('../data-raw/data-ready.csv', infer_schema_length=100_000) 

block_mapping = {1:"Block 1", 2:"Block 2", 3:"Block 3"}

treatment_map = {"V":"Virgin", "M":"Mating"}

df = df.rename({col: col.lower() for col in df.columns}).with_columns(
    block=pl.col("block").replace_strict(block_mapping, return_dtype=pl.Utf8),
    treatment=pl.col("treatment").replace_strict(treatment_map),
    )  

df.write_csv('../data-raw/data-ready.csv')

df.glimpse()
