"""Downloads a data file from a given URL.

This is the most basic of the download data scripts. It requires that the url for
the data is provided as an argument, and it assumes that a data-raw folder
has been created containing a .gitignore file.
"""

from pathlib import Path

import requests

# testing male-seed-beetle returned with print(f'{script_dir}')
resource_dir = Path(__file__).resolve().parent.parent

# testing male-seed-beetle/data-raw returned with print(f'{folder_path}')
folder_path = resource_dir / "data-raw"

url = "https://"

raw_data = requests.get(url, allow_redirects=True)

file_path = folder_path / "data.csv"

with open(file_path, "wb") as file:
    file.write(raw_data.content)
