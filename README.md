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

An interactive Power BI dashboard was developed to provide insights into portfolio performance, credit risk, fraud detection, and customer behavior.

The dashboard enables stakeholders to monitor key metrics, identify high-risk segments, and explore trends across the lending lifecycle.

👉 Detailed dashboard structure, data model, and DAX measures are available in the Power BI section:
See `powerbi/README.md` 

---

## 📸 Dashboard Preview  

![Executive Summary](powerbi/screenshots/Executive_Summary.png)

---

## 💡 Key Insights & Recommendations  

The analysis identified several high-impact opportunities to improve lending decisions, reduce default risk, and strengthen fraud detection:

- Customers in the **income $70K–$99K + 51–100% risk band** show the highest default rate (~75%), requiring stricter approval controls  
- Credit score alone is not always reliable — certain professions (e.g., Engineers) show elevated risk despite strong credit profiles  
- High-income segments (e.g., Doctors, Software Developers) still exhibit unexpected default patterns, highlighting the need for deeper income and debt validation  
- Fraud activity is concentrated in **specific loan purposes (Debt Consolidation, Car Loans)** and **mid-range loan sizes (10K–50K)**  
- Fraud behavior varies by customer tier and transaction channel, requiring **targeted, segment-specific controls** rather than uniform rules  
- Certain regions show **low volume but high severity risk**, while others combine **high fraud activity with rapid customer growth**, requiring different monitoring strategies  
- Customer segments such as **Basic class, younger borrowers, and specific demographic groups** show higher default rates and should be monitored more closely  

👉 Full detailed recommendations:  
See `business_recommendations.md`
