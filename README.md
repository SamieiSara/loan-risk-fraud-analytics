# 📊 Loan Portfolio Risk & Fraud Analytics Dashboard

## 🔍 Overview  
This project analyzes a financial institution’s loan portfolio to assess **credit risk, detect fraudulent activities, and provide executive-level insights**.  

The goal is to support better lending decisions by identifying high-risk customers, monitoring fraud patterns, and improving overall portfolio performance through data-driven insights.

---

## 🎯 Business Problem  
Financial institutions generate a significant portion of their revenue through lending. However, poor risk assessment can lead to **loan defaults and financial losses**, while undetected fraud can further impact profitability.
This project focuses on analyzing a loan portfolio to examine customer credit behavior, quantify risk levels, and uncover fraud patterns, providing a structured approach to monitoring portfolio health and supporting more accurate and consistent lending decisions.---

## 🧩 Dataset

The analysis is based on a structured, relational loan portfolio dataset capturing multiple aspects of the lending lifecycle, including applications, customer profiles, credit history, transactions, and risk assessments.

The dataset consists of the following key tables:

- **applications** → Loan application details, approval decisions, and fraud flags  
- **customers** → Demographic, financial, and credit-related attributes of borrowers  
- **credit_bureau** → Aggregated credit metrics such as debt, utilization, and account history  
- **credit_history** → Monthly credit score tracking for each customer  
- **transactions** → Customer transaction activity, including fraud indicators  
- **fraud_indicators** → Additional flags and reasons for suspicious transactions  
- **past_loans** → Historical loan performance, including balances and late payments  
- **risk_labels** → Risk scores, underwriting metrics, and default indicators  
- **branches** → Branch-level and geographic information  

These tables are connected through primary and foreign key relationships (e.g., CustomerID, ApplicationID), enabling integrated analysis across credit risk, fraud detection, and customer behavior. 

---

## ⚙️ Tools & Technologies  
- SQL → Data cleaning, validation, and preparation  
- Python (Pandas, NumPy, Matplotlib) → Exploratory data analysis & feature engineering  
- Power BI (DAX) → Data modeling, KPI calculations, and dashboard development  

---

## 🟦 Data Preparation (SQL)  
SQL was used to ensure data quality and reliability before analysis. Key steps included:
- Data profiling to assess completeness  
- Handling missing values  
- Removing duplicate records  
- Validating data types  
- Standardizing categorical variables  
- Applying business rule checks  
- Ensuring referential integrity  

---

## 🟨 Exploratory Data Analysis (Python)  
Python was used to explore the data and uncover patterns:
- Analyzed distributions of loan amounts, income, and credit scores  
- Detected outliers using statistical methods (IQR) and visualizations  
- Identified relationships between financial variables  
- Conducted fraud pattern analysis  

---

## 🟨 Exploratory Data Analysis (Python)  
Python was used to explore the data and uncover patterns prior to visualization:

- Analyzed distributions of loan amounts, income, and credit scores  
- Detected outliers using statistical methods (IQR) and visualizations  
- Identified relationships between key financial variables  
- Conducted initial fraud pattern analysis across transaction data  

---

## 🟩 Dashboard Development (Power BI)  

## 🧩 Data Model  

A relational data model was developed in Power BI to connect loan, customer, transaction, and risk datasets.

![Data Model](powerbi/screenshots/data_model.png)

### 1. Executive Summary  
- High-level overview of portfolio performance and key metrics 
  
### 2. Credit Risk Analysis  
- Risk distribution and default trends  across customers and loans  

### 3. Fraud Detection Insights  
- Fraud patterns across time, region, and customer types  

### 4. Customer Overview  
- Customer-level performance and behavior insights  

---

## 📸 Dashboard Preview  
*(Add screenshots here later)*  

---

## 💡 Key Insights  
- Lower credit scores and higher debt-to-income ratios increase default risk  
- Certain regions and segments show higher fraud activity  
- Income and credit behavior strongly impact loan performance  
