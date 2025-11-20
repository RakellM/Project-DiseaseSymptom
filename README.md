# Project: Disease Symptom

Using Kaggle's database [link](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset/data).

## Business Problems

1. Early Disease Detection & Risk Stratification
    - Are there symptom patterns that can help clinicians diagnose diseases earlier?
    - Which symptom combinations are most strongly associated with severe diseases?
    - How can we prioritize high-severity patients in triage?

2. Resource Planning & Operational Efficiency
    - Which diseases and symptoms are rising in frequency?
    - Do certain symptom clusters predict admission surges?
    - How can we anticipate staffing needs and equipment usage (e.g., isolation rooms, ICU beds)?

3. Clinical Pathway Optimization
    - Which diseases have the longest symptom progression or highest severity scores?
    - Are our recommended precautions being followed?
    - Do certain diseases produce recurring preventable escalations?

4. Public Health & Prevention
    - Can we identify preventable diseases based on symptom/precaution patterns?
    - What education initiatives would reduce high-severity diseases?

5. What-If Scenarios for Surge Preparedness
    - What happens if a severe symptom (e.g., shortness of breath) rises 20%?
    - How would increased prevalence of certain diseases affect triage load?
    - Which diseases become dangerous if the severity weights of symptoms trend upward?


## Exploratory Data Analysis (EDA) 1

[Script: 1-understand_datasets](./src/analytics/1-understand_datasets.ipynb)

We have 4 datasets: 

- dataset.csv
- symptom_Description.csv
- symptom_precaution.csv
- Symptom-severity.csv


### 1. Dataset

Each row represents a single instance where a specific set of symptoms was associated with a confirmed diagnosis of a Disease.

Key Information:
- Contains 4,920 records of disease and symptom combinations.
- Every record has at least two symptoms (Symptom_1 and Symptom_2).
- The table captures extensive symptom lists, though the number of symptoms per entry varies widely, with many entries having fewer than the maximum 17 symptoms. The NULL or missing values indicate that not all diseases present with a full list of 17 symptoms in every recorded instance.

<details>
    <summary> <span style="color:purple"> 🗨️ Variable List </span> </summary>

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


#### Variable: Disease

- There is 41 unique diseases.
- For each unique disease we have 120 observations, we can now assume each row is a patient with an identified disease and a set of symptoms.
- `Disease` can be our target variable, and we can use the `Symptom_##` columns as our features, that will help us identified the disease.

#### Variable: Symptom_1 to Sysptom_17

Based on the overall look through these 17 columns, we have symptoms that repeats on a different column but not on the same row.
- **Question**: would the order of the symptom matter?
    - _We don't have that answer, so I would assume it doesn't_.
    - **Strategy**: We can create bolleans for each symptom and this way have a yes/nor, 1/0, answer to each individual.




| #   | Variables  | Rows  | Missing | % missing | Distinct Values | Notes                                                                                                   |
| --- | ---------- | ----- | ------- | --------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| 2   | Symptom_1  | 4,920 | 0       | -         | 34              | vomiting, fatigue and itching are the most frequent one in this column, representing 44.5% of the data. |
| 3   | Symptom_2  | 4,920 | 0       | -         | 48              | vomiting is the most frequent symptom with 17.7% of the data.                                           |
| 4   | Symptom_3  | 4,920 | 0       | -         | 54              | fatigue is the most frequent symptom with 14.8% of the data.                                            |
| 5   | Symptom_4  | 4,572 | 348     | 7%        | 50              | high_fever is the most frequent symptom with 7.7% of the data.                                          |
| 6   | Symptom_5  | 3,714 | 1,206   | 24.5%     | 38              | headache is the most frequent symptom with 7% of the data.                                              |
| 7   | Symptom_6  | 2,934 | 1,986   | 40.3%     | 32              | nausea is the most frequent symptom with 7.9% of the data.                                              |
| 8   | Symptom_7  | 2,268 | 2,652   | 53.9%     | 26              | abdominal_pain is the most frequent symptom with 5.4% of the data.                                      |
| 9   | Symptom_8  | 1,944 | 2,976   | 60.5%     | 21              | abdominal_pain is the most frequent symptom with 5.6% of the data.                                      |
| 10  | Symptom_9  | 1,692 | 3,228   | 65.6%     | 22              | yellowing_of_eyes is the most frequent symptom with 4.6% of the data.                                   |
| 11  | Symptom_10 | 1,512 | 3,408   | 69.3%     | 21              | yellowing_of_eyes is the most frequent symptom with 4% of the data.                                     |
| 12  | Symptom_11 | 1,194 | 3,726   | 75.7%     | 18              | irritability is the most frequent symptom with 2.4% of the data.                                        |
| 13  | Symptom_12 | 744   | 4,176   | 84.9%     | 11              | malaise is the most frequent symptom with 2.6% of the data.                                             |
| 14  | Symptom_13 | 504   | 4,416   | 89.8%     | 8               | muscle_pain is the most frequent symptom with 1.4% of the data.                                         |
| 15  | Symptom_14 | 306   | 4,614   | 93.8%     | 4               | chest_pain is the most frequent symptom with 1.9% of the data.                                          |
| 16  | Symptom_15 | 240   | 4,680   | 95.1%     | 3               | chest_pain is the most frequent symptom with 2.9% of the data.                                          |
| 17  | Symptom_16 | 192   | 4,728   | 96.1%     | 3               | blood_in_sputum is the most frequent symptom with 1.5% of the data.                                     |
| 18  | Symptom_17 | 72    | 4,848   | 98.5%     | 1               | muscle_pain is the most frequent symptom with 1.5% of the data.                                         |





</details>

<br>

### 2. Symptom Description

A master data or reference table that provides detailed textual descriptions for specific diseases. 
It links each disease name to an explanatory paragraph, likely used in a user interface or reporting system to provide context about the condition.

Key Information:
- Contains 41 rows, each representing a unique disease and its corresponding description.
- The table has complete data, with no missing values in either column.

<details>
    <summary> <span style="color:purple"> 🗨️ Variable List </span> </summary>

| #   | Variables   | Description                    | Type   | Rows | Missing |
| --- | ----------- | ------------------------------ | ------ | ---- | ------- |
| 1   | Disease     | Diseases experienced.          | text   | 41   | 0       |
| 2   | Description | Description about the disease. | text   | 41   | 0       |


</details>

<br>

### 3. Symptom Precaution

A reference table mapping specific diseases to actionable steps or precautions that should be taken. 
It helps in quickly identifying recommended actions for various diseases. 
This table contains 41 unique disease entries.

Key Information:
- Each row represents a unique disease and its associated precautions.
- The table structure allows for a maximum of four precautions per disease entry.
- Data integrity shows most entries have at least two precautions, while one disease lacks a third or fourth precaution entry.

<details>
    <summary> <span style="color:purple"> 🗨️ Variable List </span> </summary>

| #   | Variables    | Description          | Type   | Rows | Missing |
| --- | ------------ | -------------------- | ------ | ---- | ------- |
| 1   | Disease      | Diseases experienced | text   | 41   | 0       |
| 2   | Precaution_1 | Precaution to take   | text   | 41   | 0       |
| 3   | Precaution_2 | Precaution to take   | text   | 41   | 0       |
| 4   | Precaution_3 | Precaution to take   | text   | 40   | 1       |
| 5   | Precaution_4 | Precaution to take   | text   | 40   | 1       |



#### Variable: Disease

- There is 41 unique diseases.

#### Variable: Precaution_1 to Precaution_4

Based on the overall look through these 4 columns, we have precautions that repeats on a different column but not on the same row.
- **Question**: would the order of the precaution matter?
    - _We don't have that answer, so I would assume it doesn't_.
    - **Strategy**: We can create bolleans for each one and this way have a yes/nor, 1/0, answer to each disease.


| #   | Variables    | Rows | Missing | % missing | Distinct Values | Notes                                                      |
| --- | ------------ | ---- | ------- | --------- | --------------- | ---------------------------------------------------------- |
| 2   | Precaution_1 | 41   | 0       | -         | 31              | "consult nearest hospital" is the most frequent precaution |
| 3   | Precaution_2 | 41   | 0       | -         | 34              | "exercise" is the most frequent precaution                 |
| 4   | Precaution_3 | 40   | 1       | 2.4%      | 30              | "consult a doctor" is the most frequent precaution         |
| 5   | Precaution_4 | 40   | 1       | 2.4%      | 24              | "follow up" is the most frequent precaution                |



</details>

<br>

### 4. Symptom Severity

Table containing a list of 133 symptoms and a corresponding numerical value (weight) indicating their level of effectiveness/severity.
This table serves as a reference for categorizing patient-reported symptoms and allows for consistent data analysis. 

Key Information:
- Each row represents a unique symptom.
- The weight column is a measure of a symptom's impact or importance, quantified for analysis.
- The values in the weight column are assessed every 2 days, based on the provided context. 

<details>
    <summary> <span style="color:purple"> 🗨️ Variable List </span> </summary>

| #   | Variables | Description                        | Type   | Rows | Missing |
| --- | --------- | ---------------------------------- | ------ | ---- | ------- |
| 1   | Symptom   | Symptoms experienced by body       | text   | 133  | 0       |
| 2   | weight    | level of effectiveness per 2 days. | int64  | 133  | 0       |


#### Variable: Symptom

- There are 132 unique precautions.
- "fluid_overload" is the only one that repeats it self.
    - Need to check why it repeats, if the weight value is the sama or not and how can we fix it.

#### Variable: Weight

- integers
- Min = 1
- Max = 7
- Avg = 4.2 and Median = 4, with this one a lot close, it looks like we have a normal distribution.


</details>

### <span style="color:purple"> Notes 1: Initial Analysis </span>

Foundings so far:
- **Dataset** table: contains 4,920 records of disease and symptom combinations.
    - We can think as each row as a patient, symptoms are features and disease as target.
    - Order of the symptom does not matter. The strategy will be create a variable for each symptom.

- **Symptom** table: contains 41 records representing each disease and its description.
    - More of descriptive table.
    - Need to check if we have descrisption for all diseases in the other datasets.

- **Precaution** table: contains 41 records representing each disease and up to 4 ways to prevent it.
    - Order of the precaution does not matter. The strategy will be create a variable for each precaution.

- **Severity** table: contains 133 records representing each symptom and thei severity weight.
    - "fluid_overload" has a duplicate record with 2 different weights.
        - Modify its weight to the maximum between the 2 records.
        - We are evaluating what would be worse, weight it down and it is actually worseor weight it higher and it is actually lower. Thinking this way, assuming the maximum might be better.

