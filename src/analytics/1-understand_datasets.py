# %%

## LIBRARY
import os
import pandas as pd

# %%

## PATH & OTHERS
# Project Directory
project_dir = os.path.join(os.path.expanduser("~"), "OneDrive", "Project_Code", "Project-DiseaseSymptom-Kaggle")

# %%

## IMPORT DATA
df_dataset = pd.read_csv(os.path.join(project_dir, "data/raw/", "dataset.csv"))
df_sympDesc = pd.read_csv(os.path.join(project_dir, "data/raw/", "symptom_Description.csv"))
df_sympPrec = pd.read_csv(os.path.join(project_dir, "data/raw/", "symptom_precaution.csv"))
df_sympSev = pd.read_csv(os.path.join(project_dir, "data/raw/", "Symptom-severity.csv"))

# %%

## EDA - Univariable
# Let's understand the dataset

### Dataset
df_dataset.info()

# %%
### symptom_Description
df_sympDesc.info()

# %%
### symptom_precaution
df_sympPrec.info()

# %%
### Symptom-severity
df_sympSev.info()

# %%
