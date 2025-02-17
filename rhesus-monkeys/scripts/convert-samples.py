from pathlib import Path

import janitor.polars
import polars as pl
import polars.selectors as cs

# Set the folder path for raw-data
resource_dir = Path(__file__).resolve().parent.parent
folder_path = resource_dir / "data-raw"
unzip_path = folder_path / "unzipped"

# Create the metabolite data files


# Transpose a single file
def transpose_data(load_file_name: Path, save_file_name: Path, monkey_type: str):
    """Reads a CSV file, transposes it, and writes the result to another CSV."""
    pl.read_csv(unzip_path / load_file_name).transpose(
        include_header=True, header_name=monkey_type, column_names="Metabolite"
    ).write_csv(folder_path / save_file_name)


# Find files and generate corresponding output filenames
load_file_names = list(unzip_path.glob("concentration_*.csv"))
save_file_names = [folder_path / f"data_{file.name}" for file in load_file_names]

# Extract 'maternal' or 'infant' from the filenames
monkey_types = [file.stem.split("_")[1] + "_sample_id" for file in load_file_names]

list(map(transpose_data, load_file_names, save_file_names, monkey_types))

# Cortisol data
df_cortisol_infant_bl = pl.read_excel(unzip_path / "cortisol_infant_blood.xlsx")

df_cortisol = df_cortisol_infant_bl.unpivot(
    ["samp1", "samp2", "samp3", "samp4"], index=["Infant_ID", "PD"]
)

time_mapping = {"samp1": "02:00", "samp2": "07:00", "samp3": "11:30", "samp4": "23:30"}

df_cortisol = (
    df_cortisol.with_columns(
        pl.col("variable").replace_strict(time_mapping).alias("hours_into_sampling")
    )
    .select(["Infant_ID", "PD", "hours_into_sampling", "value"])
    .rename(
        {
            "value": "cortisol_level",
            "Infant_ID": "infant_id",
            "PD": "post_gestation_day",
        }
    )
    .clean_names()
    .write_csv(folder_path / "data_cortisol_infant_blood.csv")
)
# Cytokine data both sets
df_cytokine_infant_bl = pl.read_csv(unzip_path / "cytokine_infant_blood.csv")
df_cytokine_infant_bl = (
    df_cytokine_infant_bl.drop(
        [
            "Group",
            "PD",
            "Target_PD",
            "Mother_ID",
            "GD_Delivery",
            "Mode_birth",
            "Fostered",
            "Foster_ID",
        ]
    )
    .clean_names()
    .write_csv(folder_path / "data_cytokine_infant_bl.csv", separator=";")
)

df_cytokine_maternal_bl = pl.read_csv(unzip_path / "cytokine_maternal_blood.csv")

df_cytokine_maternal_bl = (
    df_cytokine_maternal_bl.drop(["Group", "GD", "Target_GD"])
    .clean_names()
    .write_csv(folder_path / "data_cytokine_maternal_blood.csv", separator=";")
)
# May want to have a closer look at 14 at some point

# Human intruder testing
df_infant_behavior = pl.read_excel(unzip_path / "hi_infant_behavior.xlsx")

profile_mapping = {
    "pfscratch": "Profile-Far",
    "pnscratch": "Profile-Near",
    "sfscratch": "Stare-Far",
    "snscratch": "Stare-Near",
}

df_behavior = df_infant_behavior.unpivot(
    ["pfscratch", "pnscratch", "sfscratch", "snscratch"], index=["Infant_ID", "PD"]
)

df_behavior = (
    df_behavior.with_columns(
        pl.col("variable")
        .replace_strict(profile_mapping)
        .alias("presentation_of_profile")
    )
    .select(["Infant_ID", "PD", "presentation_of_profile", "value"])
    .rename(
        {"value": "scratches", "Infant_ID": "infant_id", "PD": "post_gestation_day"}
    )
    .clean_names()
    .write_csv(folder_path / "data_hi_infant_behavior.csv")
)

# Cognition testing of infants
df_infant_cognitive = pl.read_excel(unzip_path / "vpc_infant_cognitive.xlsx")

df_cognitive = df_infant_cognitive.unpivot(
    [
        "P1T1 Total number Look RIGHT FAM",
        "P1T1 Total number Look LEFT NOVEL",
        "P1T1 Total number Look Away",
        "P1T2 Total number Look RIGHT NOVEL",
        "P1T2 Total number Look LEFT FAM",
        "P1T2 Total number Look Away",
        "P2T1 Total number Look RIGHT NOVEL",
        "P2T1 Total number Look LEFT FAM",
        "P2T1 Total number Look Away",
        "P2T2 Total number Look RIGHT FAM",
        "P2T2 Total number Look LEFT NOVEL",
        "P2T2 Total number Look Away",
        "P3T1 Total number Look RIGHT NOVEL",
        "P3T1 Total number Look LEFT FAM",
        "P3T1 Total number Look Away",
        "P3T2 Total number Look RIGHT FAM",
        "P3T2 Total number Look LEFT NOVEL",
        "P3T2 Total number Look Away",
        "P4T1 Total number Look RIGHT FAM",
        "P4T1 Total number Look LEFT NOVEL",
        "P4T1 Total number Look Away",
        "P4T2 Total number Look RIGHT NOVEL",
        "P4T2 Total number Look LEFT FAM",
        "P4T2 Total number Look Away",
        "no.look_N",
        "no.look_F",
        "no.look_N+F",
        "no.look_N/N+F",
    ],
    index=["Infant_ID", "GD_delivery", "Batch", "PCD"],
)

df_cognitive = (
    df_cognitive.with_columns(pl.col("variable"))
    .select(["Infant_ID", "GD_delivery", "Batch", "PCD", "variable", "value"])
    .rename(
        {
            "value": "Looks",
            "variable": "type_of_test",
            "Infant_ID": "infant_id",
            "GD_delivery": "gestation_day_at_delivery",
            "PCD": "post_conception_day",
        }
    )
    .clean_names()
    .write_csv(folder_path / "data_vpc_infant_cognitive.csv")
)

# TO DO
# 9 Meta maternal blood
# Batch,Dilution_factor
# 10 Meta maternal urine
# Batch,Dilution_factor
# Check if there are more weight measures to be found in 15
