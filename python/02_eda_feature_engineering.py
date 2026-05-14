# ============================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# Loan Portfolio Risk & Fraud Analytics Project
#
# Description:
# This script performs exploratory data analysis to understand
# data distributions, detect outliers, and explore relationships
# across loan, customer, and transaction datasets.
#
# Output:
# Cleaned and enriched datasets for downstream use in Power BI.
# ============================================================


# ================================
# SECTION 1: IMPORT LIBRARIES
# ================================

import pandas as pd
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
# SECTION 3: INITIAL DATA CHECK
# ================================

# Quick sanity check before analysis
print("Applications Shape:", applications.shape)
print("Customers Shape:", customers.shape)
print("Transactions Shape:", transactions.shape)


# ================================
# SECTION 4: DISTRIBUTION ANALYSIS
# ================================

# Loan Amount Distribution
plt.figure()
plt.hist(applications['LoanAmount'], bins=50)
plt.title("Distribution of Loan Amount")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.show()

# Customer Income Distribution
plt.figure()
plt.hist(customers['Income'], bins=50)
plt.title("Distribution of Customer Income")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

# Credit Score Distribution
plt.figure()
plt.hist(customers['CreditScore'], bins=50)
plt.title("Distribution of Credit Score")
plt.xlabel("Credit Score")
plt.ylabel("Frequency")
plt.show()


# ================================
# SECTION 5: OUTLIER DETECTION
# ================================

# Boxplot for Loan Amount
plt.figure()
plt.boxplot(applications['LoanAmount'])
plt.title("Loan Amount Outliers")
plt.show()

# IQR method for detecting extreme values
Q1 = applications['LoanAmount'].quantile(0.25)
Q3 = applications['LoanAmount'].quantile(0.75)
IQR = Q3 - Q1

loan_outliers = applications[
    (applications['LoanAmount'] < Q1 - 1.5 * IQR) |
    (applications['LoanAmount'] > Q3 + 1.5 * IQR)
]

print("\nNumber of Loan Amount Outliers:", len(loan_outliers))


# ================================
# SECTION 6: RELATIONSHIP ANALYSIS
# ================================

# Merge customer and risk data for analysis
merged = customers.merge(risk, on='CustomerID')

# Income vs Risk Probability
plt.figure()
sns.scatterplot(data=merged, x='Income', y='RiskProb')
plt.title("Income vs Risk Probability")
plt.show()

# Credit Score vs Risk Probability
plt.figure()
sns.scatterplot(data=merged, x='CreditScore', y='RiskProb')
plt.title("Credit Score vs Risk Probability")
plt.show()

# Correlation Matrix
corr = merged[['Income', 'CreditScore', 'DebtToIncomeRatio', 'RiskProb']].corr()

plt.figure()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Between Financial Variables")
plt.show()


# ================================
# SECTION 7: FRAUD EXPLORATION
# ================================

# Overall fraud rate
fraud_rate = transactions['IsFraud'].mean()
print("\nOverall Fraud Rate:", fraud_rate)

# Fraud rate by merchant category
fraud_by_category = transactions.groupby('MerchantCategory')['IsFraud'].mean()

print("\nFraud Rate by Merchant Category:")
print(fraud_by_category)

# Customers with highest fraud activity
fraud_by_customer = transactions.groupby('CustomerID')['IsFraud'].sum()

print("\nTop Customers by Fraud Count:")
print(fraud_by_customer.sort_values(ascending=False).head(10))
