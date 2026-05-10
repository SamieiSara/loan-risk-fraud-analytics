# 📊 Loan Portfolio Risk & Fraud Analytics Dashboard

## 🔍 Overview  
This project analyzes a financial institution’s loan portfolio to assess **credit risk, detect fraudulent activities, and provide executive-level insights**.  

The goal is to support better lending decisions by identifying high-risk customers, monitoring fraud patterns, and improving overall portfolio performance through data-driven insights.

---

## 🎯 Business Problem  
Financial institutions generate a significant portion of their revenue through lending. However, poor risk assessment can lead to **loan defaults and financial losses**, while undetected fraud can further impact profitability.
This project leverages data analytics to examine customer credit behavior, quantify risk levels, and uncover fraud patterns, providing a structured approach to monitoring portfolio health and supporting more accurate and consistent lending decisions.
---

## 🧩 Dataset  
The dataset includes multiple interconnected tables representing:
- Loan applications  
- Customer demographics and financial profiles  
- Credit bureau data  
- Transaction history  
- Risk assessment scores  

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

## 🧠 Feature Engineering  
- Risk bands (Low, Medium, High)  
- Income segments  
- Customer segmentation (Basic, Advance, Premium)  
- Aggregated fraud indicators  

---

## 🟩 Dashboard Development (Power BI)  

## 🧩 Data Model  

A relational data model was developed in Power BI to connect loan, customer, transaction, and risk datasets.

![Data Model](powerbi/screenshots/data_model.png)

### 1. Executive Summary  
- Portfolio-level KPIs (approval rate, default rate, fraud rate)

### 2. Credit Risk Analysis  
- Risk distribution and default trends  

### 3. Fraud Detection Insights  
- Fraud patterns across time, region, and customer types  

### 4. Customer Overview  
- Customer-level performance and behavior insights  

---

## 📊 Key KPIs  
- Approval Rate  
- Default Rate  
- Fraud Rate  
- Average Loan per Customer  
- Risk Score Distribution  
- Total Loan Amount  

---

## 📸 Dashboard Preview  
*(Add screenshots here later)*  

---

## 💡 Key Insights  
- Lower credit scores and higher debt-to-income ratios increase default risk  
- Certain regions and segments show higher fraud activity  
- Income and credit behavior strongly impact loan performance  
