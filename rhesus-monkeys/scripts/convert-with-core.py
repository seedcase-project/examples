import polars as pl
import re
from pathlib import Path

# Convert files from xlsx to csv
df = pl.read_excel("../data-raw/data06.xlsx")
df.write_csv('../data-raw/data06.csv')

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

# Transpose all files with metabolite data
def transpose_data(load_file_name, save_file_name, monkey_type):
    df_1 = pl.read_csv(folder_path / load_file_name)
    df_1a = df_1.transpose(include_header=True, header_name=monkey_type, column_names="Metabolite")
    df_1a.write_csv(folder_path / save_file_name)

if __name__ == "__main__":
     load_file_names = [
         "data01.csv",
         "data02.csv",
         "data03.csv",
         "data04.csv",
         "data05.csv"
     ]
     save_file_names = [
         "data01-ready.csv",
         "data02-ready.csv",
         "data03-ready.csv",
         "data04-ready.csv",
         "data05-ready.csv"
     ]
     monkey_types = [
        "infant_id",
        "infant_id",
        "adult_id",
        "adult_id",
        "adult_id"
     ]
     for load_file_name, save_file_name, monkey_type in zip(load_file_names, save_file_names, monkey_types):
         transpose_data(load_file_name, save_file_name, monkey_type)

# Cortisol - infants in tidydata format

df = pl.read_csv('../data-raw/data06.csv') 

sample1 = '02:00'
sample2 = '07:00'
sample3 = '11:30'
sample4 = '23:30'

df1 = df.select(pl.col("Infant_ID").alias("infant_id"), pl.col("PD").alias("post_gestation_day"), pl.col("samp1").alias("cortisol_level"),)
df2 = df.select(pl.col("Infant_ID").alias("infant_id"), pl.col("PD").alias("post_gestation_day"), pl.col("samp2").alias("cortisol_level"),)
df3 = df.select(pl.col("Infant_ID").alias("infant_id"), pl.col("PD").alias("post_gestation_day"), pl.col("samp3").alias("cortisol_level"),)
df4 = df.select(pl.col("Infant_ID").alias("infant_id"), pl.col("PD").alias("post_gestation_day"), pl.col("samp4").alias("cortisol_level"),)

df_sample1 = df1.with_columns(pl.lit(sample1).alias("hours_into_sampling"))
df_sample2 = df2.with_columns(pl.lit(sample2).alias("hours_into_sampling"))
df_sample3 = df1.with_columns(pl.lit(sample3).alias("hours_into_sampling"))
df_sample4 = df2.with_columns(pl.lit(sample4).alias("hours_into_sampling"))

df_cortisol = pl.concat([df_sample1, df_sample2, df_sample3, df_sample4])

df_cortisol.write_csv('../data-raw/data6-ready.csv')

# Main infant table
df5 = df.select(pl.col("Infant_ID").alias("infant_id"), pl.col("PD").alias("post_gestation_day"), pl.col("Infant_weight").alias("infant_weight"),)

df5.write_csv('../data-raw/data-infant-ready.csv')


# 02 - Concentration_Infant.urine.csv
    # Transpose data
    # Check for snake-case
    # Rename Metabolite to subject_ID
# 03 - Concentration_Maternal.blood.csv
    # Transpose data
    # Check for snake-case
    # Remove full stop in heading
    # Rename Metabolite to subject_ID
# 04 - Concentration_Maternal.placenta.csv
    # Transpose data
    # Check for snake-case
    # Rename Metabolite to subject_ID
# 05 - Concentration_Maternal.urine.csv
    # Transpose data
    # Check for snake-case
    # Remove "" and , and - from headings
    # Rename Metabolite to subject_ID

# 06 - Cortisol_infant.blood.xlsx
    # Convert into csv
    # Clarify headings
    # Check for snake-case

