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
        "https://zenodo.org/records/4965431/files/Expe3Abundance.csv?download=1",
        "https://zenodo.org/records/4965431/files/Expe3Richness.csv?download=1"
    ]
    names = [
        "data3a.csv",
        "data3b.csv"
    ]

    # Loop through the URLs and names and call the function for each pair
    for url, name in zip(urls, names):
        download_data(url, name)
