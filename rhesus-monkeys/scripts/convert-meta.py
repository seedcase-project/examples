import polars as pl
import re
from pathlib import Path

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"

df07 = pl.read_csv(folder_path / "data07.csv")

df_infant1 = df07.select(pl.col("Infant_ID"), pl.col("Group").alias("obesity_classification_mother"), 
pl.col("Mother_ID"), pl.col("GD_Delivery").alias("gestation_day_delivery"), pl.col("Mode_birth"), pl.col("Fostered"),
pl.col("Foster_ID"), pl.col("Weight_PD7").alias("weight_at_x_days_old"), pl.col("ActualDay_PD7").alias("x_days_old"))

df_infant1.glimpse()

df08 = pl.read_csv(folder_path / "data08.csv")

df_infant2 = df08.select(pl.col("Infant_ID"), pl.col("Group").alias("obesity_classification_mother"), 
pl.col("Mother_ID"), pl.col("GD_Delivery").alias("gestation_day_delivery"), pl.col("Mode_birth"), pl.col("Fostered"),
pl.col("Foster_ID"), pl.col("Infant_weight").alias("weight_at_x_days_old"), pl.col("PD").alias("x_days_old"))

df_infant2.glimpse()
