"""Downloads a data file from a given URL.

This is the most basic of the download data scripts. It requires that the url for
the data is provided as an argument, and it assumes that a data-raw folder
has been created containing a .gitignore file.
"""

from pathlib import Path

import requests

resource_dir = Path(__file__).resolve().parent.parent

folder_path = resource_dir / "data-raw"

def download_data(url, name):
     try:      
         # Get the data from the URL
         raw_data = requests.get(url, allow_redirects=True)
         raw_data.raise_for_status()  # Raise an exception for HTTP errors

         file_path = folder_path / name
         with open(file_path, "wb") as file:
             file.write(raw_data.content)

     except requests.exceptions.RequestException as e:
         print(f"Error downloading the data: {e}")
     except Exception as e:
         print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define lists of URLs and corresponding filenames
    urls = [
        "https://zenodo.org/records/7055715/files/Concentration_Infant.blood.csv?download=1", #1
        "https://zenodo.org/records/7055715/files/Concentration_Infant.urine.csv?download=1",
        "https://zenodo.org/records/7055715/files/Concentration_Maternal.blood.csv?download=1",
        "https://zenodo.org/records/7055715/files/Concentration_Maternal.placenta.csv?download=1",
        "https://zenodo.org/records/7055715/files/Concentration_Maternal.urine.csv?download=1", #5
        "https://zenodo.org/records/7055715/files/Cortisol_infant.blood.xlsx?download=1"
    ]
    names = [
        "data1.csv",
        "data2.csv",
        "data3.csv",
        "data4.csv",
        "data5.csv",
        "data6.xlsx"
    ]

    # Loop through the URLs and names and call the function for each pair
    for url, name in zip(urls, names):
        download_data(url, name)
