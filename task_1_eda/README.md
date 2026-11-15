# 🔍 Task 1: Exploratory Data Analysis & Data Hygiene — E-Commerce Transactions

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243.svg)](https://numpy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab%20%2F%20Notebook-orange.svg)](https://jupyter.org/)
[![Internship](https://img.shields.io/badge/Internship-ApexPlanet%20Solutions-orange.svg)](#-internship-context)

Master repository module for **Task 1: Exploratory Data Analysis (EDA) and Data Hygiene Auditing** of the **ApexPlanet Data Analytics Internship**.

---

## 📌 Internship Context
- **Organization:** **ApexPlanet Solutions**
- **Internship Role:** Data Analytics Intern
- **Project Scope:** **Task 1: Data Cleaning, Hygiene Auditing & Exploratory Analysis (Days 1–7)**
- **Author:** Siddhesh (1st Year B.Tech in Artificial Intelligence & Data Science)
- **Dataset:** 50,000 Global E-Commerce Transactions (\$25.16M Gross Sales)

---

## 🎯 Task 1 Objectives
1. **Dataset Ingestion & Schema Audit:** Ingest raw CSV logs, inspect structural integrity, verify data types, and check shape.
2. **Data Hygiene Certification:** Conduct exhaustive checks for missing values (nulls/NaNs), blank strings, and duplicate transaction rows.
3. **Temporal Standardization:** Parse datetime strings into ISO-standard datetime timestamps and analyze temporal boundaries.
4. **Univariate & Bivariate Distribution Analysis:** Analyze summary statistics (Mean, Median, Standard Deviation, IQR, Min/Max) for transaction spend and evaluate categorical cardinality across countries, categories, and payment rails.
5. **Demographic Profiling:** Examine customer age distributions and test linear correlation against purchase amounts.
6. **Cross-Tabulation Analysis:** Compute pivot matrices mapping geographical revenue contributions across retail categories.

---

## 📁 Repository & Folder Structure

```text
task_1_eda/
├── data/
│   └── ecommerce_transactions.csv                      # Raw source dataset (50,000 records x 8 columns)
├── notebooks/
│   ├── Task_1_Exploratory_Data_Analysis.ipynb          # Master executed EDA Jupyter Notebook
│   ├── Ecommerce.ipynb                                 # Original exploration notebook
│   └── 01_data_cleaning_eda.ipynb                      # Environment verification & smoke test
├── reports/
│   └── Task_1_Summary.md                               # Executive EDA Summary & Data Hygiene Report
├── requirements.txt                                    # Environment dependencies
└── README.md                                           # Comprehensive documentation & Viva Voce defense guide
```

---

## 🔬 Dataset Schema & Attributes

| Attribute Name | Data Type | Non-Null | Cardinality | Semantic Description |
| :--- | :--- | :--- | :--- | :--- |
| `Transaction_ID` | `int64` | 50,000 | 50,000 | Unique primary transaction key |
| `User_Name` | `object` | 50,000 | 100 | Customer account identifier (averaging 500 orders each) |
| `Age` | `int64` | 50,000 | 53 | Customer age (18 to 70 years) |
| `Country` | `object` | 50,000 | 10 | Customer country of residence |
| `Product_Category` | `object` | 50,000 | 8 | Retail product department |
| `Purchase_Amount` | `float64` | 50,000 | 38,719 | Total transaction gross sales in USD |
| `Payment_Method` | `object` | 50,000 | 6 | Payment gateway / settlement rail |
| `Transaction_Date` | `datetime64[ns]` | 50,000 | 730 | ISO transaction calendar timestamp |

---

## 📊 Summary of Findings & Analytical Milestones

- **Data Integrity:** **0 missing values (0.00%)** and **0 duplicate records (0.00%)**.
- **Financial Baseline:** Total gross sales of **\$25,157,989.23** with an Average Order Value (AOV) of **\$503.16** and median of **\$503.11**.
- **Product Portfolio Balance:** All 8 product departments account for 12.16% to 12.73% of gross sales, led by **Sports (\$3.20M)** and anchored by **Beauty (\$3.06M)**.
- **Geographic Parity:** 10 international markets contribute evenly (~\$2.5M each); France leads gross volume (\$2.55M) while the USA drives top AOV (\$510.39).
- **Payment Method Adoption:** Cash on Delivery (\$4.28M) and UPI (\$4.26M) are the top two payment rails.
- **Age-Spend Independence:** Pearson correlation coefficient $r = -0.0036$, demonstrating price sensitivity is uniform across age groups.

---

## ⚙️ How to Run

1. **Activate Environment & Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch JupyterLab:**
   ```bash
   jupyter lab notebooks/Task_1_Exploratory_Data_Analysis.ipynb
   ```

---

## 🎓 Viva Voce Technical Defense Guide (15+ Q&A)

### Q1: What is the primary difference between `df.info()` and `df.describe()`?
**Answer:** `df.info()` provides high-level structural metadata: memory usage, data types (`dtypes`), total entries, and non-null counts per column. `df.describe()` generates descriptive summary statistics for numerical columns (count, mean, std, min, 25%, 50%, 75%, max) and categorical frequency counts when `include='all'` is specified.

### Q2: Why is checking for duplicates essential before calculating business KPIs?
**Answer:** Duplicate transaction rows artificially inflate financial metrics such as Total Gross Sales, Order Count, and Customer Lifetime Value (CLV). Deduplication guarantees accurate accounting and prevents bias in downstream predictive models.

### Q3: How did you verify missing values, and how would you handle them if present?
**Answer:** We executed `df.isnull().sum()`, which returned 0 across all 8 features. If null values existed, strategies would include:
1. Numerical imputation via median (robust against outliers) or mean.
2. Mode imputation for categorical attributes.
3. Algorithmic imputation (KNN / Iterative Imputer) or record omission if missingness is completely at random and represents <1% of data.

### Q4: What does a near-zero Pearson correlation between Age and Purchase Amount ($r = -0.0036$) signify?
**Answer:** It demonstrates that customer age has no linear association with transaction amount. Younger customers (e.g. 18–25) and senior customers (56–70) spend across the entire price spectrum (\$5 to \$1,000) at similar frequencies.

### Q5: Why is `Transaction_Date` parsed into a datetime object rather than kept as a string?
**Answer:** String timestamps prevent chronological arithmetic and temporal feature engineering. Converting to `pd.to_datetime` enables temporal operations: `.dt.year`, `.dt.month`, `.dt.day_name()`, time-series resampling (`df.resample('M')`), and date range slicing.

### Q6: What is the difference between Mean and Median, and what does their near-equality indicate here?
**Answer:** The mean is the arithmetic average (sensitive to extreme outliers), while the median is the 50th percentile rank value (robust against outliers). Here, Mean = \$503.16 and Median = \$503.11, indicating a highly symmetric, non-skewed distribution.

### Q7: Why is `User_Name` cardinality (100) significant given 50,000 records?
**Answer:** Each customer account appears an average of 500 times over the 24-month horizon. This provides high-frequency longitudinal order behavior ideal for cohort analysis, loyalty tracking, and customer segmentation.

### Q8: What is the difference between univariate, bivariate, and multivariate analysis?
**Answer:**
- **Univariate:** Analyzing single variables in isolation (e.g. histogram of `Purchase_Amount`, value counts of `Country`).
- **Bivariate:** Analyzing relationships between pairs of variables (e.g. `Purchase_Amount` vs `Age`, `Purchase_Amount` by `Payment_Method`).
- **Multivariate:** Analyzing interactions across three or more variables simultaneously (e.g. pivot matrix of Country × Product Category × Revenue).

### Q9: How do you detect outliers in numerical transaction data?
**Answer:** Using the Interquartile Range (IQR) rule ($Q_1 - 1.5 \times \text{IQR}$ to $Q_3 + 1.5 \times \text{IQR}$) or Z-score thresholding ($|z| > 3$). In this dataset, values span smoothly between \$5.04 and \$999.98 without isolated anomalies.

### Q10: What is cross-tabulation in Pandas?
**Answer:** `pd.crosstab()` or `pd.pivot_table()` computes aggregate summary metrics across two categorical variables simultaneously, producing a 2D contingency or revenue matrix (e.g., Country by Product Category).

---

## 👤 Author
- **Intern:** Siddhesh
- **Role:** Data Analytics Intern, ApexPlanet Solutions
- **Academic Discipline:** B.Tech in Artificial Intelligence & Data Science
