#%pip install pandas numpy scikit-learn matplotlib seaborn sqlite3

import pandas as pd
import numpy as np
import os
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

################################################################################
# 1. Synthetic Data Generation
################################################################################

def generate_synthetic_data(num_records=2000):
    """
    Generates a synthetic bank customer churn dataset with added data quality issues.
    
    Args:
        num_records (int): The number of records to generate.
    
    Returns:
        pd.DataFrame: A DataFrame with synthetic data and quality issues.
    """
    print(f"Starting synthetic data generation for {num_records} records.")
    
    # Define columns and their data generation logic
    data = {
        'RowNumber': range(1, num_records + 1),
        'CustomerId': np.random.randint(15000000, 16000000, size=num_records),
        'Surname': np.random.choice([
            'Smith', 'Jones', 'Williams', 'Brown', 'Garcia', 'Lee', 'Kim', 'Muller'
        ], size=num_records),
        'CreditScore': np.random.randint(300, 851, size=num_records),
        'Geography': np.random.choice(['France', 'Spain', 'Germany', 'unknown'], size=num_records),
        'Gender': np.random.choice(['Female', 'Male', 'other'], size=num_records),
        'Age': np.random.randint(18, 70, size=num_records),
        'Tenure': np.random.randint(0, 11, size=num_records),
        'Balance': np.random.randint(0, 250000, size=num_records) + np.random.random(num_records),
        'NumOfProducts': np.random.randint(1, 5, size=num_records),
        'HasCrCard': np.random.choice([0, 1, 99], size=num_records), # Inconsistent data
        'IsActiveMember': np.random.choice([0, 1], size=num_records),
        'EstimatedSalary': np.random.randint(0, 200000, size=num_records) + np.random.random(num_records),
        'Exited': np.random.randint(0, 2, size=num_records)
    }

    df = pd.DataFrame(data)
    
    # Introduce deliberate data quality issues
    # Add missing values (NaN)
    for col in ['Balance', 'Tenure', 'EstimatedSalary']:
        df.loc[df.sample(frac=0.02).index, col] = np.nan
    
    # Add empty values (empty strings)
    df.loc[df.sample(frac=0.01).index, 'Surname'] = ''

    # Add duplicate rows
    duplicate_rows = df.sample(n=10, random_state=1).copy()
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    return df

def save_data_to_csv(df, filename="raw_data_with_issues.csv"):
    """
    Saves a DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The name of the output file.
    """
    print("-" * 50)
    print(f"Saving generated data to '{filename}'...")
    try:
        df.to_csv(filename, index=False)
        print(f"Data successfully saved to {os.path.abspath(filename)}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
