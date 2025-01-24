import polars as pl
import re
from pathlib import Path

# 01 - Concentration_Infant.blood.csv
    # Transpose data
    # Check for snake-case
    # Rename Metabolite to subject_ID
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
df = pl.read_excel("../data-raw/data6.xlsx")
df.write_csv('../data-raw/data6.csv') # just for now so that I have a reference

sample1 = '02:00'
sample2 = '07:00'
sample3 = '11:30'
sample4 = '23:30'

df1 = df.select(pl.col("Infant_ID"), pl.col("PD").alias("post_gestation_day"), pl.col("samp1").alias("cortisol_level"),)
df2 = df.select(pl.col("Infant_ID"), pl.col("PD").alias("post_gestation_day"), pl.col("samp2").alias("cortisol_level"),)
df3 = df.select(pl.col("Infant_ID"), pl.col("PD").alias("post_gestation_day"), pl.col("samp3").alias("cortisol_level"),)
df4 = df.select(pl.col("Infant_ID"), pl.col("PD").alias("post_gestation_day"), pl.col("samp4").alias("cortisol_level"),)

df_sample1 = df1.with_columns(pl.lit(sample1).alias("hours_into_sampling"))
df_sample2 = df2.with_columns(pl.lit(sample2).alias("hours_into_sampling"))
df_sample3 = df1.with_columns(pl.lit(sample3).alias("hours_into_sampling"))
df_sample4 = df2.with_columns(pl.lit(sample4).alias("hours_into_sampling"))

df_cortisol = pl.concat([df_sample1, df_sample2, df_sample3, df_sample4])

#df_cortisol.glimpse()
df_cortisol.write_csv('../data-raw/data6-ready.csv')
