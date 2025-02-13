import polars as pl
import re
from pathlib import Path
import janitor.polars

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

# Create the infant metadata files
    # FIO All infants in meta_infant_ur are included in meta_infant_bl. There is one extra infant in meta_infant_bl.
df_meta_infant_bl = pl.read_csv(folder_path / "metadata_infant_blood.csv") 
df_meta_infant_ur = pl.read_csv(folder_path / "metadata_infant_urine.csv") 

df_infant = df_meta_infant_bl.select(["Infant_ID", "Mother_ID", "GD_Delivery", "Fostered"
, "Foster_ID"]).rename({"GD_Delivery": "gestation_day_delivery"}).unique().clean_names().write_csv(folder_path / "data_infant_meta.csv", separator=";")
    # infant gender is in data_adult at present, all subjects are male, females are not included in the study

df_infant_w1 = df_meta_infant_bl.select(["Infant_ID", "Weight_PD7", "ActualDay_PD7"]).rename({"Weight_PD7": "weight_at_x_days_old", "ActualDay_PD7": "x_days_old"}).clean_names()
df_infant_w2 = df_meta_infant_ur.select(["Infant_ID","Infant_weight","PD"]).rename({"Infant_weight": "weight_at_x_days_old", "PD": "x_days_old"}).clean_names()
df_infant_weight = pl.concat([df_infant_w1, df_infant_w2]).unique().write_csv(folder_path / "data_infant_weight.csv", separator=";") # Concatenate (long)

# Create the infant linking tables

matter1 = "Blood"
matter2 = "Urine"

df_link_infant1 = df_meta_infant_bl.select(["Infant_ID", "Exp", "PD", "Batch"]).rename({"PD": "day_sample_taken"}).clean_names().with_columns(pl.lit(matter1).alias("type_of_matter"))
df_link_infant2 = df_meta_infant_ur.select(["Infant_ID", "Exp", "PD", "Batch"]).rename({"PD": "day_sample_taken"}).clean_names().with_columns(pl.lit(matter2).alias("type_of_matter"))

df_infant_link = pl.concat([df_link_infant1, df_link_infant2]).write_csv(folder_path / "data_infant_sample_meta.csv", separator=";") # Concatenate long

# Create the adult metadata files
    # FIO There are no additional Mother_ID in file 11
df_metadata_maternal_bl = pl.read_csv(folder_path / "metadata_maternal_blood.csv")
df_metadata_maternal_ur = pl.read_csv(folder_path / "metadata_maternal_urine.csv")
df_metadata_maternal_pl = pl.read_csv(folder_path / "metadata_maternal_placenta.csv")

df_adult_meta1 = df_metadata_maternal_bl.select(["Mother_ID", "Mother_age", "GD_Delivery", "Group", "Mode_birth", "Reject", "Infant_sex"]).rename({"Mother_age": "Age_at_conception"
, "GD_Delivery": "gestation_day_at_delivery", "Group": "obesity_classification", "Mode_birth": "mode_of_birth"}).clean_names()
df_adult_meta2 = df_metadata_maternal_ur.select(["Mother_ID", "Mother_age", "GD_Delivery", "Group", "Mode_birth", "Reject", "Infant_sex"]).rename({"Mother_age": "Age_at_conception"
, "GD_Delivery": "gestation_day_at_delivery", "Group": "obesity_classification", "Mode_birth": "mode_of_birth"}).clean_names()
df_adult = pl.concat([df_adult_meta1, df_adult_meta2]).unique().write_csv(folder_path / "data_adult_meta.csv", separator=";") # Concatenate long

df_adult_weight1 = df_metadata_maternal_bl.select(["Mother_ID", "GD_day", "GD_targeted", "Mother_Weight", "BCS"]).rename({"GD_day": "sample_gestation_day"
, "GD_targeted": "target_gestation_day", "Mother_Weight": "weight_at_gestation_day", "BCS": "body_condition_score"})
df_adult_weight2 = df_metadata_maternal_ur.select(["Mother_ID", "GD", "Target_GD", "Mother_Weight", "BCS"]).rename({"GD": "sample_gestation_day"
, "Target_GD": "target_gestation_day", "Mother_Weight": "weight_at_gestation_day", "BCS": "body_condition_score"})
df_adult_weight = pl.concat([df_adult_weight1, df_adult_weight2]).unique().write_csv(folder_path / "data_adult_weight.csv", separator=";") # Concatenate long

# Create the adult linking tables

# matter1 = "Blood" define above in infant linking tables
# matter2 = "Urine" define above in infant linking tables
matter3 = "Placenta"

df_link_adult1 = df_metadata_maternal_bl.select(["Mother_ID", "Exp", "GD_day", "GD_targeted", "Batch", "Dilution_factor"]).rename({"GD_day": "day_sample_taken"
, "GD_targeted": "target_sampling_day"}).with_columns(pl.lit(matter1).alias("type_of_matter"))
df_link_adult2 = df_metadata_maternal_ur.select(["Mother_ID", "Exp", "GD", "Target_GD", "Batch", "Dilution_factor"]).rename({"GD": "day_sample_taken"
, "Target_GD": "target_sampling_day"}).with_columns(pl.lit(matter2).alias("type_of_matter"))
df_link_adult3 = df_metadata_maternal_pl.select(["Mother_ID", "Exp", "GD", "Target_GD", "Batch", "Dilution_factor"]).rename({"GD": "day_sample_taken"
, "Target_GD": "target_sampling_day"}).with_columns(pl.lit(matter3).alias("type_of_matter"))

df_adult_link = pl.concat([df_link_adult1, df_link_adult2, df_link_adult3]).write_csv(folder_path / "data_adult_sample_meta.csv", separator=";") # Concatenate long


# Create the placenta file
# Both from metadata_maternal_bl (Placenta_Width,Placenta_Height,Placenta_Thickness,EPV) and from 11 (see below)
# More than one measure in metadata_maternal_bl?
'''
11 - Metadata_Maternal_placenta.csv
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
