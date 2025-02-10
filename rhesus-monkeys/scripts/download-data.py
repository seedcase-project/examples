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
        "https://zenodo.org/records/7055715/files/Concentration_Infant.blood.csv?download=1", #01
        "https://zenodo.org/records/7055715/files/Concentration_Infant.urine.csv?download=1",
        "https://zenodo.org/records/7055715/files/Concentration_Maternal.blood.csv?download=1",
        "https://zenodo.org/records/7055715/files/Concentration_Maternal.placenta.csv?download=1",
        "https://zenodo.org/records/7055715/files/Concentration_Maternal.urine.csv?download=1", #05
        "https://zenodo.org/records/7055715/files/Cortisol_infant.blood.xlsx?download=1",
        "https://zenodo.org/records/7055715/files/Metadata_Infant.blood.csv?download=1",
        "https://zenodo.org/records/7055715/files/Metadata_Infant.urine.csv?download=1",
        "https://zenodo.org/records/7055715/files/Metadata_Maternal.blood.csv?download=1",
        "https://zenodo.org/records/7055715/files/Metadata_Maternal.urine.csv?download=1", #10
        "https://zenodo.org/records/7055715/files/Metadata_Maternal.placenta.csv?download=1",
        "https://zenodo.org/records/7055715/files/Cytokine_Infant.blood.csv?download=1",
        "https://zenodo.org/records/7055715/files/Cytokine_Maternal.blood.csv?download=1",
        "https://zenodo.org/records/7055715/files/WB_Infant.brain.csv?download=1",
        "https://zenodo.org/records/7055715/files/HI_infant.behavior.xlsx?download=1", #15
        "https://zenodo.org/records/7055715/files/VPC_infant.cognitive.xlsx?download=1",
        "https://zenodo.org/records/7055715/files/Gestational.weight.gain.rate.csv?download=1"
    ]
    names = [
        "data01.csv",
        "data02.csv",
        "data03.csv",
        "data04.csv",
        "data05.csv",
        "data06.xlsx",
        "data07.csv",
        "data08.csv",
        "data09.csv",
        "data10.csv",
        "data11.csv",
        "data12.csv",
        "data13.csv",
        "data14.csv",
        "data15.xlsx",
        "data16.xlsx",
        "data17.csv",

    ]

    # Loop through the URLs and names and call the function for each pair
    for url, name in zip(urls, names):
        download_data(url, name)

'''
1 - Concentration_Infant.blood.csv
* Columns: Samples. The same “Exp” represent the same sample in Metadata_Infant.blood.csv & Cytokine_Infant.blood.csv files.
* Rows: Metabolites
* The unit is uM. 

2 - Concentration_Infant.urine.csv
* Columns: Samples. The same “Exp” represent the same sample in Metadata_Infant.urine.csv file.
* Rows: Metabolites
* The unit is uM. 

3 - Concentration_Maternal.blood.csv
* Columns: Sample IDs. The same “Exp” represent the same sample in Concentration_Maternal.blood.csv, Cytokine_Infant.blood.csv, and Metadata_Maternal.blood.csv files. 
* Rows: Metabolites
* The unit is uM. 

4 - Concentration_Maternal.placenta.csv
* Columns: Samples. The same “Exp” represent the same sample in Metadata_Maternal.placenta.csv file.
* Rows: Metabolites
* The unit is uM.

5 - Concentration_Maternal.urine.csv
* Columns: Samples. The same “Exp” represent the same sample in Metadata_Maternal.urine.csv file.
* Rows: Metabolites
* The unit is uM. 

6 - Cortisol_Infant.blood.csv
* Variables 
o Infant_ID: IDs of infants. 
o Group: Lean or Obese.
o PD: Exact postnatal day (PD) when samples were collected.
o Mother_ID: IDs of mothers. 
o Foster_ID: IDs of foster mothers. 
o Infant_weight: Infant weights (kg) recorded at samples collection. 
o samp1: Cortisol level from the 1st blood samples collected from infants at 11am, after being separated from mothers at 9am. 
o samp2: Cortisol level from the 2nd blood samples collected 4 pm. After the blood collection, 500 ?g/kg dexamethasone was injected intramuscularly. 
o samp3: Cortisol level from the 3rd blood samples collected at 8:30 am of the following day. After the blood collection, 2.5 IU of adrenocorticotropic hormone (ACTH) was injected intramuscularly.
o samp4: Cortisol level from the 4th blood samples collected 30 min after ACTH injection. 
o pctsuppression: Values obtained by dividing samp3 by samp2.
* Missing data codes: Indicated by NAs.

7 - Metadata_Infant.blood.csv
* Variables 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Infant.blood.csv & Cytokine_Infant.blood.csv files.
o Infant_ID: IDs of infants. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o PD: Exact postnatal day (PD) when samples were collected.
o Target_PD: Target PD for sample collection. 
o Dilution_factor: Dilution factor used to prepare NMR samples. 
o Mother_ID: IDs of mothers. 
o GD_Delivery: Gestational day at delivery. 
o Mode_birth: Mode of delivery.
o Fostered: Yes (fostered) or No (was not fostered).
o Foster_ID: IDs of foster mothers. 
o Weight_PD7: Infant weights recorded at around PD7.
o ActualDay_PD7: Actual day for “Weight_PD7”. 
o Infant_weight: Infant weights (kg) recorded at samples collection. 
* Missing data codes: Indicated by NAs.

8 - Metadata_Infant.urine.csv
* Variables 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Infant.urine.csv file.
o Infant_ID: IDs of infants. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o PD: Exact postnatal day (PD) when samples were collected.
o Target_PD: Target PD for sample collection. 
o Dilution_factor: Dilution factor used to prepare NMR samples. 
o Mother_ID: IDs of mothers. 
o GD_Delivery: Gestational day at delivery. 
o Mode_birth: Mode of delivery.
o Fostered: Yes (fostered) or No (was not fostered).
o Foster_ID: IDs of foster mothers. 
o Infant_weight: Infant weights (kg) recorded at samples collection. 
* Missing data codes: Indicated by NAs.

9 - Metadata_Maternal.blood.csv
* Variables 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Maternal.blood.csv, Cytokine_Infant.blood.csv, and Metadata_Maternal.blood.csv files.
o Mother_ID: IDs of mothers. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o GD: Exact gestational day (GD) when samples were collected.
o Target_GD: Target GD for sample collection. 
o Dilution_factor: Dilution factor used to prepare NMR samples. 
o BCS: Body Condition Score (BCS) 
o Mother_Weight: Maternal weight in kg at sample collection. 
o Mother_age: Maternal age at conception. 
o GD_Delivery: Gestational day at delivery. 
o Infant_sex: Infant sex.
o Mode_birth: Mode of delivery.
o Reject: Whether mothers rejected infants or not. 
o Placenta_Width: Width of placenta at sample collection.
o Placenta_Height: Height of placenta at sample collection.
o Placenta_Thickness: Thickness of placenta at sample collection.
o EPV: Estimated placental volume. 
* Missing data codes: Indicated by NAs.

10 - Metadata_Maternal.urine.csv
* Variables 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Maternal.urine.csv file.
o Mother_ID: IDs of mothers. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o GD: Exact gestational day (GD) when samples were collected.
o Target_GD: Target GD for sample collection. 
o Dilution_factor: Dilution factor used to prepare NMR samples. 
o BCS: Body Condition Score (BCS) 
o Mother_Weight: Maternal weight in kg at sample collection. 
o Mother_age: Maternal age at conception. 
o GD_Delivery: Gestational day at delivery. 
o Infant_sex: Infant sex.
o Mode_birth: Mode of delivery.
* Missing data codes: Indicated by NAs.

11 - Metadata_Maternal.placenta.csv
* Variables 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Maternal.placenta.csv file.
o Mother_ID: IDs of mothers. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o GD: Exact gestational day (GD) when samples were collected.
o Target_GD: Target GD for sample collection. 
o Dilution_factor: Dilution factor used to prepare NMR samples. 
o BCS: Body Condition Score (BCS) 
o Tissue_weight: Weight of placental tissue sample. 
o V1: Volume of solvent used to extract (uL). Used to correct the metabolite concentration.
o V2: Volume of polar layer (methanol + water) collected (uL). Used to correct the metabolite concentration.
o V3: Buffer added to reconstitute the sample after freeze drying (uL). Used to correct the metabolite concentration. 
* Missing data codes: Indicated by NAs.

12 - Cytokine_Infant.blood
* Variables: 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Infant.blood.csv & Metadata_Infant.blood.csv files.
o Infant_ID: IDs of infants. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o PD: Exact postnatal day (PD) when samples were collected.
o Target_PD: Target PD for sample collection. 
o Mother_ID: IDs of mothers.
o GD_Delivery: Gestational day at delivery. 
o Mode_birth: Mode of delivery.
o Fostered: Yes (fostered) or No (was not fostered).
o Foster_ID: IDs of foster mothers. 
o Weight_PD7: Infant weights recorded at around PD7.
o hsCPP, GM_CSF, IFN_g, IL_1b, IL_ra, IL_2, IL_4, IL_5, IL_6, IL_8, IL_10, IL_12.23_p40, IL_13, IL_15, 
IL_17a, MCP_1, MIP_1b, sCD40L_38, TGFa, TNFa, VEGF, C_Peptide, GIP, Inflammatory markers. 
o Insulin: Insulin level (pg/mL).
* Missing data codes: Indicated by NAs.
* Specialized formats or other abbreviations used: GD, gestational day; BCS, Body Condition Score; 
GM-CSF, granulocyte-macrophage colony-stimulating factor; IFN- ?, interferon ?; TNF-?, tumor necrosis factor-?; 
TGF-?, transforming growth factor-?; MCP-1, monocyte chemoattractant protein-1; MIP-1?, macrophage inflammatory protein-1?; 
hs-CRP, high-sensitivity C-reactive protein; IL, interleukin.

13 - Cytokine_Maternal.blood
* Variables: 
o Exp: Samples IDs. The same “Exp” represent the same sample in Concentration_Maternal.blood.csv, Cytokine_Infant.blood.csv, and Metadata_Maternal.blood.csv files.
o Mother_ID: IDs of mothers. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o GD: Exact gestational day (GD) when samples were collected.
o Target_GD: Target GD for sample collection. 
o BCS: Body Condition Score (BCS) 
o hsCPP, GM_CSF, IFN_g, IL_1b, IL_ra, IL_2, IL_6, IL_8, IL_10, IL_12/23_p40, IL_13, IL_15, 
IL_17a, MCP_1, MIP_1b, sCD40L, TGFa, VEGF, C_Peptide, GIP, PP_53, PYY_54: Inflammatory markers. 
o Insulin: Insulin level (uU/mL)
* Missing data codes: Indicated by NAs.
* Specialized formats or other abbreviations used: GD, gestational day; BCS, Body Condition Score; 
hs-CRP, high-sensitivity C-reactive protein; GM_CSF, granulocyte-macrophage colony-stimulating factor; 
IFN- ?, interferon-?; TNF-?, tumor necrosis factor-?; TGF-?, transforming growth factor-?; 
MCP-1, monocyte chemoattractant protein-1; MIP-1?, macrophage inflammatory protein-1?; IL, interleukin; 
IL-1ra, IL-1 receptor antagonist.

14 - WB.infant.brain
* Variables
o Infant_ID: IDs of infants.
o Brain_region: Amygdala, Hippocampus, Hypothalamus, P.Cortex (= prefrontal cortex)
o Group: Lean or Obese.
o Akt, p.Akt, AMPK, p.AMPK, S6K, p.S6K: Normalized relative intensity levels.

15 - HI_infant.behavior
* Variables 
o Infant_ID: IDs of infants. 
o Group: Lean or Obese.
o PD: Exact postnatal day (PD) when samples were collected.
o Mother_ID: IDs of mothers. 
o Foster_ID: IDs of foster mothers. 
o Infant_weight: Infant weights (kg) recorded at samples collection. 
o pfscratch: Profile-Far (technician presented the left profile from ~1 m away from an infant in a cage)
o pnscratch: Profile-Near (presented left profile from ~0.3 m)
o sfscratch: Stare-Far (made direct eye contact with the animal from far)
o snscratch: Stare-Near (direct eye contact from near position)
* Missing data codes: Indicated by NAs.

16 - VPC_infant_cognitive
* Variables 
o Infant_ID: IDs of infants. 
o Mother_ID: IDs of mothers. 
o Foster_ID: IDs of foster mothers. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o GD_Delivery: Gestational day at delivery. 
o PCD: post-conception day.
o PxTx Total number Look RIGHT/LEFT FAM: Total number of looks at a familiar object that was placed right or left side. P stands for the number of problem (1 to 4) and T stands for the number of Trial (1 or 2). 
o PxTx Total number Look RIGHT/LEFT NOVEL: Total number of looks at a novel object that was placed right or left side. P stands for the number of problem (1 to 4) and T stands for the number of Trial (1 or 2).
o PxTx Total number Look Away: Total number of looks away from either of the object. P stands for the number of problem (1 to 4) and T stands for the number of Trial (1 or 2).
o no.looks_N: Total number of looks at novel object throughout the problems and trials. 
o no.looks_F: Total number of looks at familiar object throughout the problems and trials.
o no.looks_N+F: Total number of looks at novel and familiar object throughout the problems and trials.
o no.looks_N/N+F: Novelty preference calculated as: number of fixations at the novel stimulus (no.looks_N)/number of fixations at both the novel and familiar stimulus (no.looks_N+F).

17 - Gestational.weight.gain.rate
* Variables 
o Mother_ID: IDs of mothers. 
o Batch: The experiment was conducted over two batches (Batch1 or Batch2)
o Group: Lean or Obese.
o Infant_ID: IDs of infants. 
o Foster_ID: IDs of foster mothers. 
o GWG: Gestational weight gain rate. 
'''
