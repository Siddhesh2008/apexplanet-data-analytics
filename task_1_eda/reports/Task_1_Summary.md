# 📋 Task 1 Executive Summary: Exploratory Data Analysis & Data Hygiene
**ApexPlanet Data Analytics Internship**  
**Author:** Siddhesh (1st Year B.Tech in Artificial Intelligence & Data Science)  
**Dataset:** Global E-Commerce Transactions (50,000 Records, \$25.16M Gross Sales)  

---

## 1. Executive Overview

Task 1 establishes the foundational data hygiene, exploratory data analysis (EDA), and data profiling for the ApexPlanet Data Analytics portfolio. Utilizing Python, Pandas, and NumPy, the complete 50,000-row transaction log was ingested, audited for data integrity, parsed for temporal continuity, and profiled across all business dimensions.

```
================================================================================
                    KEY DATA HYGIENE CERTIFICATIONS
================================================================================
 Total Transactions Audited   : 50,000 records
 Missing / Null Values        : 0 (0.00% across all 8 features)
 Duplicate Transaction Rows   : 0 (0.00% duplicated records)
 Temporal Span Audited        : 730 Calendar Days (March 9, 2023 – March 8, 2025)
 Gross Sales Processed        : $25,157,989.23 USD
 Mean Order Value (AOV)       : $503.16 USD (Median: $503.11 USD)
 Standard Deviation (Spend)   : $286.56 USD
 Minimum / Maximum Spend      : $5.04 / $999.98 USD
================================================================================
```

---

## 2. Dataset Architecture & Schema Audit

The audited dataset comprises 8 core columns structured as follows:

| Column Name | Data Type | Non-Null Count | Unique Values | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Transaction_ID` | `int64` | 50,000 | 50,000 | Unique primary transaction identifier |
| `User_Name` | `object` | 50,000 | 100 | Distinct customer account label (averaging 500 orders each) |
| `Age` | `int64` | 50,000 | 53 | Customer age (ranging uniformly from 18 to 70 years) |
| `Country` | `object` | 50,000 | 10 | Customer country of origin across 10 international markets |
| `Product_Category` | `object` | 50,000 | 8 | Retail product category across 8 distinct business units |
| `Purchase_Amount` | `float64` | 50,000 | 38,719 | Total transaction purchase value in USD |
| `Payment_Method` | `object` | 50,000 | 6 | Settlement rail (Credit Card, Debit Card, PayPal, Cash on Delivery, UPI, Crypto) |
| `Transaction_Date` | `datetime64[ns]` | 50,000 | 730 | ISO-standard transaction calendar timestamp |

---

## 3. Core Exploratory Findings & Insights

### 3.1 Financial Distribution & Spend Behavior
- **Uniform Continuous Spend:** Transaction values span from \$5.04 to \$999.98, displaying near-perfect symmetric balance around the central mean (\$503.16) and median (\$503.11).
- **Kurtosis & Skewness:** Distribution shows minimal skewness (-0.008), indicating no severe upper-end outlier distortion or artificial retail price gating.

### 3.2 Product Category Parity
- Revenue is extraordinarily well-balanced across all 8 product departments, with variance between top and bottom categories under 4.5%:
  1. **Sports:** \$3,203,792.83 (12.73% | 6,366 orders)
  2. **Clothing:** \$3,190,483.56 (12.68% | 6,350 orders)
  3. **Books:** \$3,172,127.12 (12.61% | 6,290 orders)
  4. **Home & Kitchen:** \$3,161,248.91 (12.57% | 6,281 orders)
  5. **Toys:** \$3,141,894.40 (12.49% | 6,233 orders)
  6. **Electronics:** \$3,119,842.10 (12.40% | 6,211 orders)
  7. **Automotive:** \$3,109,249.88 (12.36% | 6,192 orders)
  8. **Beauty:** \$3,059,350.43 (12.16% | 6,077 orders)

### 3.3 International Market Balance
- Transactions span 10 global economies with steady ~\$2.5M revenue contribution per nation:
  - **France:** \$2,553,491.12 (5,081 orders) — Highest gross volume
  - **USA:** \$2,548,912.45 (4,994 orders) — Highest AOV (\$510.39)
  - **Germany:** \$2,532,180.20 (5,042 orders)
  - **UK:** \$2,525,419.87 (5,019 orders)
  - **Australia:** \$2,521,048.90 (5,023 orders)
  - **India:** \$2,514,892.30 (5,001 orders)
  - **Canada:** \$2,508,310.40 (4,989 orders)
  - **Japan:** \$2,498,720.15 (4,978 orders)
  - **Brazil:** \$2,482,912.60 (4,952 orders)
  - **Mexico:** \$2,472,101.24 (4,921 orders)

### 3.4 Payment Rail Dynamics
- **Cash on Delivery (\$4,279,812.15)** and **UPI (\$4,261,390.80)** represent the two leading settlement methods, showing equal viability between modern instant fintech rails and traditional cash-on-receipt fulfillment.

### 3.5 Demographic & Age Independence
- Customer age spans 18 to 70.
- **Correlation with Purchase Amount:** Pearson correlation coefficient is **r = -0.0036** ($p > 0.05$). Spending power is statistically independent of age.
- **Senior Spending Power:** Customers aged 56–70 generate **\$7.09M (28.2%)** of gross revenue, making older demographics a crucial segment.

---

## 4. Methodological Hygiene Checklist
- [x] Clean zero-null dataset verified
- [x] Complete primary key uniqueness (`Transaction_ID`) confirmed
- [x] Datetime column transformed to pandas native datetime object
- [x] Memory usage optimized through proper column typing
- [x] Reusable data validation pipeline established for downstream tasks
