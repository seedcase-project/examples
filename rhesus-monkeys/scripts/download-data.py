"""Downloads a data file from a given URL.

This is the most basic of the download data scripts. It requires that the url for
the data is provided as an argument, and it assumes that a data-raw folder
has been created containing a .gitignore file.
"""

from pathlib import Path
from zipfile import ZipFile
import os
import requests

resource_dir = Path(__file__).resolve().parent.parent

folder_path = resource_dir / "data-raw"

# Download and save the zip file
all_files = requests.get("https://zenodo.org/api/records/7055715/files-archive")

all_files_path = folder_path / "all_files.zip"
with open(all_files_path, "wb") as file:
    file.write(all_files.content)

# Extract the zip file
with ZipFile(all_files_path, 'r') as zip_ref:
    zip_ref.extractall(folder_path)

# Rename the files to snake_case
for file in folder_path.iterdir():
    if file.name.endswith((".csv", ".xlsx")):
        new_name = file.name.lower().replace(".", "_", 1)
        file.rename(folder_path / new_name)
