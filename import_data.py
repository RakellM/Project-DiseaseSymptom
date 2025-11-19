# %%

## LIBRARY
import os
import kaggle

# %%

## PATH & OTHERS
# Project Directory
project_dir = os.path.join(os.path.expanduser("~"), "OneDrive", "Project_Code", "Project-DiseaseSymptom-Kaggle")

# Data path
data_raw_path = os.path.join(project_dir, "data", "raw")
os.makedirs(data_raw_path, exist_ok=True)

data_processed_path = os.path.join(project_dir, "data", "processed")
os.makedirs(data_processed_path, exist_ok=True)

data_srcA_path = os.path.join(project_dir, "src", "analytics")
os.makedirs(data_srcA_path, exist_ok=True)

data_srcE_path = os.path.join(project_dir, "src", "EDA")
os.makedirs(data_srcE_path, exist_ok=True)

# %%
## DATA
# Download data from Kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files('itachi9604/disease-symptom-description-dataset', 
                                  path=data_raw_path, 
                                  unzip=True)

# %%
