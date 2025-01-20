# How to use the template-folder

This folder is a template for creating new folders. It contains all the necessary files and folders to get started with a new example data source. 

## Create the new folder

Open the `make-copy.py` script and update the folder-name variable, be sure to use camel-case and save the changes. Check that you are in the `_template-folder` directory and run the `make-copy.py` script. This will create the folders and files described below, as well as removing the make-copy.py script and delete this README file.

## Folder and file structure

The folder and file structure is as follows:

```
_template-folder
├── README.md
├── make-copy.py
├── data-raw
│   └── .gitignore
├── scripts
    ├── convert-with-core.py
    ├── download-data.py
    └── README.md
```

### Script files that will need to be modified after copying

`README.md` - This file should be updated with a description of the data source and any other relevant information.

`download-data.py` - This script should be updated to download the data from the source url and save it to the data-raw folder.

`convert-with-core.py` - This script is left blank and should be used to do any processing of the data in preparation for creating a data package.
