from pathlib import Path
import requests
import argparse

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
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Download data from a URL and save it to a file.")
    parser.add_argument("url", type=str, help="The URL of the data to download.")
    parser.add_argument("name", type=str, help="The name of the file to save the data as.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the download function
    download_data(args.url, args.name)
