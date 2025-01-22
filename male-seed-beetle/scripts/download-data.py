from core.download import download_data
#from core import download_data
#from examples.functions.download import download_data
#from functions.download import download_data
if __name__ == "__main__":
   # Provide the two arguments needed for download_data
    arg1 = "https://zenodo.org/records/4932381/files/BeetleMetabolicRate_Dryad.txt?download=1"  # Replace with your actual argument
    arg2 = "data.csv"  # Replace with your actual argument

    # Call the download_data function
    download_data(arg1, arg2)
