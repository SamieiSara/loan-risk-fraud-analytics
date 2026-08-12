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
import os
os.makedirs("charts", exist_ok=True)

# ================================
# SECTION 2: LOAD DATA
# ================================

applications = pd.read_csv("applications.csv")
customers = pd.read_csv("customers.csv")
transactions = pd.read_csv("transactions.csv")
risk = pd.read_csv("risk_labels.csv")

# Quick sanity check on all loaded tables
for name, df in [("applications", applications), ("customers", customers),
                 ("transactions", transactions), ("risk", risk)]:
    print(f"\n--- {name} ---")
    print(f"Shape: {df.shape}")
    print(df.head(3))


# ================================
# SECTION 3: DATA DISTRIBUTIONS
# ================================

# Loan Amount Distribution
plt.figure(figsize=(10, 5))
plt.hist(applications['LoanAmount'], bins=50, color='steelblue', edgecolor='white')
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/loan_amount_distribution.png", dpi=150, bbox_inches='tight')
plt.show()

# Income Distribution
plt.figure(figsize=(10, 5))
plt.hist(customers['Income'], bins=50, color='steelblue', edgecolor='white')
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/income_distribution.png", dpi=150, bbox_inches='tight')
plt.show()

# Credit Score Distribution
plt.figure(figsize=(10, 5))
plt.hist(customers['CreditScore'], bins=50, color='steelblue', edgecolor='white')
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/credit_score_distribution.png", dpi=150, bbox_inches='tight')
plt.show()


# ================================
# SECTION 4: OUTLIER DETECTION
# ================================

# Boxplot for Loan Amount
plt.figure(figsize=(8, 5))
plt.boxplot(applications['LoanAmount'])
plt.title("Loan Amount Outliers")
plt.ylabel("Loan Amount ($)")
plt.tight_layout()
plt.savefig("charts/loan_amount_outliers.png", dpi=150, bbox_inches='tight')
plt.show()

# IQR Method
Q1 = applications['LoanAmount'].quantile(0.25)
Q3 = applications['LoanAmount'].quantile(0.75)
IQR = Q3 - Q1
loan_outliers = applications[
    (applications['LoanAmount'] < Q1 - 1.5 * IQR) |
    (applications['LoanAmount'] > Q3 + 1.5 * IQR)
]
print(f"Loan Amount outliers: {len(loan_outliers)} records "
      f"({100 * len(loan_outliers) / len(applications):.1f}% of applications)")

# --- Income ---
plt.figure(figsize=(8, 5))
plt.boxplot(customers['Income'])
plt.title("Income Outliers")
plt.ylabel("Income ($)")
plt.tight_layout()
plt.savefig("charts/income_outliers.png", dpi=150, bbox_inches='tight')
plt.show()

Q1 = customers['Income'].quantile(0.25)
Q3 = customers['Income'].quantile(0.75)
IQR = Q3 - Q1
income_outliers = customers[
    (customers['Income'] < Q1 - 1.5 * IQR) |
    (customers['Income'] > Q3 + 1.5 * IQR)
]
print(f"Income outliers: {len(income_outliers)} records "
      f"({100 * len(income_outliers) / len(customers):.1f}% of customers)")

# --- Credit Score ---
plt.figure(figsize=(8, 5))
plt.boxplot(customers['CreditScore'])
plt.title("Credit Score Outliers")
plt.ylabel("Credit Score")
plt.tight_layout()
plt.savefig("charts/credit_score_outliers.png", dpi=150, bbox_inches='tight')
plt.show()

Q1 = customers['CreditScore'].quantile(0.25)
Q3 = customers['CreditScore'].quantile(0.75)
IQR = Q3 - Q1
credit_outliers = customers[
    (customers['CreditScore'] < Q1 - 1.5 * IQR) |
    (customers['CreditScore'] > Q3 + 1.5 * IQR)
]
print(f"Credit Score outliers: {len(credit_outliers)} records "
      f"({100 * len(credit_outliers) / len(customers):.1f}% of customers)")

# Outliers retained — flagged for review in Power BI risk segmentation

# ================================
# SECTION 5: RELATIONSHIP ANALYSIS
# ================================
# Merge customers with risk labels to include RiskProb
customers_risk = customers.merge(risk, on='CustomerID')

# Correlation heatmap across key financial variables including risk
corr = customers_risk[['Income', 'CreditScore', 'DebtToIncomeRatio', 'RiskProb']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Financial Variables")
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png", dpi=150, bbox_inches='tight')
plt.show()
# Finding: review correlation values after running to note key relationships

# Income vs Risk Probability
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Income', y='RiskProb', data=customers_risk, alpha=0.3, color='steelblue')
plt.title("Income vs Risk Probability")
plt.xlabel("Income ($)")
plt.ylabel("Risk Probability")
plt.tight_layout()
plt.savefig("charts/income_vs_risk.png", dpi=150, bbox_inches='tight')
plt.show()

# ================================
# SECTION 6: FRAUD PATTERN EXPLORATION
# ================================

# Overall fraud rate
fraud_rate = transactions['IsFraud'].mean() * 100
print(f"Overall fraud rate: {fraud_rate:.2f}% of all transactions")

# Fraud count per customer — top fraud-flagged accounts
fraud_summary = transactions.groupby('CustomerID')['IsFraud'].sum().reset_index()
fraud_summary.columns = ['CustomerID', 'FraudCount']
print("\nTop 10 customers by fraud flag count:")
print(fraud_summary[fraud_summary['FraudCount'] > 0]
      .sort_values('FraudCount', ascending=False)
      .head(10))

# Fraud rate by transaction type
fraud_by_type = (transactions.groupby('TransactionType')['IsFraud']
                 .mean()
                 .reset_index()
                 .sort_values('IsFraud', ascending=False))
fraud_by_type.columns = ['TransactionType', 'FraudRate']
fraud_by_type['FraudRate'] = fraud_by_type['FraudRate'] * 100

plt.figure(figsize=(8, 5))
plt.bar(fraud_by_type['TransactionType'], fraud_by_type['FraudRate'],
        color='steelblue', edgecolor='white')
plt.title("Fraud Rate by Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Fraud Rate (%)")
plt.tight_layout()
plt.savefig("charts/fraud_rate_by_transaction_type.png", dpi=150, bbox_inches='tight')
plt.show()

# Fraud rate by loan purpose (merge transactions with applications)
fraud_purpose = transactions.merge(applications[['CustomerID', 'LoanPurpose']],
                                   on='CustomerID', how='left')
fraud_by_purpose = (fraud_purpose.groupby('LoanPurpose')['IsFraud']
                    .mean()
                    .reset_index()
                    .sort_values('IsFraud', ascending=False))
fraud_by_purpose.columns = ['LoanPurpose', 'FraudRate']
fraud_by_purpose['FraudRate'] = fraud_by_purpose['FraudRate'] * 100

plt.figure(figsize=(10, 5))
plt.bar(fraud_by_purpose['LoanPurpose'], fraud_by_purpose['FraudRate'],
        color='steelblue', edgecolor='white')
plt.title("Fraud Rate by Loan Purpose")
plt.xlabel("Loan Purpose")
plt.ylabel("Fraud Rate (%)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("charts/fraud_rate_by_loan_purpose.png", dpi=150, bbox_inches='tight')
plt.show()
