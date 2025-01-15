from pathlib import Path
from shutil import copytree

folder_name = 'seed-bank-dynamics'

source = Path.cwd()
destination = source.parent / folder_name

copytree(source, destination)

(destination / 'make-copy.py').unlink()
(destination / 'README.md').unlink()
