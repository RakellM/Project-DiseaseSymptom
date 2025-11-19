# Project: Disease Symptom

Using Kaggle's database [link](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset/data).


## Datasets

We have 4 datasets: 

- dataset.csv
- symptom_Description.csv
- symptom_precaution.csv
- Symptom-severity.csv


### 1. Dataset

A data table used likely for training a machine learning model or conducting extensive data analysis. 
Each row represents a single instance where a specific set of symptoms was associated with a confirmed diagnosis of a Disease.

Key Information:
- Contains 4,920 records of disease and symptom combinations.
- Every record has at least two symptoms (Symptom_1 and Symptom_2).
- The table captures extensive symptom lists, though the number of symptoms per entry varies widely, with many entries having fewer than the maximum 17 symptoms. The NULL or missing values indicate that not all diseases present with a full list of 17 symptoms in every recorded instance.


| #   | Variables  | Description                                 | Type   | Rows  | Missing |
| --- | ---------- | ------------------------------------------- | ------ | ----- | ------- |
| 1   | Disease    | Diseases that may be present                | text   | 4,920 | 0       |
| 2   | Symptom_1  | The symptoms experienced during the disease | text   | 4,920 | 0       |
| 3   | Symptom_2  | The symptoms experienced during the disease | text   | 4,920 | 0       |
| 4   | Symptom_3  | The symptoms experienced during the disease | text   | 4,920 | 0       |
| 5   | Symptom_4  | The symptoms experienced during the disease | text   | 4,572 | 348     |
| 6   | Symptom_5  | The symptoms experienced during the disease | text   | 3,714 | 1,206   |
| 7   | Symptom_6  | The symptoms experienced during the disease | text   | 2,934 | 1,986   |
| 8   | Symptom_7  | The symptoms experienced during the disease | text   | 2,268 | 2,652   |
| 9   | Symptom_8  | The symptoms experienced during the disease | text   | 1,944 | 2,976   |
| 10  | Symptom_9  | The symptoms experienced during the disease | text   | 1,692 | 3,228   |
| 11  | Symptom_10 | The symptoms experienced during the disease | text   | 1,512 | 3,408   |
| 12  | Symptom_11 | The symptoms experienced during the disease | text   | 1,194 | 3,726   |
| 13  | Symptom_12 | The symptoms experienced during the disease | text   | 744   | 4,176   |
| 14  | Symptom_13 | The symptoms experienced during the disease | text   | 504   | 4,416   |
| 15  | Symptom_14 | The symptoms experienced during the disease | text   | 306   | 4,614   |
| 16  | Symptom_15 | The symptoms experienced during the disease | text   | 240   | 4,680   |
| 17  | Symptom_16 | The symptoms experienced during the disease | text   | 192   | 4,728   |
| 18  | Symptom_17 | The symptoms experienced during the disease | text   | 72    | 4,848   |


<br>

2. Symptom Description

A master data or reference table that provides detailed textual descriptions for specific diseases. 
It links each disease name to an explanatory paragraph, likely used in a user interface or reporting system to provide context about the condition.

Key Information:
- Contains 41 rows, each representing a unique disease and its corresponding description.
- The table has complete data, with no missing values in either column.


| #   | Variables   | Description                    | Type   | Rows | Missing |
| --- | ----------- | ------------------------------ | ------ | ---- | ------- |
| 1   | Disease     | Diseases experienced.          | text   | 41   | 0       |
| 2   | Description | Description about the disease. | text   | 41   | 0       |


<br>

3. Symptom Precaution

A reference table mapping specific diseases to actionable steps or precautions that should be taken. 
It helps in quickly identifying recommended actions for various diseases. 
This table contains 41 unique disease entries.

Key Information:
- Each row represents a unique disease and its associated precautions.
- The table structure allows for a maximum of four precautions per disease entry.
- Data integrity shows most entries have at least two precautions, while one disease lacks a third or fourth precaution entry.


| #   | Variables    | Description          | Type   | Rows | Missing |
| --- | ------------ | -------------------- | ------ | ---- | ------- |
| 1   | Disease      | Diseases experienced | text   | 41   | 0       |
| 2   | Precaution_1 | Precaution to take   | text   | 41   | 0       |
| 3   | Precaution_2 | Precaution to take   | text   | 41   | 0       |
| 4   | Precaution_3 | Precaution to take   | text   | 40   | 1       |
| 5   | Precaution_4 | Precaution to take   | text   | 40   | 1       |


<br>

4. Symptom Severity

Table containing a list of 133 symptoms and a corresponding numerical value (weight) indicating their level of effectiveness/severity.
This table serves as a reference for categorizing patient-reported symptoms and allows for consistent data analysis. 

Key Information:
- Each row represents a unique symptom.
- The weight column is a measure of a symptom's impact or importance, quantified for analysis.
- The values in the weight column are assessed every 2 days, based on the provided context. 


| #   | Variables | Description                        | Type   | Rows | Missing |
| --- | --------- | ---------------------------------- | ------ | ---- | ------- |
| 1   | Symptom   | Symptoms experienced by body       | text   | 133  | 0       |
| 2   | weight    | level of effectiveness per 2 days. | int64  | 133  | 0       |


