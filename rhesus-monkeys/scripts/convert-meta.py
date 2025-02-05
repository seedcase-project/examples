import polars as pl
import re
from pathlib import Path

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

# Create the infant metadata files
    # FIO There is one extra infant in 07, all infants in 08 are included in 07
df07 = pl.read_csv(folder_path / "data07.csv")
df08 = pl.read_csv(folder_path / "data08.csv")

df_infant = df07.select(pl.col("Infant_ID"), pl.col("Mother_ID"), pl.col("GD_Delivery").alias("gestation_day_delivery")
, pl.col("Fostered"), pl.col("Foster_ID"))
# infant gender is in data_adult at present
df_infant1 = df_infant.unique()
df_infant1.write_csv("../data-raw/data_infant.csv", separator=";")

df_infant_w1 = df07.select(pl.col("Infant_ID"), pl.col("Weight_PD7").alias("weight_at_x_days_old"), pl.col("ActualDay_PD7").alias("x_days_old"))
df_infant_w2 = df08.select(pl.col("Infant_ID"), pl.col("Infant_weight").alias("weight_at_x_days_old"), pl.col("PD").alias("x_days_old"))
df_infant_weight = pl.concat([df_infant_w1, df_infant_w2])
df_infant_weight1 = df_infant_weight.unique()
df_infant_weight1.write_csv("../data-raw/data_infant_weight.csv", separator=";")

# Create the adult metadata files
    # FIO There are no additional Mother_ID in file 11
df09 = pl.read_csv(folder_path / "data09.csv")
df10 = pl.read_csv(folder_path / "data10.csv")
df11 = pl.read_csv(folder_path / "data11.csv")

df_adult09 = df09.select(pl.col("Mother_ID"), pl.col("Mother_age").alias("Age_at_conception"), pl.col("GD_Delivery").alias("gestation_day_at_delivery")
, pl.col("Group").alias("obesity_classification"), pl.col("Mode_birth"), pl.col("Reject"), pl.col("Infant_sex"))
df_adult10 = df10.select(pl.col("Mother_ID"), pl.col("Mother_age").alias("Age_at_conception"), pl.col("GD_Delivery").alias("gestation_day_at_delivery")
, pl.col("Group").alias("obesity_classification"), pl.col("Mode_birth"), pl.col("Reject"), pl.col("Infant_sex"))

df_adult_w1 = df09.select(pl.col("Mother_ID"), pl.col("GD_day").alias("sample_gestation_day"), pl.col("GD_targeted").alias("target_gestation_day")
, pl.col("Mother_Weight").alias("weight_at_gestation_day"), pl.col("BCS").alias("body_condition_score")) 
df_adult_w2 = df10.select(pl.col("Mother_ID"), pl.col("GD").alias("sample_gestation_day"), pl.col("Target_GD").alias("target_gestation_day")
, pl.col("Mother_Weight").alias("weight_at_gestation_day"), pl.col("BCS").alias("body_condition_score")) 

# Concatenate and de-dup adult files
df_adult1 = pl.concat([df_adult09, df_adult10])
df_adult2 = df_adult1.unique()
df_adult2.write_csv("../data-raw/data_adult.csv", separator=";")

df_adultw1 = pl.concat([df_adult_w1, df_adult_w2])
df_adultw2 = df_adultw1.unique()
df_adultw2.write_csv("../data-raw/data_adult_weight.csv", separator=";")

# Create the linking table

df_link07 = df07.select(pl.col("Infant_ID"), pl.col("Exp"), pl.col("PD").alias("day_sample_taken"), pl.col("Batch"))
df_link08 = df08.select(pl.col("Infant_ID"), pl.col("Exp"), pl.col("PD").alias("day_sample_taken"), pl.col("Batch"))

df_link09 = df09.select(pl.col("Mother_ID"), pl.col("Exp"), pl.col("GD_day").alias("day_sample_taken"), pl.col("Batch"))
df_link10 = df10.select(pl.col("Mother_ID"), pl.col("Exp"), pl.col("GD").alias("day_sample_taken"), pl.col("Batch"))
df_link11 = df11.select(pl.col("Mother_ID"), pl.col("Exp"), pl.col("GD").alias("day_sample_taken"), pl.col("Batch"))

matter1 = "Blood"
matter2 = "Urine"
matter3 = "Placenta"

df_lnk1 = df_link07.with_columns(pl.lit(matter1).alias("type_of_matter"))
df_lnk2 = df_link08.with_columns(pl.lit(matter2).alias("type_of_matter"))
df_lnk3 = df_link09.with_columns(pl.lit(matter1).alias("type_of_matter"))
df_lnk4 = df_link10.with_columns(pl.lit(matter2).alias("type_of_matter"))
df_lnk5 = df_link11.with_columns(pl.lit(matter3).alias("type_of_matter"))

df_infant_link = pl.concat([df_lnk1, df_lnk2])
df_infant_link.write_csv('../data-raw/data_infant_link.csv')
df_adult_link = pl.concat([df_lnk3, df_lnk4, df_lnk5])
df_adult_link.write_csv('../data-raw/data_adult_link.csv')

# Create the placenta file



'''
11 - Metadata_Maternal.placenta.csv
* Variables 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Maternal.placenta.csv file.
o Mother_ID: IDs of mothers. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o GD: Exact gestational day (GD) when samples were collected.
o Target_GD: Target GD for sample collection. 
o Dilution_factor: Dilution factor used to prepare NMR samples. 
o BCS: Body Condition Score (BCS) 
o Tissue_weight: Weight of placental tissue sample. 
o V1: Volume of solvent used to extract (uL). Used to correct the metabolite concentration.
o V2: Volume of polar layer (methanol + water) collected (uL). Used to correct the metabolite concentration.
o V3: Buffer added to reconstitute the sample after freeze drying (uL). Used to correct the metabolite concentration. 
* Missing data codes: Indicated by NAs.
'''
