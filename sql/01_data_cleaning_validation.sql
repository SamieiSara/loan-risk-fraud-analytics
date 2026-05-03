/* ============================================================
   DATA CLEANING & VALIDATION SCRIPT
   Loan Portfolio Risk & Fraud Analytics Project

   Description:
   This script performs data profiling, cleaning, and validation 
   on loan portfolio datasets including applications, customers, 
   and transactions.

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

-- Check duplicate applications
SELECT ApplicationID, COUNT(*) AS duplicate_count
FROM applications
GROUP BY ApplicationID
HAVING COUNT(*) > 1;


-- ============================================================
-- SECTION 3: DATA TYPE VALIDATION
-- ============================================================

-- Inspect sample date values
SELECT ApplicationDate
FROM applications
LIMIT 20;

-- Identify invalid date formats (SQLite)
SELECT ApplicationDate
FROM applications
WHERE date(ApplicationDate) IS NULL;


-- ============================================================
-- SECTION 4: BUSINESS RULE VALIDATION
-- ============================================================

-- Business Rule: Loan amount should not be negative
SELECT *
FROM applications
WHERE LoanAmount < 0;

-- Business Rule: Credit score should be within valid range (300–850)
SELECT *
FROM customers
WHERE CreditScore < 300 OR CreditScore > 850;

-- Business Rule: Debt-to-Income ratio should not be negative
SELECT *
FROM customers
WHERE DebtToIncomeRatio < 0;


-- ============================================================
-- SECTION 5: NULL HANDLING (FILTERING CLEAN DATA)
-- ============================================================

-- Retain only valid records for analysis
SELECT *
FROM customers
WHERE Income IS NOT NULL
  AND CreditScore IS NOT NULL;


-- ============================================================
-- SECTION 6: DATA STANDARDIZATION
-- ============================================================

-- Check inconsistent categorical values (e.g., Region)
SELECT DISTINCT Region
FROM customers;

-- Note: Standardization (e.g., casing, naming) would be applied 
-- during data transformation if inconsistencies are found.


-- ============================================================
-- SECTION 7: OUTLIER DETECTION
-- ============================================================

-- Detect unusually high loan amounts
SELECT *
FROM applications
WHERE LoanAmount > 1000000;

-- Detect unusually high transaction amounts
SELECT *
FROM transactions
WHERE Amount > 50000;


-- ============================================================
-- SECTION 8: FRAUD DATA VALIDATION
-- ============================================================

-- Validate fraud flags in transactions (should be 0 or 1)
SELECT *
FROM transactions
WHERE IsFraud NOT IN (0, 1);

-- Validate fraud flags in applications
SELECT *
FROM applications
WHERE IsFraudApp NOT IN (0, 1);


-- ============================================================
-- SECTION 9: REFERENTIAL INTEGRITY CHECKS
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
-- SECTION 10: CLEAN DATASET (OPTIONAL VIEW)
-- ============================================================

-- Create a cleaned customer dataset for downstream use
CREATE VIEW clean_customers AS
SELECT *
FROM customers
WHERE Income IS NOT NULL
  AND CreditScore BETWEEN 300 AND 850;
