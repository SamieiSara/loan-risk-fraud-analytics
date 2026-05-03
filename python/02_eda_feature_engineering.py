# ============================================================
# EXPLORATORY DATA ANALYSIS & FEATURE ENGINEERING
# Loan Portfolio Risk & Fraud Analytics Project
#
# Description:
# This script performs exploratory data analysis (EDA),
# outlier detection, and feature engineering to uncover
# patterns in loan, customer, and transaction data.
#
# Output:
# Cleaned and enriched datasets for downstream use in Power BI.
# ============================================================


# ================================
# SECTION 1: IMPORT LIBRARIES
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ================================
# SECTION 2: LOAD DATA
# ================================

applications = pd.read_csv("applications.csv")
customers = pd.read_csv("customers.csv")
transactions = pd.read_csv("transactions.csv")
risk = pd.read_csv("risk_labels.csv")


# ================================
# SECTION 3: DATA OVERVIEW
# ================================

print("Applications Shape:", applications.shape)
print("Customers Shape:", customers.shape)

print("\nCustomer Data Types:")
print(customers.dtypes)

print("\nCustomer Summary Statistics:")
print(customers.describe())


# ================================
# SECTION 4: MISSING VALUES CHECK
# ================================

print("\nMissing Values - Customers:")
print(customers.isnull().sum())

print("\nMissing Values - Applications:")
print(applications.isnull().sum())


# ================================
# SECTION 5: OUTLIER DETECTION
# ================================

# Distribution of Loan Amount
plt.figure()
plt.hist(applications['LoanAmount'], bins=50)
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.show()

# Boxplot for Loan Amount
plt.figure()
plt.boxplot(applications['LoanAmount'])
plt.title("Loan Amount Outliers")
plt.show()

# IQR Method for Outlier Detection
Q1 = applications['LoanAmount'].quantile(0.25)
Q3 = applications['LoanAmount'].quantile(0.75)
IQR = Q3 - Q1

loan_outliers = applications[
    (applications['LoanAmount'] < Q1 - 1.5 * IQR) |
    (applications['LoanAmount'] > Q3 + 1.5 * IQR)
]

print("\nLoan Amount Outliers:")
print(loan_outliers)


# ================================
# SECTION 6: CORRELATION ANALYSIS
# ================================

corr_matrix = customers[['Income', 'CreditScore', 'DebtToIncomeRatio']].corr()

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


# ================================
# SECTION 7: FEATURE ENGINEERING
# ================================

# Risk Bands
risk['Risk_Band'] = pd.cut(
    risk['RiskProb'],
    bins=[0, 0.3, 0.7, 1],
    labels=['Low', 'Medium', 'High']
)

# Income Buckets
customers['Income_Bucket'] = pd.cut(
    customers['Income'],
    bins=[0, 40000, 80000, 150000],
    labels=['Low', 'Medium', 'High']
)

# Customer Segmentation
def segment_customer(row):
    if row['Income'] > 100000 and row['CreditScore'] > 700:
        return 'Premium'
    elif row['Income'] > 50000:
        return 'Advance'
    else:
        return 'Basic'

customers['Customer_Type'] = customers.apply(segment_customer, axis=1)

# Fraud Count per Customer
fraud_summary = (
    transactions.groupby('CustomerID')['IsFraud']
    .sum()
    .reset_index()
    .rename(columns={'IsFraud': 'Fraud_Count'})
)


# ================================
# SECTION 8: GROUP ANALYSIS
# ================================

# Merge datasets for analysis
merged = customers.merge(risk, on='CustomerID')

# Average risk by income bucket
risk_by_income = merged.groupby('Income_Bucket')['RiskProb'].mean()

print("\nAverage Risk by Income Bucket:")
print(risk_by_income)


# ================================
# SECTION 9: EXPORT CLEAN DATA
# ================================

customers.to_csv("clean_customers.csv", index=False)
applications.to_csv("clean_applications.csv", index=False)

print("\nClean datasets exported successfully.")
