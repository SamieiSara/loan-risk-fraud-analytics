/* ============================================================
   DATA CLEANING & VALIDATION SCRIPT| Tool: SQLite / DB Browser for SQLite
   Loan Portfolio Risk & Fraud Analytics Project

   Description:
   This script performs data profiling, cleaning, and validation  
   on loan portfolio datasets covering all 9  tables including applications,
   customers, transactions, credit_bureau, risk_labels, and more.
   
   The goal is to ensure data quality, consistency, and reliability 
   before downstream analysis in Python and Power BI.
   ============================================================ */


-- ============================================================
-- SECTION 1: DATA PROFILING
-- ============================================================

-- Check number of records in key tables
SELECT COUNT(*) AS total_applications FROM applications;
SELECT COUNT(*) AS total_customers FROM customers;
SELECT COUNT(*) AS total_transactions FROM transactions;


-- Check missing values in important financial fields
SELECT 
    COUNT(*) AS total_rows,
    COUNT(LoanAmount) AS non_null_loan_amount,
    COUNT(InterestRate) AS non_null_interest_rate
FROM applications;

SELECT 
    COUNT(*) AS total_rows,
    COUNT(Income) AS non_null_income,
    COUNT(CreditScore) AS non_null_credit_score
FROM customers;


-- ============================================================
-- SECTION 2: DUPLICATE DETECTION
-- ============================================================

-- Check duplicate customers
SELECT CustomerID, COUNT(*) AS duplicate_count
FROM customers
GROUP BY CustomerID
HAVING COUNT(*) > 1;

-- If duplicates are found, retain the most recent record per customer
-- ROW_NUMBER() assigns rank 1 to the latest record; we keep only rank = 1
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY CreatedDate DESC) AS row_num
    FROM customers
)
WHERE row_num = 1;

-- Check duplicate applications
SELECT ApplicationID, COUNT(*) AS duplicate_count
FROM applications
GROUP BY ApplicationID
HAVING COUNT(*) > 1;

-- Check duplicate transaction ID
SELECT TransactionID, COUNT(*) 
FROM transactions 
GROUP BY TransactionID 
HAVING COUNT(*) > 1;


-- ============================================================
-- SECTION 3: DATA TYPE VALIDATION
-- ============================================================

-- Inspect raw date format to confirm consistency before applying date() conversion
SELECT ApplicationDate
FROM applications
LIMIT 20;

-- Identify invalid date formats (SQLite)
SELECT ApplicationDate
FROM applications
WHERE date(ApplicationDate) IS NULL;

-- No numeric type checks for LoanAmount
SELECT LoanAmount 
FROM applications 
WHERE TYPEOF(LoanAmount) != 'real' AND TYPEOF(LoanAmount) != 'integer';


-- ============================================================
-- SECTION 4: BUSINESS RULE VALIDATION
-- ============================================================

-- Loan amounts must be non-negative
SELECT *
FROM applications
WHERE LoanAmount < 0;

-- Credit score should be within valid range (300–850)
SELECT *
FROM customers
WHERE CreditScore < 300 OR CreditScore > 850;

-- Debt-to-Income ratio must be non-negative OR DebtToIncomeRatio > 1 to flag unrealistic DTI values
SELECT *
FROM customers
WHERE DebtToIncomeRatio < 0
   OR DebtToIncomeRatio > 1;

-- InterestRate of 0% or above 50% would be a red flag
SELECT * 
FROM applications 
WHERE InterestRate <= 0 OR InterestRate > 50;


-- ============================================================
-- SECTION 5: NULL HANDLING (FILTERING CLEAN DATA)
-- ============================================================

-- NULL FILTERING PREVIEW
SELECT *
FROM customers
WHERE Income IS NOT NULL
  AND CreditScore IS NOT NULL;

-- Retain only valid application records
SELECT *
FROM applications
WHERE LoanAmount IS NOT NULL
  AND InterestRate IS NOT NULL
  AND ApplicationDate IS NOT NULL;

-- Retain only valid transaction records
SELECT *
FROM transactions
WHERE TransactionAmount IS NOT NULL
  AND IsFraud IS NOT NULL;

-- ============================================================
-- SECTION 6: DATA STANDARDIZATION
-- ============================================================

-- Check inconsistent categorical values (e.g., Region)
SELECT DISTINCT Region
FROM customers;

-- Note: Standardization (e.g., casing, naming) would be applied 
-- during data transformation if inconsistencies are found.

UPDATE customers 
SET Region = UPPER(TRIM(Region)) 
WHERE Region != UPPER(TRIM(Region))


-- ============================================================
-- SECTION 7: FRAUD DATA VALIDATION
-- ============================================================

-- Validate fraud flags in transactions (expected values = 0 or 1)
SELECT *
FROM transactions
WHERE IsFraud NOT IN (0, 1);

-- Validate fraud flags in applications
SELECT *
FROM applications
WHERE IsFraudApp NOT IN (0, 1);

-- Validate fraud flags in fraud indicators
SELECT * FROM fraud_indicators 
WHERE FraudReason IS NULL OR FraudReason = '';

-- ============================================================
-- SECTION 8: REFERENTIAL INTEGRITY CHECKS
-- ============================================================

-- Check for applications without valid customer records
SELECT *
FROM applications a
LEFT JOIN customers c 
    ON a.CustomerID = c.CustomerID
WHERE c.CustomerID IS NULL;

-- Check for transactions without valid customer records
SELECT *
FROM transactions t
LEFT JOIN customers c
    ON t.CustomerID = c.CustomerID
WHERE c.CustomerID IS NULL;


-- ============================================================
-- SECTION 9: DERIVED FIELDS (FEATURE ENGINEERING)
-- ============================================================

-- Create age groups for segmentation
SELECT 
    CustomerID,
    Age,
    CASE 
        WHEN Age < 25 THEN '<25'
        WHEN Age < 35 THEN '25–34'
        WHEN Age < 45 THEN '35–44'
        WHEN Age < 55 THEN '45–54'
        ELSE '55+'
    END AS Age_Range
FROM customers;


-- Create income buckets for analysis
SELECT 
    CustomerID,
    Income,
    CASE 
        WHEN Income < 40000 THEN '<40K'
        WHEN Income < 70000 THEN '40K–69K'
        WHEN Income < 100000 THEN '70K–99K'
        ELSE '100K+'
    END AS Income_Bucket
FROM customers;


-- CREDIT SCORE RANGE

SELECT 
    CustomerID,
    CreditScore,
    CASE 
        WHEN CreditScore < 580 THEN 'Poor'
        WHEN CreditScore < 670 THEN 'Fair'
        WHEN CreditScore < 740 THEN 'Good'
        WHEN CreditScore < 800 THEN 'Very Good'
        ELSE 'Excellent'
    END AS Credit_Score_Range
FROM customers;


-- RISK SCORE BAND
-- RiskProb is stored as decimal (0–1); equivalent to 0–100% risk range

SELECT 
    CustomerID,
    RiskProb,
    CASE 
        WHEN RiskProb <= 0.10 THEN 'Low (0–10%)'
        WHEN RiskProb <= 0.25 THEN 'Medium (11–25%)'
        WHEN RiskProb <= 0.50 THEN 'High (26–50%)'
        ELSE 'Very High (51–100%)'
    END AS Risk_Score_Band
FROM risk_labels;
