import polars as pl
import re
from pathlib import Path

# Convert files from xlsx to csv
df06 = pl.read_excel("../data-raw/data06.xlsx")
df06.write_csv('../data-raw/data06.csv')
df15 = pl.read_excel("../data-raw/data15.xlsx")
df15.write_csv('../data-raw/data15.csv')
df16 = pl.read_excel("../data-raw/data16.xlsx")
df16.write_csv('../data-raw/data16.csv')


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
        "infant_exp",
        "infant_exp",
        "adult_exp",
        "adult_exp",
        "adult_exp"
     ]
     for load_file_name, save_file_name, monkey_type in zip(load_file_names, save_file_names, monkey_types):
         transpose_data(load_file_name, save_file_name, monkey_type)

# Cortisol - infants in tidydata format

df06 = pl.read_csv('../data-raw/data06.csv') 

sample1 = '02:00'
sample2 = '07:00'
sample3 = '11:30'
sample4 = '23:30'

df1 = df06.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("samp1").alias("cortisol_level"),)
df2 = df06.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("samp2").alias("cortisol_level"),)
df3 = df06.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("samp3").alias("cortisol_level"),)
df4 = df06.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("samp4").alias("cortisol_level"),)

df_sample1 = df1.with_columns(pl.lit(sample1).alias("hours_into_sampling"))
df_sample2 = df2.with_columns(pl.lit(sample2).alias("hours_into_sampling"))
df_sample3 = df1.with_columns(pl.lit(sample3).alias("hours_into_sampling"))
df_sample4 = df2.with_columns(pl.lit(sample4).alias("hours_into_sampling"))

df_cortisol = pl.concat([df_sample1, df_sample2, df_sample3, df_sample4])

df_cortisol.write_csv('../data-raw/data6-ready.csv')

# Cytokine data both sets
df12 = pl.read_csv(folder_path / "data12.csv")
df12 = df12.drop(["Batch","Group","PD","Target_PD","Mother_ID","GD_Delivery","Mode_birth","Fostered","Foster_ID"])
df12.write_csv("../data-raw/data12-ready.csv", separator=";")

df13 = pl.read_csv(folder_path / "data13.csv")
df13 = df13.drop(["Batch","Group","GD","Target_GD"])
df13.write_csv("../data-raw/data13-ready.csv", separator=";")

# May want to have a closer look at 14 at some point

# Human intruder testing
df15 = pl.read_csv('../data-raw/data15.csv') 

sample1 = 'Profile-Far'
sample2 = 'Profile-Near'
sample3 = 'Stare-Far'
sample4 = 'Stare-Near'

df1 = df15.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("pfscratch").alias("scratch"),)
df2 = df15.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("pnscratch").alias("scratch"),)
df3 = df15.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("sfscratch").alias("scratch"),)
df4 = df15.select(pl.col("Infant_ID").alias("infant_exp"), pl.col("PD").alias("post_gestation_day"), pl.col("snscratch").alias("scratch"),)

df_sample1 = df1.with_columns(pl.lit(sample1).alias("presentation_of_profile"))
df_sample2 = df2.with_columns(pl.lit(sample2).alias("presentation_of_profile"))
df_sample3 = df1.with_columns(pl.lit(sample3).alias("presentation_of_profile"))
df_sample4 = df2.with_columns(pl.lit(sample4).alias("presentation_of_profile"))

df_hi = pl.concat([df_sample1, df_sample2, df_sample3, df_sample4])

df_hi.write_csv('../data-raw/data15-ready.csv')

# Cognition testing of infants
df16 = pl.read_csv('../data-raw/data16.csv')

sample01 = 'P1T1 Total number Look RIGHT FAM'
sample02 = 'P1T1 Total number Look LEFT NOVEL'
sample03 = 'P1T1 Total number Look Away'
sample04 = 'P1T2 Total number Look RIGHT NOVEL'
sample05 = 'P1T2 Total number Look LEFT FAM'
sample06 = 'P1T2 Total number Look Away'
sample07 = 'P2T1 Total number Look RIGHT NOVEL'
sample08 = 'P2T1 Total number Look LEFT FAM'
sample09 = 'P2T1 Total number Look Away'
sample10 = 'P2T2 Total number Look RIGHT FAM'
sample11 = 'P2T2 Total number Look LEFT NOVEL'
sample12 = 'P2T2 Total number Look Away'
sample13 = 'P3T1 Total number Look RIGHT NOVEL'
sample14 = 'P3T1 Total number Look LEFT FAM'
sample15 = 'P3T1 Total number Look Away'
sample16 = 'P3T2 Total number Look RIGHT FAM'
sample17 = 'P3T2 Total number Look LEFT NOVEL'
sample18 = 'P3T2 Total number Look Away'
sample19 = 'P4T1 Total number Look RIGHT FAM'
sample20 = 'P4T1 Total number Look LEFT NOVEL'
sample21 = 'P4T1 Total number Look Away'
sample22 = 'P4T2 Total number Look RIGHT NOVEL'
sample23 = 'P4T2 Total number Look LEFT FAM'
sample24 = 'P4T2 Total number Look Away'
sample25 = 'no.look_N'
sample26 = 'no.look_F'
sample27 = 'no.look_N+F'
sample28 = 'no.look_N/N+F'

df001 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P1T1 Total number Look RIGHT FAM").cast(pl.Float32).alias("looks"),)
df002 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P1T1 Total number Look LEFT NOVEL").cast(pl.Float32).alias("looks"),)
df003 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P1T1 Total number Look Away").cast(pl.Float32).alias("looks"),)
df004 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P1T2 Total number Look RIGHT NOVEL").cast(pl.Float32).alias("looks"),)
df005 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P1T2 Total number Look LEFT FAM").cast(pl.Float32).alias("looks"),)
df006 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P1T2 Total number Look Away").cast(pl.Float32).alias("looks"),)
df007 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P2T1 Total number Look RIGHT NOVEL").cast(pl.Float32).alias("looks"),)
df008 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P2T1 Total number Look LEFT FAM").cast(pl.Float32).alias("looks"),)
df009 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P2T1 Total number Look Away").cast(pl.Float32).alias("looks"),)
df010 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P2T2 Total number Look RIGHT FAM").cast(pl.Float32).alias("looks"),)
df011 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P2T2 Total number Look LEFT NOVEL").cast(pl.Float32).alias("looks"),)
df012 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P2T2 Total number Look Away").cast(pl.Float32).alias("looks"),)
df013 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P3T1 Total number Look RIGHT NOVEL").cast(pl.Float32).alias("looks"),)
df014 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P3T1 Total number Look LEFT FAM").cast(pl.Float32).alias("looks"),)
df015 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P3T1 Total number Look Away").cast(pl.Float32).alias("looks"),)
df016 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P3T2 Total number Look RIGHT FAM").cast(pl.Float32).alias("looks"),)
df017 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P3T2 Total number Look LEFT NOVEL").cast(pl.Float32).alias("looks"),)
df018 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P3T2 Total number Look Away").cast(pl.Float32).alias("looks"),)
df019 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P4T1 Total number Look RIGHT FAM").cast(pl.Float32).alias("looks"),)
df020 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P4T1 Total number Look LEFT NOVEL").cast(pl.Float32).alias("looks"),)
df021 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P4T1 Total number Look Away").cast(pl.Float32).alias("looks"),)
df022 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P4T2 Total number Look RIGHT NOVEL").cast(pl.Float32).alias("looks"),)
df023 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P4T2 Total number Look LEFT FAM").cast(pl.Float32).alias("looks"),)
df024 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("P4T2 Total number Look Away").cast(pl.Float32).alias("looks"),)
df025 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("no.look_N").cast(pl.Float32).alias("looks"),)
df026 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("no.look_F").cast(pl.Float32).alias("looks"),)
df027 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("no.look_N+F").cast(pl.Float32).alias("looks"),)
df028 = df16.select(pl.col("Infant_ID").alias("infant_id"), pl.col("GD_delivery").alias("gestation_day_at_delivery"), pl.col("PCD").alias("post_conception_day")
, pl.col("no.look_N/N+F").cast(pl.Float32).alias("looks"),)

df_sample1 = df001.with_columns(pl.lit(sample01).alias("number_of_recognition"))
df_sample2 = df002.with_columns(pl.lit(sample02).alias("number_of_recognition"))
df_sample3 = df003.with_columns(pl.lit(sample03).alias("number_of_recognition"))
df_sample4 = df004.with_columns(pl.lit(sample04).alias("number_of_recognition"))
df_sample5 = df005.with_columns(pl.lit(sample05).alias("number_of_recognition"))
df_sample6 = df006.with_columns(pl.lit(sample06).alias("number_of_recognition"))
df_sample7 = df007.with_columns(pl.lit(sample07).alias("number_of_recognition"))
df_sample8 = df008.with_columns(pl.lit(sample08).alias("number_of_recognition"))
df_sample9 = df009.with_columns(pl.lit(sample09).alias("number_of_recognition"))
df_sample10 = df010.with_columns(pl.lit(sample10).alias("number_of_recognition"))
df_sample11 = df011.with_columns(pl.lit(sample11).alias("number_of_recognition"))
df_sample12 = df012.with_columns(pl.lit(sample12).alias("number_of_recognition"))
df_sample13 = df013.with_columns(pl.lit(sample13).alias("number_of_recognition"))
df_sample14 = df014.with_columns(pl.lit(sample14).alias("number_of_recognition"))
df_sample15 = df015.with_columns(pl.lit(sample15).alias("number_of_recognition"))
df_sample16 = df016.with_columns(pl.lit(sample16).alias("number_of_recognition"))
df_sample17 = df017.with_columns(pl.lit(sample17).alias("number_of_recognition"))
df_sample18 = df018.with_columns(pl.lit(sample18).alias("number_of_recognition"))
df_sample19 = df019.with_columns(pl.lit(sample19).alias("number_of_recognition"))
df_sample20 = df020.with_columns(pl.lit(sample20).alias("number_of_recognition"))
df_sample21 = df021.with_columns(pl.lit(sample21).alias("number_of_recognition"))
df_sample22 = df022.with_columns(pl.lit(sample22).alias("number_of_recognition"))
df_sample23 = df023.with_columns(pl.lit(sample23).alias("number_of_recognition"))
df_sample24 = df024.with_columns(pl.lit(sample24).alias("number_of_recognition"))
df_sample25 = df025.with_columns(pl.lit(sample25).alias("number_of_recognition"))
df_sample26 = df026.with_columns(pl.lit(sample26).alias("number_of_recognition"))
df_sample27 = df027.with_columns(pl.lit(sample27).alias("number_of_recognition"))
df_sample28 = df028.with_columns(pl.lit(sample28).alias("number_of_recognition"))

df_cognitive = pl.concat([df_sample1, df_sample2, df_sample3, df_sample4, df_sample5, df_sample6, df_sample7, df_sample8
, df_sample9, df_sample10, df_sample11, df_sample12, df_sample13, df_sample14, df_sample15, df_sample16, df_sample17
, df_sample18, df_sample19, df_sample20, df_sample21, df_sample22, df_sample23, df_sample24, df_sample25, df_sample26
, df_sample27, df_sample28])

df_cognitive.write_csv('../data-raw/data16-ready.csv')

#TO DO
# 9 Meta maternal blood
  # Batch,Dilution_factor
# 10 Meta maternal urine
  # Batch,Dilution_factor
# Check if there are more weight measures to be found in 15
