import polars as pl
import re
from pathlib import Path

# 01 - Concentration_Infant.blood.csv
    # Transpose data
    # Check for snake-case
    # Rename Metabolite to subject_ID
# 02 - Concentration_Infant.urine.csv
    # Transpose data
    # Check for snake-case
    # Rename Metabolite to subject_ID
# 03 - Concentration_Maternal.blood.csv
    # Transpose data
    # Check for snake-case
    # Remove full stop in heading
    # Rename Metabolite to subject_ID
# 04 - Concentration_Maternal.placenta.csv
    # Transpose data
    # Check for snake-case
    # Rename Metabolite to subject_ID
# 05 - Concentration_Maternal.urine.csv
    # Transpose data
    # Check for snake-case
    # Remove "" and , and - from headings
    # Rename Metabolite to subject_ID
# 06 - Cortisol_infant.blood.xlsx
    # Convert into csv
    # Clarify headings
    # Check for snake-case
