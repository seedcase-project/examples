"""Downloads a data file from a given URL.

This is the most basic of the download data scripts. It requires that the url for
the data is provided as an argument, and it assumes that a data-raw folder
has been created containing a .gitignore file.
"""

from pathlib import Path

import requests

resource_dir = Path(__file__).resolve().parent.parent

folder_path = resource_dir / "data-raw"

url = "https://zenodo.org/records/4965431/files/Expe3Abundance.csv?download=1"

raw_data = requests.get(url, allow_redirects=True)

file_path = folder_path / "data.csv"

with open(file_path, "wb") as file:
    file.write(raw_data.content)
