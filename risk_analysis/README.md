# Hospital Readmission Risk Prediction & Analytics Pipeline
### Domain: Healthcare Analytics (Leveraging Clinical & Operational Data)
### Tech Stack:

  - Data Storage & Processing: Snowflake
  - ETL/Data Engineering: PySpark, T-SQL, Python
  - Analytics & Visualization: Python (Pandas, Scikit-learn), VS Code (Jupyter Notebooks)
  - SQL Optimization: SQL Cookbook techniques
  - Deployment (Bonus): Docker, FastAPI (if time permits)
     
### Phase 1: Data Acquisition & Engineering (ETL Pipeline)
### Objective: Build a scalable ETL pipeline that ingests, cleans, and structures hospital data for analysis.

        Step 1: Dataset Selection - Identify & Download Healthcare Datasets:
                Primary Dataset: 
                        Diabetes 130-US Hospitals	   -     Contains readmission records for diabetic patients.    
                Secondary Data (Enrichment):
                        Medical Cost Personal Datasets -	 Demographics + medical costs.
                        Synthetic Patient EHR Data	   -     Fake but realistic patient records.  
        Step 2: Snowflake Setup:
                Design Schema:
                Final Dataset Schema:
                        Table	       -         Columns
                        PATIENTS       -         patient_id, age, gender, comorbidities, admission_date, discharge_date, readmitted
                        LABS	       -         lab_id, patient_id, glucose, creatinine, test_date
                        DIAGNOSES      -         diagnosis_id, patient_id, icd_code, description (from Kaggle)
        Step 3: PySpark ETL Pipeline:
                Extract: Read CSV/JSON files (or API calls if using CMS data):
                Transform:
                        Clean missing values (impute median for labs, drop duplicates).
                        Derive features (e.g., "days_to_readmission").
                        Normalize lab results (Z-score).
                Load: Write to Snowflake via JDBC Java Database Connectivity.
