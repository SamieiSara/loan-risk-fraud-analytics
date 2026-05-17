# 🧮 DAX Measures

The following measures were developed to support KPI calculations across portfolio performance, credit risk analysis, fraud detection, and customer insights.

Measures are grouped based on their primary use in the dashboard. Some are reused across multiple views but are defined once for clarity.

---

## 🟩 Executive Summary (Core Portfolio KPIs)

### Total Loan Applications

```DAX
Total Loan Applications Number = COUNT(applications[ApplicationID])
```

### Total Loans Approved

```DAX
Total Loans Approved Number =
CALCULATE(
    COUNTROWS(Applications),
    Applications[Approved] = TRUE()
)
```

### Approval Rate (%)

```DAX
Approval Rate (%) =
DIVIDE(
    [Total Loans Approved Number],
    [Total Loan Applications Number],
    0
)
```

### Total Loan Amount Approved

```DAX
Total Loan Amount Approved =
CALCULATE(
    SUM(Applications[LoanAmount]),
    Applications[Approved] = TRUE()
)
```

### Average Loan per Customer

```DAX
Average Loan per Customer =
DIVIDE(
    SUM(Applications[LoanAmount]),
    DISTINCTCOUNT(Applications[CustomerID]),
    0
)
```

### Average Credit Score

```DAX
Average Credit Score =
AVERAGE(DimCustomers[CreditScore])
```

---

## ⚠️ Credit Risk Analysis

### Defaulted Loans Number

```DAX
Defaulted Loans Number =
CALCULATE(
    COUNTROWS(Applications),
    Applications[Approved] = TRUE(),
    Applications[Status] = "Default"
)
```

### Default Rate (%)

```DAX
Defaulted Loans Rate % =
DIVIDE(
    [Defaulted Loans Number],
    [Total Loans Approved Number]
)
```

### Defaulted Loan Value

```DAX
Defaulted Loan Value =
CALCULATE(
    SUM(Applications[LoanAmount]),
    Applications[Approved] = TRUE(),
    Applications[Status] = "Default"
)
```

### High-Risk Customers (%)

```DAX
High-Risk Customers % =
DIVIDE(
    [High-Risk Customers],
    [Total Customers],
    0
)
```

### Average Risk Score

```DAX
Average Risk Score =
AVERAGE(Risk_Labels[RiskProb])
```

---

## 🛑 Fraud Detection Insights

### Total Transactions

```DAX
Total Transactions Number =
COUNT(Transactions[TransactionID])
```

### Fraudulent Transactions

```DAX
Fraudulent Transactions Number =
CALCULATE(
    COUNT(Transactions[TransactionID]),
    Transactions[IsFraud] = TRUE()
)
```

### Fraud Transaction Rate (%)

```DAX
Fraud Trns Rate % =
DIVIDE(
    [Fraudulent Transactions Number],
    [Total Transactions Number],
    0
)
```

### Fraud Loan Applications

```DAX
Fraudulent Loan Application Number =
CALCULATE(
    COUNT(Applications[ApplicationID]),
    Applications[IsFraudApp] = TRUE()
)
```

### Fraud Loan Rate (%)

```DAX
Fraud Loan Rate % =
DIVIDE(
    [Fraudulent Loan Application Number],
    [Total Loan Applications Number],
    0
)
```

---

## 👤 Customer Overview

### Total Customers

```DAX
Total Customers =
DISTINCTCOUNT(DimCustomers[CustomerID])
```

### Active Customers

```DAX
Active Customers =
CALCULATE(
    DISTINCTCOUNT(Applications[CustomerID]),
    Applications[Status] = "Active"
)
```

### New Customers (Last 30 Days)

```DAX
New Customers (Last 30 Days) =
VAR MaxDate =
CALCULATE(MAX(Applications[ApplicationDate]), ALL(Applications))
RETURN
CALCULATE(
    DISTINCTCOUNT(Applications[CustomerID]),
    FILTER(
        Applications,
        Applications[ApplicationDate] >= MaxDate - 30
    )
)
```

### Customer Default Rate (%)

```DAX
Customer Default Rate =
DIVIDE(
    CALCULATE(
        DISTINCTCOUNT(DimCustomers[CustomerID]),
        DimCustomers[HasDefaultedBefore] = 1
    ),
    DISTINCTCOUNT(DimCustomers[CustomerID]),
    0
)
```

