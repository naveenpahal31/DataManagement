# Data Quality Report

**Report Generated:** 2025-08-23 20:54:01

This report summarizes the data quality findings from the `bank_churn` dataset.

## Dataset Overview
- Total Rows: 15010
- Total Columns: 14

## Validation Findings Summary
| Category          | Description                                                                                                           |
|:------------------|:----------------------------------------------------------------------------------------------------------------------|
| Missing Data      | Missing values found in the following columns: {'Surname': 50, 'Tenure': 101, 'Balance': 100, 'EstimatedSalary': 100} |
| Data Types        | Initial data types and structure verified. See log output for details.                                                |
| Outliers          | Found 85 outliers in column 'Age'. Example: [75, 73, 79, 80, 75]                                                      |
| Inconsistent Data | Column 'HasCrCard' contains values other than 0 or 1.                                                                 |
| Duplicates        | Found 10 duplicate rows in the dataset.                                                                               |