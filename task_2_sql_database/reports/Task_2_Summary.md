# 📋 Task 2 Executive Summary: SQL & Relational Database Analytics
**ApexPlanet Data Analytics Internship**  
**Author:** Siddhesh (1st Year B.Tech in Artificial Intelligence & Data Science)  
**Database Dialect:** PostgreSQL 15+ / SQLAlchemy / Python  
**Dataset:** 50,000 Ingested E-Commerce Records  

---

## 1. Executive Summary

Task 2 transitions the e-commerce transaction dataset from flat file storage into a relational PostgreSQL enterprise database architecture. Using **PostgreSQL**, **SQLAlchemy**, and **psycopg2**, a relational schema was modeled, indexed, and queried to solve critical business analytics questions regarding revenue concentration, payment method performance, and customer lifetime expenditure.

```
================================================================================
                    RELATIONAL DATABASE METRICS
================================================================================
 Target Database              : apexplanet_analytics
 Ingested Table Name          : public.ecommerce_transactions
 Rows Stored & Audited        : 50,000 records
 Query Engine Integration     : SQLAlchemy 2.x + psycopg2 Python Connector
 Primary Analytical Queries   : Aggregations, GROUP BY, HAVING, Window Functions
 Top Revenue Country          : France ($2,553,491.12 | 5,081 transactions)
 Top Product Category         : Sports ($3,203,792.83 | 6,366 transactions)
 Top Customer Account         : Sophia Harris ($296,354.98 | 568 transactions)
 Leading Settlement Rail      : Cash on Delivery ($4,279,812.15 | 8,485 transactions)
================================================================================
```

---

## 2. Relational Schema Architecture

The PostgreSQL table is defined with strict relational constraints:

```sql
CREATE TABLE IF NOT EXISTS public.ecommerce_transactions (
    transaction_id INT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18 AND age <= 100),
    country VARCHAR(100) NOT NULL,
    product_category VARCHAR(100) NOT NULL,
    purchase_amount NUMERIC(10, 2) NOT NULL CHECK (purchase_amount > 0),
    payment_method VARCHAR(50) NOT NULL,
    transaction_date TIMESTAMP WITHOUT TIME ZONE NOT NULL
);

-- Analytical B-Tree Indexes for Query Optimization
CREATE INDEX idx_country ON public.ecommerce_transactions(country);
CREATE INDEX idx_category ON public.ecommerce_transactions(product_category);
CREATE INDEX idx_date ON public.ecommerce_transactions(transaction_date);
CREATE INDEX idx_user ON public.ecommerce_transactions(user_name);
```

---

## 3. Core SQL Query Categories & Results

### 3.1 Financial Aggregations & Summary Benchmarks
- **Total Gross Revenue:** `SELECT SUM(purchase_amount) FROM public.ecommerce_transactions;`
  - **Result:** **\$25,157,989.23**
- **Average Transaction Value:** `SELECT AVG(purchase_amount) FROM public.ecommerce_transactions;`
  - **Result:** **\$503.16**

### 3.2 Product Category Performance Breakdown
```sql
SELECT
    product_category,
    COUNT(*) AS total_orders,
    ROUND(SUM(purchase_amount), 2) AS total_revenue,
    ROUND(AVG(purchase_amount), 2) AS avg_ticket_size
FROM public.ecommerce_transactions
GROUP BY product_category
ORDER BY total_revenue DESC;
```
- **Sports** leads overall sales at \$3.20M (6,366 orders), followed closely by **Clothing** (\$3.19M, 6,350 orders) and **Books** (\$3.17M, 6,290 orders).
- The spread between the top and bottom product category is exceptionally narrow (4.5%), indicating strong catalog diversification with no single point of inventory vulnerability.

### 3.3 International Geographic Breakdown
```sql
SELECT
    country,
    COUNT(*) AS total_transactions,
    ROUND(SUM(purchase_amount), 2) AS total_revenue,
    ROUND(AVG(purchase_amount), 2) AS avg_purchase_amount
FROM public.ecommerce_transactions
GROUP BY country
ORDER BY total_revenue DESC;
```
- All 10 international markets generate between **\$2.47M and \$2.55M**.
- **France** ranks #1 by volume with \$2.55M across 5,081 transactions.
- **USA** ranks #1 by average order value at **\$510.39** per transaction.

### 3.4 Customer Lifetime Expenditure & VIP Ranking (Window Functions)
```sql
SELECT
    user_name,
    COUNT(*) AS total_transactions,
    ROUND(SUM(purchase_amount), 2) AS total_spent,
    ROUND(AVG(purchase_amount), 2) AS avg_spend,
    ROW_NUMBER() OVER (ORDER BY SUM(purchase_amount) DESC) AS customer_rank
FROM public.ecommerce_transactions
GROUP BY user_name
ORDER BY total_spent DESC
LIMIT 10;
```
- **Top 3 Customer Accounts:**
  1. **Sophia Harris:** \$296,354.98 (568 transactions, AOV: \$521.75) — Rank 1
  2. **David Miller:** \$285,085.83 (553 transactions, AOV: \$515.53) — Rank 2
  3. **Michael Smith:** \$284,752.61 (551 transactions, AOV: \$516.79) — Rank 3

### 3.5 Temporal Monthly Velocity Analysis
```sql
SELECT
    DATE_TRUNC('month', transaction_date) AS sales_month,
    COUNT(*) AS monthly_orders,
    ROUND(SUM(purchase_amount), 2) AS monthly_revenue
FROM public.ecommerce_transactions
GROUP BY DATE_TRUNC('month', transaction_date)
ORDER BY sales_month ASC;
```
- Consistent revenue velocity ranging from **\$1.00M to \$1.11M** per calendar month.
- Peak monthly revenue occurred in **July 2023 (\$1,105,420.15)**.
- Peak transaction count occurred in **January 2024 (2,190 orders)**.

---

## 4. Key Database Insights & Recommendations
1. **Index Optimization:** B-Tree indexing on `country`, `product_category`, and `transaction_date` reduced query scan time by preventing sequential full-table scans.
2. **Schema Integrity:** Numeric precision `NUMERIC(10, 2)` prevented floating-point arithmetic rounding discrepancies in financial reporting.
3. **Data Access Layer:** The modular `db_utils.py` connection engine provides secure connection pooling and automatic cursor cleanup.
