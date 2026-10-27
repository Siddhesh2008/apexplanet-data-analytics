# 🛒 E-Commerce Transactions — Exploratory Data Analysis (EDA)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.x-013243.svg)](https://numpy.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-blueviolet.svg)](https://seaborn.pydata.org/)
[![ApexPlanet](https://img.shields.io/badge/Internship-ApexPlanet%20Solutions-orange.svg)](#-internship-context)

An end-to-end exploratory data analysis project analyzing **50,000 global e-commerce transactions** across multiple product categories, geographic regions, payment gateways, and customer demographic segments.

---

## 📌 Internship Context

This project was developed as part of the **Data Analytics Internship** at **ApexPlanet Solutions**. The objective is to apply industry-standard analytical workflows, rigorous data cleaning, descriptive statistics, customer segmentation, and visual storytelling to uncover actionable commercial insights from raw transaction records.

---

## 📊 Project Overview & Objectives

E-commerce businesses operate in fast-moving, multi-currency, and geographically diverse environments. Understanding consumer behavior, sales drivers, and regional trends is vital for inventory forecasting, customer retention, and targeted marketing campaigns.

### Key Objectives:
- **Data Audit & Integrity:** Verify data completeness, detect anomalies, check missingness, and ensure type consistency.
- **Univariate & Bivariate Exploration:** Analyze distributions of transaction amounts, category frequencies, payment preferences, and regional order volume.
- **Financial & Category Breakdown:** Evaluate total gross revenue and average transaction value (AOV) across product lines.
- **Geographic Spend Analysis:** Identify top revenue-generating markets and assess regional purchasing power parity.
- **Temporal & Trend Analysis:** Map sales trajectories over a 2-year horizon (2023–2025) to identify seasonal shifts.
- **Customer Segmentation & Repeat Behavior:** Segment users by age cohorts, assess customer retention patterns, and profile high-value consumers.
- **Cross-Tabulation Matrix:** Construct multidimensional pivot views comparing countries against product categories.

---

## 🗂️ Repository Structure

```text
apexplanet-data-analytics/
├── notebooks/
│   ├── Ecommerce.ipynb               # Primary EDA and visualization notebook
│   └── ecommerce_transactions.csv    # Source transactions dataset (50,000 rows)
├── dashboards/                       # Future BI dashboard assets (Power BI / Tableau)
├── data/                             # Data storage (raw, processed, staging)
├── reports/                          # Generated analytical reports & documentation
├── scripts/                          # Reusable data pipeline & helper scripts
└── README.md                         # Project documentation and summary
```

---

## 📁 Dataset Description

The dataset covers **50,000 customer transactions** recorded between **March 9, 2023** and **March 8, 2025** (a 24-month continuous window).

### Data Schema

| Column Name | Data Type | Non-Null Count | Description |
| :--- | :--- | :--- | :--- |
| `Transaction_ID` | `int64` | 50,000 | Unique numeric identifier for each transaction |
| `User_Name` | `object` | 50,000 | Customer identifier / full name |
| `Age` | `int64` | 50,000 | Age of the customer (ranging from 18 to 70) |
| `Country` | `object` | 50,000 | Country where the purchase originated (10 countries) |
| `Product_Category`| `object` | 50,000 | Category of item purchased (8 distinct categories) |
| `Purchase_Amount` | `float64` | 50,000 | Transaction value in USD ($5.04 – $999.98) |
| `Payment_Method`  | `object` | 50,000 | Payment channel utilized (6 payment types) |
| `Transaction_Date`| `datetime64[ns]`| 50,000 | Timestamp of transaction (parsed from raw string) |

### Key Summary Statistics

- **Total Records:** 50,000 transactions
- **Total Gross Revenue:** \$25,157,989.23 (~**\$25.16 Million USD**)
- **Average Transaction Value (AOV):** \$503.16 (Median: \$503.11, Std Dev: \$286.56)
- **Customer Age:** Mean: 43.97 years | Range: 18 – 70 years
- **Missing Values / Duplicates:** 0 null values, 0 duplicate rows detected

---

## 🔍 Key Findings & Analysis Summary

### 1. Data Cleaning & Integrity Check
- **Zero Missing / Duplicated Data:** The dataset exhibits complete data hygiene with 0 null values across all 8 fields and 0 duplicate transaction rows.
- **Datetime Parsing:** `Transaction_Date` converted smoothly to standard `datetime64[ns]` without unparseable (NaT) entries.

### 2. Product Category Performance
All 8 product categories generated steady transaction volume and revenue, with individual category revenues ranging between \$3.05M and \$3.20M:

| Product Category | Total Revenue (USD) | Order Count | Performance Highlight |
| :--- | :---: | :---: | :--- |
| **Sports** | \$3,195,335.90 | 6,346 | Top revenue-generating category |
| **Toys** | \$3,185,652.36 | 6,331 | Strong year-round gift & hobby demand |
| **Books** | \$3,181,897.30 | 6,321 | Consistent high-frequency orders |
| **Clothing** | \$3,171,225.96 | 6,303 | Core lifestyle category |
| **Electronics** | \$3,133,965.04 | 6,228 | High-demand tech goods |
| **Grocery** | \$3,123,579.52 | 6,208 | Steady non-discretionary volume |
| **Home & Kitchen**| \$3,108,945.78 | 6,179 | Regular household basket sizes |
| **Beauty** | \$3,057,387.79 | 6,084 | Stable personal care segment |

### 3. Geographic Distribution
The user base spans 10 countries with balanced geographic performance (~5,000 transactions per market):

- **Top Grossing Markets:**
  - 🇫🇷 **France:** \$2,545,739.19 (Avg: \$509.86)
  - 🇨🇦 **Canada:** \$2,544,335.12 (Avg: \$500.66)
  - 🇺🇸 **USA:** \$2,541,220.22 (Avg: \$510.39 — highest average ticket size)
  - 🇲🇽 **Mexico:** \$2,534,475.67 (Avg: \$500.98)
  - 🇦🇺 **Australia:** \$2,514,911.65 (Avg: \$504.50)
  - 🇧🇷 **Brazil:** \$2,507,287.54 (Avg: \$506.73)
  - 🇮🇳 **India:** \$2,503,542.71 (Avg: \$501.11)
  - 🇩🇪 **Germany:** \$2,502,442.20 (Avg: \$495.83)
  - 🇯🇵 **Japan:** \$2,492,312.20 (Avg: \$502.48)
  - 🇬🇧 **UK:** \$2,471,723.15 (Avg: \$499.24)

### 4. Payment Method Preferences
Adoption is distributed evenly across 6 payment methods:
- **Cash on Delivery (COD):** \$4,276,269.38 (8,434 transactions, Avg: \$507.03) — highest total spend
- **UPI:** \$4,259,355.65 (8,477 transactions, Avg: \$502.46)
- **Debit Card:** \$4,234,776.21 (8,355 transactions, Avg: \$506.86)
- **PayPal:** \$4,173,529.85 (8,250 transactions, Avg: \$505.88)
- **Credit Card:** \$4,150,547.15 (8,310 transactions, Avg: \$499.46)
- **Net Banking:** \$4,063,511.41 (8,174 transactions, Avg: \$497.13)

### 5. Temporal Trends & Seasonality
- **Monthly Revenue Run-Rate:** Average monthly revenue consistently tracks between **\$1.0M and \$1.1M** across all full 24 months.
- **Top Revenue Month:** **July 2023** recorded the peak monthly gross revenue of **\$1,105,402.88** (2,154 orders).
- **Top Volume Month:** **January 2024** achieved the highest monthly transaction count with **2,190 orders** (\$1,101,023.49).
- *Note:* March 2025 contains partial-month data (up to March 8) with 538 orders and \$273,128.67.

### 6. Customer Demographics (Age Group Cohorts)
Segmenting customer ages into five standard analytical bins:

| Age Group | Order Count | Total Revenue (USD) | Average Order Value | Share of Volume |
| :---: | :---: | :---: | :---: | :---: |
| **18–25** | 7,443 | \$3,759,841.83 | \$505.15 | 14.9% |
| **26–35** | 9,513 | \$4,781,196.28 | \$502.60 | 19.0% |
| **36–45** | 9,628 | \$4,863,329.78 | \$505.12 | 19.3% |
| **46–55** | 9,303 | \$4,658,823.09 | \$500.79 | 18.6% |
| **56–70** | 14,113 | \$7,094,798.67 | \$502.71 | **28.2%** |

*Key Insight:* The **56–70 demographic** is the largest revenue contributor (\$7.09M), driven by higher order frequency, while average ticket size remains remarkably stable (~$500–$505) across all life stages.

### 7. Customer Loyalty & Repeat Purchasing
- **High Lifetime Frequency:** The dataset represents an established repeat-customer pool consisting of **100 unique customer profiles**, each averaging **500 transactions** (ranging between 435 and 568 purchases).
- **Top Spend Champions:**
  1. **Sophia Harris:** 568 transactions | \$296,354.98 total spend (\$521.75 AOV)
  2. **James Allen:** 545 transactions | \$278,079.15 total spend (\$510.24 AOV)
  3. **Olivia Hall:** 534 transactions | \$277,302.09 total spend (\$519.29 AOV)
  4. **Isabella Hall:** 539 transactions | \$275,798.04 total spend (\$511.68 AOV)
  5. **Noah Anderson:** 545 transactions | \$274,347.15 total spend (\$503.39 AOV)

---

## 💡 Business Recommendations

1. **VIP Loyalty & Retention Tiering:** Top spenders (e.g., customers spending >\$270,000) should be enrolled into an exclusive VIP loyalty program featuring dedicated support, priority fulfillment, and custom bundled rewards to maximize customer lifetime value (CLV).
2. **Targeted Campaigns for Senior Demographics:** Customers aged 56–70 drive over 28% of total gross revenue. Tailoring UI accessibility, specialized recommendations, and home/leisure product promotions towards this segment can yield high conversion.
3. **Checkout Optimization for Local Payment Rails:** Cash on Delivery, UPI, and debit cards account for the largest shares. Continuing to streamline one-click checkout and UPI deep-linking will minimize friction and cart abandonment.
4. **Category Cross-Selling Strategies:** Given balanced cross-border demand across all 8 product categories, implementing AI-driven cross-selling algorithms (e.g., pairing Sports gear with Electronics or Home & Kitchen with Groceries) will help lift basket sizes beyond the \$503 baseline.

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python 3.10+
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/) (DataFrames, GroupBy, Pivot Tables, Datetime operations), [NumPy](https://numpy.org/)
- **Data Visualization:** [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Development Environment:** Jupyter Notebook / VS Code

---

## 🚀 Getting Started & Reproduction

### Prerequisites
Make sure you have Python 3.10+ installed.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/apexplanet-data-analytics.git
cd apexplanet-data-analytics
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Launch the Analysis Notebook
```bash
jupyter notebook notebooks/Ecommerce.ipynb
```

---

## 👤 Author & Acknowledgments

- **Intern:** Siddhesh
- **Role:** Data Analytics Intern
- **Organization:** [ApexPlanet Solutions](https://apexplanetsolutions.com/)
- **Project:** Day 1 — Exploratory Data Analysis on E-Commerce Transactions
