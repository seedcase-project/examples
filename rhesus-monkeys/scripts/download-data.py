"""Downloads a data file from a given URL.

This is the most basic of the download data scripts. It requires that the url for
the data is provided as an argument, and it assumes that a data-raw folder
has been created containing a .gitignore file.
"""

from pathlib import Path

import requests

resource_dir = Path(__file__).resolve().parent.parent

folder_path = resource_dir / "data-raw"

url_1 = "https://zenodo.org/records/7055715/files/Concentration_Infant.blood.csv?download=1"

raw_data_1 = requests.get(url_1, allow_redirects=True)

file_path_1 = folder_path / "data_1.csv"

with open(file_path_1, "wb") as file_1:
    file_1.write(raw_data_1.content)

url_2 = "https://zenodo.org/records/7055715/files/Concentration_Infant.urine.csv?download=1"

raw_data_2 = requests.get(url_2, allow_redirects=True)

file_path_2 = folder_path / "data_2.csv"

with open(file_path_2, "wb") as file_2:
    file_2.write(raw_data_2.content)
