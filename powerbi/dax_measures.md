# 📊 Power BI DAX Measures
Loan Risk & Fraud Analytics Project

This document contains key DAX measures used to build KPIs across Executive Summary, Credit Risk, Fraud Detection, and Customer Overview dashboards.

---

## 🟦 EXECUTIVE SUMMARY

### Total Loan Applications
```DAX
Total Loan Applications = COUNTROWS(applications)
````

### Approval Rate (%)

Approval Rate = 
DIVIDE(
    SUM(applications[Approved]),
    COUNTROWS(applications)
)

### Total Loan Amount

Total Loan Amount = SUM(applications[LoanAmount])


### Average Loan per Customer

Avg Loan per Customer =
DIVIDE(
    SUM(applications[LoanAmount]),
    DISTINCTCOUNT(customers[CustomerID])
)

---

## 🟥 CREDIT RISK ANALYSIS

### Average Risk Score


Avg Risk Score = AVERAGE(risk_labels[RiskProb])


### High-Risk Customers (%)

High Risk % =
DIVIDE(
    COUNTROWS(FILTER(risk_labels, risk_labels[RiskProb] > 0.7)),
    COUNTROWS(risk_labels)
)


### Default Rate (%)

Default Rate =
DIVIDE(
    COUNTROWS(FILTER(risk_labels, risk_labels[HasDefaultedBefore] = 1)),
    COUNTROWS(risk_labels)
)

### Defaulted Loan Value

Defaulted Loan Value =
CALCULATE(
    SUM(applications[LoanAmount]),
    risk_labels[HasDefaultedBefore] = 1
)


---

## 🟨 FRAUD DETECTION

### Total Transactions

Total Transactions = COUNTROWS(transactions)


### Fraudulent Transactions


Fraud Transactions = SUM(transactions[IsFraud])


### Fraud Rate (%)

Fraud Rate =
DIVIDE(
    SUM(transactions[IsFraud]),
    COUNTROWS(transactions)
)


### Total Fraud Amount

Fraud Amount =
CALCULATE(
    SUM(transactions[Amount]),
    transactions[IsFraud] = 1
)



## 🟪 CUSTOMER OVERVIEW

### Total Customers


Total Customers = DISTINCTCOUNT(customers[CustomerID])


### Average Credit Score


Avg Credit Score = AVERAGE(customers[CreditScore])


### Customer Default Rate

Customer Default Rate =
DIVIDE(
    COUNTROWS(FILTER(customers, customers[HasDefaultedBefore] = 1)),
    COUNTROWS(customers)
)
