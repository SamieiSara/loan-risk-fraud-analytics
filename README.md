#  Loan Portfolio Risk & Fraud Analytics

##  Overview  
This project analyzes a financial institution’s loan portfolio to assess **credit risk, detect fraudulent activities, and provide executive-level insights**.  
This dashboard enables lending teams to reduce defaults, flag fraud early, make risk-adjusted approval decisions, and improving overall portfolio performance.

---

## Business Problem  
Financial institutions generate a significant portion of their revenue through lending. However, poor risk assessment can lead to **loan defaults and financial losses**, while undetected fraud can further impact profitability.
This project analyzes customer credit behavior and fraud patterns. The output is a structured monitoring framework that supports consistent, data-driven lending decisions

## Dataset

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

##  Tools & Technologies  
- SQL → Data cleaning, validation, and preparation
- Python (Pandas, NumPy, Matplotlib) → Exploratory data analysis to identify distributions, outliers, and relationships before visualization
- Power BI (DAX) → Data modeling, KPI calculations, and dashboard development  

---

##  Data Preparation (SQL)  
SQL was used to ensure data quality and reliability before analysis. Key steps included:
- Data profiling to assess completeness  
- Handling missing values  
- Removing duplicate records  
- Validating data types  
- Standardizing categorical variables
- Creating derived fields such as income buckets, credit score ranges, and risk score bands to support segmentation and analysis
- Applying business rule checks  
- Ensuring referential integrity across tables
- Cleaned and prepared data across 9 related tables; created 6+ derived segmentation fields to support downstream analysis
  
---

##  Exploratory Data Analysis (Python)  
Python was used to explore the data and uncover patterns prior to dashboard development:
- Analyzed distributions of loan amounts, income, and credit scores
- Detected outliers using statistical methods (IQR) and visualizations
- Explored relationships between key financial variables (e.g., income, credit score, debt-to-income ratio)
- Performed initial fraud exploration by aggregating flagged transactions at the customer level to identify high-frequency fraud accounts, informing the segmentation approach used in the Power BI fraud detection analysis.

---

##  Dashboard Development (Power BI)

An interactive Power BI dashboard was developed to provide insights into portfolio performance, credit risk, fraud detection, and customer behavior.

The dashboard includes 4 pages: Executive Summary, Credit Risk Analysis, Fraud Detection, and Customer Behavior, with cross-filtering and drill-through enabled.

👉 Detailed dashboard structure, data model, and DAX measures are available in the Power BI section:
See `powerbi/README.md` 

---

##  Dashboard Preview  

![Executive Summary](powerbi/screenshots/Executive_Summary.png)

---

##  Key Insights & Recommendations  

- Customers in the **income $70K–$99K + 51–100% risk band** show the highest default rate (~75%), requiring immediate tightening of approval rules for this segment  

- Credit score alone is not reliable for certain professions — **Engineers with excellent credit scores still show elevated risk (~6% vs ~1–2%)**, requiring additional income and debt validation even at high credit levels  

- High-income borrowers are not always low-risk — **Doctors (100K+), Software Developers (100K+ and 70–99K), and Engineers (40–69K)** show elevated default rates, indicating the need for stricter approval criteria despite strong income  

- Fraud is strongly concentrated in specific loan purposes — **Debt Consolidation and Car Loans**, which should trigger additional verification steps such as supporting documentation or secondary identity checks  

- The **10K–50K loan range** is the most targeted by fraud, requiring enhanced verification at the **Pending stage**, the final decision point before approval  

- Fraud behavior differs by customer tier and transaction channel:
  - **Prime customers → ATM transactions**
  - **Subprime customers → Transfer transactions**
  - **Near-prime → both channels**
  → Requires tier-specific fraud controls instead of uniform rules  

- Regional risk patterns vary significantly:
  - **Penticton and White Rock → low volume but extremely high risk severity** (require early detection logic)
  - **Vancouver and Surrey → high fraud volume + customer growth** (require stricter controls without slowing growth)

- Highest default risk is concentrated among:
  - **Basic customer class**
  - **Widowed customers on work permits**
  - **Customers under 25 with poor credit scores**
  → These groups require closer monitoring and stricter approval review  

- Portfolio baseline default rate is **8%**, with **Subprime customers (51–100% risk band)** requiring the closest ongoing monitoring, followed by Near-prime segments

👉 Full detailed recommendations:  
See `business_recommendations.md`
