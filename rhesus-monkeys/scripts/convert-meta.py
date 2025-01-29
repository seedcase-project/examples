import polars as pl
import re
from pathlib import Path

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

# Create the infant metadata files
df07 = pl.read_csv(folder_path / "data07.csv")
df08 = pl.read_csv(folder_path / "data08.csv")

df_infant1 = df07.select(pl.col("Infant_ID"),  
pl.col("Mother_ID"), pl.col("GD_Delivery").alias("gestation_day_delivery"), pl.col("Fostered"), pl.col("Foster_ID"))
# infant gender is in 09 Maternal Blood

df_infant1.write_csv("../data-raw/data_infant.csv", separator=";")

df_infant_w1 = df07.select(pl.col("Infant_ID"), pl.col("Weight_PD7").alias("weight_at_x_days_old"), pl.col("ActualDay_PD7").alias("x_days_old"))
df_infant_w2 = df08.select(pl.col("Infant_ID"), pl.col("Infant_weight").alias("weight_at_x_days_old"), pl.col("PD").alias("x_days_old"))
df_infant_weight = pl.concat([df_infant_w1, df_infant_w2])

df_infant_weight.write_csv("../data-raw/data_infant_weight.csv", separator=";")

# Create the adult metadata file
df09 = pl.read_csv(folder_path / "data09.csv")
df10 = pl.read_csv(folder_path / "data10.csv")

df_adult09 = df09.select(pl.col("Mother_ID"), pl.col("Mother_age").alias("Age_at_conception"), pl.col("GD_Delivery").alias("gestation_day_at_delivery")
, pl.col("Group").alias("obesity_classification"), pl.col("Mode_birth"), pl.col("Reject"), pl.col("BCS").alias("body_condition_score"))
#, pl.col("Placenta_Width"), pl.col("Placenta_Height"), pl.col("Placenta_Thickness"), pl.col("EPV").alias("estimated_placenta_volume"))
df_adult10 = df10.select(pl.col("Mother_ID"), pl.col("Mother_age").alias("Age_at_conception"), pl.col("GD_Delivery").alias("gestation_day_at_delivery")
, pl.col("Group").alias("obesity_classification"), pl.col("Mode_birth"), pl.col("Reject"), pl.col("BCS").alias("body_condition_score"))
# No placenta information in file 10, a couple of mothers not registered in file 9
# No additional Mother_ID in file 11

df_adult1 = pl.concat([df_adult09, df_adult10])

df_adult1.unique() # doesn't do anything at present

df_adult1.write_csv("../data-raw/data_adult.csv", separator=";")

# 9 Meta maternal blood
# Batch,GD_day,GD_targeted,Dilution_factor,Mother_Weight,Infant_sex
# 10 Meta maternal urine
# Batch,GD,Target_GD,Dilution_factor,Mother_Weight,Infant_sex
