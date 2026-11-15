# 📑 Task 3 Summary Report: Data Visualization & Dashboarding
**Project Title:** E-Commerce Sales Performance & Customer Behavior Analysis  
**Internship Program:** ApexPlanet Data Analytics Internship — Roadmap Task 3 (Days 14–20)  
**Author:** Siddhesh (1st Year B.Tech Artificial Intelligence and Data Science)  
**Date:** November 2026  
**Status:** Completed & Ready for Review  

---

## Executive Summary
As part of **Task 3 (Data Visualization & Dashboarding)** of the **ApexPlanet Data Analytics Internship**, this report synthesizes the end-to-end analytical pipeline developed to analyze **50,000 e-commerce transactions** totaling **$25,157,989.23 (~$25.16 Million USD)** in gross sales recorded between **March 9, 2023** and **March 8, 2025**.

The analytical suite integrates three complementary layers:
1. **Procedural Static Visualization (Matplotlib):** Line charts, bar charts, histograms with KDE, and scatter plots with linear trendlines.
2. **Statistical Visual Modeling (Seaborn):** Correlation heatmaps, multi-dimensional pairplots, and letter-value boxen plots.
3. **Interactive Business Intelligence (Plotly & Power BI):** Dual-axis interactive time series, responsive category and country choropleths, a centralized DAX measure library, and an interactive executive dashboard with dynamic slicer cross-filtering.

---

## 🗂️ Data Hygiene & Integrity Audit

Prior to any visualization or statistical computation, the raw transactional dataset was audited for quality, consistency, and structural integrity:

| Metric | Empirical Result | Analytical Assessment |
| :--- | :--- | :--- |
| **Total Record Count** | 50,000 rows | Complete transactional dataset, no truncated observations |
| **Feature Dimensions** | 8 attributes | 1 numerical ID, 1 target amount, 1 age, 1 timestamp, 4 categorical |
| **Null / Missing Values** | 0 missing fields (0.00%) | Complete data hygiene across all columns |
| **Duplicate Records** | 0 duplicate rows (0.00%) | Every transaction record is unique |
| **Temporal Span** | 24 continuous months | March 9, 2023 to March 8, 2025 (730 calendar days) |
| **Customer Identifier** | 100 distinct labels | Account-level cohort labels (average 500 transactions per account) |
| **Currency Range** | $5.04 to $999.98 USD | Mean: $503.16, Median: $503.11, Standard Deviation: $286.56 |

---

## 📊 Detailed Visual Analytics & Empirical Findings

### 1. Temporal Dynamics & Revenue Run-Rate
- **Monthly Consistency:** Total monthly gross revenue consistently tracks between **$1.00M and $1.11M** across all 23 full calendar months.
- **Historical Peak Revenue:** **July 2023** recorded the highest gross revenue at **$1,105,402.88** across 2,154 orders ($513.19 AOV).
- **Historical Peak Volume:** **January 2024** achieved the highest transaction volume with **2,190 orders** generating $1,101,023.49.
- **Partial Period:** March 2025 covers transactions only up to March 8 (538 orders, $273,128.67), reflecting data cutoff rather than a decline in sales velocity.

### 2. Merchandising Portfolio Performance
Analysis of the 8 product categories reveals an exceptionally balanced revenue distribution:

| Product Category | Total Revenue (USD) | Order Count | Average Order Value | Share of Catalog |
| :--- | :---: | :---: | :---: | :---: |
| **Sports** | \$3,195,335.90 | 6,312 | \$506.23 | 12.70% |
| **Toys** | \$3,185,652.36 | 6,392 | \$498.38 | 12.66% |
| **Books** | \$3,181,897.30 | 6,253 | \$508.86 | 12.65% |
| **Clothing** | \$3,171,225.96 | 6,224 | \$509.52 | 12.61% |
| **Electronics** | \$3,133,965.04 | 6,320 | \$495.88 | 12.46% |
| **Grocery** | \$3,123,579.52 | 6,215 | \$502.59 | 12.42% |
| **Home & Kitchen**| \$3,108,945.78 | 6,209 | \$500.72 | 12.36% |
| **Beauty** | \$3,057,387.79 | 6,075 | \$503.27 | 12.15% |
| **Total** | **\$25,157,989.23** | **50,000** | **\$503.16** | **100.00%** |

*Insight:* The difference between the highest-grossing category (Sports) and lowest-grossing (Beauty) is merely **4.5% ($137,948.11)**. This indicates that the business has zero single-category dependency risk.

### 3. Geographic Spend & International Markets
Transactions are distributed evenly across 10 global economies (~5,000 transactions each):
- **France:** \$2,545,739.19 (4,993 orders, \$509.86 AOV)
- **Canada:** \$2,544,335.12 (5,082 orders, \$500.66 AOV)
- **USA:** \$2,541,220.22 (4,979 orders, **\$510.39 AOV — highest average ticket size**)
- **Mexico:** \$2,534,475.67 (5,059 orders, \$500.98 AOV)
- **Australia:** \$2,514,911.65 (4,985 orders, \$504.50 AOV)
- **Brazil:** \$2,507,287.54 (4,948 orders, \$506.73 AOV)
- **India:** \$2,503,542.71 (4,996 orders, \$501.11 AOV)
- **Germany:** \$2,502,442.20 (5,047 orders, \$495.83 AOV)
- **Japan:** \$2,492,312.20 (4,960 orders, \$502.48 AOV)
- **UK:** \$2,471,723.15 (4,951 orders, \$499.24 AOV)

### 4. Settlement Channels & Payment Preferences
Adoption shows equal split between cash/traditional rails and modern instant digital payment methods:
- **Cash on Delivery (COD):** \$4,276,269.38 (8,434 orders, \$507.03 AOV)
- **UPI:** \$4,259,355.65 (8,477 orders, \$502.46 AOV)
- **Debit Card:** \$4,234,776.21 (8,355 orders, \$506.86 AOV)
- **PayPal:** \$4,173,529.85 (8,250 orders, \$505.88 AOV)
- **Credit Card:** \$4,150,547.15 (8,310 orders, \$499.46 AOV)
- **Net Banking:** \$4,063,511.41 (8,174 orders, \$497.13 AOV)

### 5. Customer Demographics & Age Inelasticity
- **Linear Independence:** Pearson correlation between `Age` and `Purchase_Amount` is **r = -0.0036**, with an OLS regression slope of -0.06. This confirms that price sensitivity is uniform across age groups.
- **Age Cohort Distribution:**
  - **18–25:** 7,443 orders (14.9%) | \$3,759,841.83 revenue (\$505.15 AOV)
  - **26–35:** 9,513 orders (19.0%) | \$4,781,196.28 revenue (\$502.60 AOV)
  - **36–45:** 9,628 orders (19.3%) | \$4,863,329.78 revenue (\$505.12 AOV)
  - **46–55:** 9,303 orders (18.6%) | \$4,658,823.09 revenue (\$500.79 AOV)
  - **56–70:** 14,113 orders (**28.2%**) | **\$7,094,798.67 revenue** (\$502.71 AOV)
- *Key Takeaway:* The 56–70 cohort represents the largest gross revenue generator purely due to higher order frequency over a wider 15-year bracket.

### 6. Customer Repeat Frequency & Top Spenders
The 50,000 transactions are driven by **100 distinct customer labels**, each averaging **500 purchases**:
1. **Sophia Harris:** 568 orders | \$296,354.98 gross spend (\$521.75 AOV)
2. **James Allen:** 545 orders | \$278,079.15 gross spend (\$510.24 AOV)
3. **Olivia Hall:** 534 orders | \$277,302.09 gross spend (\$519.29 AOV)
4. **Isabella Hall:** 539 orders | \$275,798.04 gross spend (\$511.68 AOV)
5. **Noah Anderson:** 545 orders | \$274,347.15 gross spend (\$503.39 AOV)

---

## 🏛️ Power BI Architecture & DAX Modeling

The Power BI model is structured as an in-memory single-table star schema optimized for fast recalculation:
- **Core Table:** `ecommerce_transactions`
- **Measures Table:** `_Measures`
  - `Total Sales = SUM(ecommerce_transactions[Purchase_Amount])`
  - `Total Orders = COUNTROWS(ecommerce_transactions)`
  - `Distinct Customer Names = DISTINCTCOUNT(ecommerce_transactions[User_Name])`
  - `Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)`
- **Slicers:** Date range slider, Country dropdown, Category list.
- **Interactive Delivery:** Packaged alongside a self-contained interactive web application (`PowerBI_Interactive_Dashboard.html`) that replicates all slicers, cards, line graphs, bar charts, donut charts, and cross-tabulation matrices with live reactive filtering.

---

## 💡 Strategic Recommendations for Management

1. **Implement Automated Cross-Category Recommendation Engines:** Since customer spending is uniform across all categories, deploying collaborative filtering recommendation models at checkout can lift average basket size from \$503 toward \$600.
2. **Launch a Dedicated VIP Account Concierge:** Top spenders (e.g. Sophia Harris, James Allen) each contribute over \$270,000 in gross spend. Providing tailored corporate account management, exclusive bundles, and premium shipping will protect these core revenue streams.
3. **Maintain Cash on Delivery While Incentivizing Digital Instant Checkout:** With COD capturing \$4.28M, the business must preserve cash payment options in emerging markets while offering small instant-cashback incentives on UPI/debit cards to reduce cash handling overhead and reconciliation lag.
4. **Senior Demographics Digital Accessibility:** Given that customers aged 56–70 contribute 28.2% of total revenue (\$7.09M), ensuring clear typography, intuitive navigation, and responsive phone support will drive sustained retention.
