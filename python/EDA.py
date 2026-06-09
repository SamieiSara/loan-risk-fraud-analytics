# ============================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# Loan Portfolio Risk & Fraud Analytics Project
#
# Description:
# This script performs exploratory data analysis to understand
# key patterns in the data, including distributions, outliers,
# and relationships across loan, customer, and transaction datasets.
#
# The goal is to explore distributions, outliers, and variable 
# relationships before Power BI dashboard development.
# ============================================================


# ================================
# SECTION 1: IMPORT LIBRARIES
# ================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# ================================
# SECTION 2: LOAD DATA
# ================================

applications = pd.read_csv("applications.csv")
customers = pd.read_csv("customers.csv")
transactions = pd.read_csv("transactions.csv")
risk = pd.read_csv("risk_labels.csv")


# ================================
# SECTION 3: DATA DISTRIBUTIONS
# ================================

# Loan Amount Distribution
plt.hist(applications['LoanAmount'], bins=50)
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.show()

# Credit Score Distribution
plt.hist(customers['CreditScore'], bins=50)
plt.title("Credit Score Distribution")
plt.show()


# ================================
# SECTION 4: OUTLIER DETECTION
# ================================

# Boxplot for Loan Amount
plt.boxplot(applications['LoanAmount'])
plt.title("Loan Amount Outliers")
plt.show()

# IQR Method
Q1 = applications['LoanAmount'].quantile(0.25)
Q3 = applications['LoanAmount'].quantile(0.75)
IQR = Q3 - Q1

loan_outliers = applications[
    (applications['LoanAmount'] < Q1 - 1.5 * IQR) |
    (applications['LoanAmount'] > Q3 + 1.5 * IQR)
]

print(loan_outliers)


# ================================
# SECTION 5: RELATIONSHIP ANALYSIS
# ================================

corr = customers[['Income', 'CreditScore', 'DebtToIncomeRatio']].corr()

sns.heatmap(corr, annot=True)
plt.title("Correlation Between Financial Variables")
plt.show()

# Relationship between risk and income
risk_income = customers.merge(risk, on='CustomerID')

sns.scatterplot(x='Income', y='RiskProb', data=risk_income)
plt.title("Income vs Risk Probability")
plt.show()


# ================================
# SECTION 6: FRAUD PATTERN EXPLORATION
# ================================

fraud_summary = transactions.groupby('CustomerID')['IsFraud'].sum().reset_index()

print(fraud_summary.head())
