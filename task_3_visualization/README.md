# 📊 Task 3: Data Visualization & Dashboarding — E-Commerce Sales Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13%2B-3776ab.svg)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3f4f75.svg)](https://plotly.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Internship](https://img.shields.io/badge/Internship-ApexPlanet%20Solutions-orange.svg)](#-internship-context)

---

## 📌 Internship Context
- **Organization:** **ApexPlanet Solutions**
- **Internship Role:** Data Analytics Intern
- **Project Scope:** **Task 3: Data Visualization & Dashboarding — Days 14 to 20**
- **Author:** Siddhesh (1st Year B.Tech in Artificial Intelligence & Data Science)

---

## 🎯 Task 3 Objectives
The primary goal of Task 3 is to bridge exploratory data analysis with executive decision-making by creating high-impact visual analytics and interactive business dashboards across two distinct toolchains:
1. **Python Data Visualization Stack (Phase 1, Days 14–15):** Building static and statistical visualizations using **Matplotlib** and **Seaborn**, alongside interactive web visualizations using **Plotly**.
2. **Business Intelligence Dashboarding Stack (Phases 2 & 3, Days 16–20):** Structuring an executive-level **Power BI** dashboard equipped with dynamic DAX measures, KPI cards, visual hierarchy, cross-tabulation matrices, and interactive slicer filter panels.

---

## 📁 Repository & Folder Organization

```text
task_3_visualization/
├── data/
│   └── ecommerce_transactions.csv                      # Local dataset copy (50,000 records)
├── dashboards/
│   └── Ecommerce_Sales_Dashboard.html                  # Interactive executive dashboard application
├── notebooks/
│   └── Task_3_Data_Visualization.ipynb                 # Fully executed Jupyter notebook with outputs
├── visualizations/                                     # Exported charts (high-res PNG & standalone HTML)
│   ├── monthly_revenue.png                             # Matplotlib: Monthly gross sales time series
│   ├── category_revenue.png                            # Matplotlib: Sorted product category revenue
│   ├── purchase_distribution.png                       # Matplotlib: Amount histogram & KDE overlay
│   ├── age_purchase_scatter.png                        # Matplotlib: Age vs spend scatter with OLS trendline
│   ├── correlation_heatmap.png                         # Seaborn: Annotated Pearson correlation matrix
│   ├── pairplot.png                                    # Seaborn: Multivariate distributions across categories
│   ├── category_boxen.png                              # Seaborn: Letter-value quantile distribution
│   ├── monthly_revenue.html                            # Plotly: Interactive dual-axis time-series
│   ├── category_revenue.html                           # Plotly: Interactive category bar chart
│   └── country_revenue.html                            # Plotly: Interactive global choropleth map
├── powerbi/
│   ├── ecommerce_transactions_cleaned_for_powerbi.csv  # Cleaned CSV pre-formatted for Power BI
│   ├── DAX_Measures_and_Data_Model.md                 # Complete DAX formula library & schema docs
│   ├── Power_BI_Step_by_Step_Build_Guide.md            # Visual-by-visual Power BI Desktop creation manual
│   └── PowerBI_Interactive_Dashboard.html              # Full in-memory interactive Power BI replica
├── reports/
│   └── Task_3_Summary.md                               # Executive analytical findings report
├── requirements.txt                                    # Environment dependencies
└── README.md                                           # Task 3 documentation & Viva Voce guide
```

---

## 📊 Dataset Overview & Integrity Rules

The dataset contains **50,000 completed e-commerce transactions** recorded between **March 9, 2023** and **March 8, 2025**.

### Key Statistical Parameters
- **Gross Revenue:** \$25,157,989.23 (~**\$25.16 Million USD**)
- **Total Orders:** 50,000 completed transactions
- **Average Order Value (AOV):** \$503.16 (Median: \$503.11, Std Dev: \$286.56)
- **Customer Age Range:** 18 to 70 years (Mean: 43.97 years)
- **Data Quality:** **0 null values** across all 8 columns, **0 duplicate records** detected.
- **Data Integrity Rule:** `User_Name` has 100 distinct labels, each representing an account profile averaging 500 transactions. It is documented and evaluated as an account cohort label rather than an assumed legal identity.

---

## 📈 Visualizations Built & Techniques Used

### 1. Matplotlib (Procedural & Publication-Grade)
- **Monthly Revenue Trend (`monthly_revenue.png`):** Continuous time series line chart with shaded area, formatted currency axis, and arrow annotations marking peak sales in **July 2023 ($1.11M)**.
- **Revenue by Product Category (`category_revenue.png`):** Sorted vertical bar chart with exact value labels ($3.20M down to $3.06M).
- **Purchase Amount Distribution (`purchase_distribution.png`):** 40-bin probability density histogram overlaid with a smooth **Kernel Density Estimate (KDE)** and vertical dashed lines marking Mean ($503.16) and Median ($503.11).
- **Customer Age vs. Purchase Amount (`age_purchase_scatter.png`):** Scatter plot utilizing alpha transparency to prevent overplotting, an ordinary least squares regression trendline, and annotated Pearson correlation (**r = -0.0036**).

### 2. Seaborn (Statistical Modeling Layer)
- **Correlation Heatmap (`correlation_heatmap.png`):** Diverging heatmap (`vlag` colormap) evaluating linear dependencies among numerical features (`Age`, `Purchase_Amount`, `Year`, `Month`, `Day_of_Week`).
- **Statistical Pairplot (`pairplot.png`):** Bivariate scatter plots and diagonal univariate KDE distributions across numerical variables, segmented by product category.
- **Category Boxen Plot (`category_boxen.png`):** Advanced letter-value plot illustrating recursive quantiles (1/8, 1/16, 1/32) across the 8 categories, confirming uniform dispersion without outlier distortion.

### 3. Plotly (Client-Side Interactive Web Graphics)
- **Interactive Monthly Revenue & Volume (`monthly_revenue.html`):** Dual-axis interactive chart linking transaction volume bars with gross revenue lines, custom hover tooltips (Revenue, Orders, AOV), and a date range slider.
- **Interactive Category Breakdown (`category_revenue.html`):** Interactive horizontal bar chart with hover metadata showing order volume, AOV, and catalog percentage.
- **Interactive Country Choropleth (`country_revenue.html`):** Interactive world map with ISO-3 country mapping, dynamic hover cards, and zoom/pan controls.

---

## 🖥️ Power BI Executive Dashboard Architecture

The dashboard design adheres strictly to enterprise business intelligence principles:
- **Title:** **E-COMMERCE SALES PERFORMANCE DASHBOARD**
- **Grid Layout:** 16:9 widescreen canvas (1280 x 720 px) in executive navy and soft slate.
- **Top KPI Cards Banner:**
  - `Total Sales = SUM(ecommerce_transactions[Purchase_Amount])` -> **$25.16M**
  - `Total Orders = COUNTROWS(ecommerce_transactions)` -> **50,000**
  - `Distinct Customer Names = DISTINCTCOUNT(ecommerce_transactions[User_Name])` -> **100**
  - `Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)` -> **$503.16**
- **Visuals Included:**
  1. Monthly Sales Revenue Trend (Line Chart)
  2. Revenue Breakdown by Product Category (Clustered Bar Chart)
  3. Payment Method Adoption Share (Donut Chart)
  4. Global Geographic Spend (Map / Bar Visual)
  5. Top 10 Customer Labels by Total Spend (Top N Bar Chart)
  6. Cross-Tabulation Matrix (Country rows x Category columns x Sales values with data bars)
- **Interactive Slicers Panel:**
  - Date Range Slicer (Between slider)
  - Country Slicer (Dropdown multi-select)
  - Product Category Slicer (Vertical list)

### Interactive Browser Replica
For immediate demonstration and grading without requiring a Power BI Desktop installation or Microsoft organizational tenant license, launch:
👉 **[PowerBI_Interactive_Dashboard.html](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_3_visualization/powerbi/PowerBI_Interactive_Dashboard.html)**  
*(Contains a complete in-memory reactive filtering engine matching Power BI DAX evaluations).*

---

## 💡 Top 8 Empirical Business Insights

1. **Catalog Revenue Diversity:** Product categories show near-equal revenue generation, led by **Sports ($3.20M)** and anchored by **Beauty ($3.06M)**. The tight 4.5% variance protects the business against single-category demand shocks.
2. **Predictable Cash Flow:** Complete calendar months show a steady run rate between **$1.00M and $1.11M**, allowing six-month forward inventory planning with minimal forecasting error.
3. **Summer & Winter Revenue Peaks:** Peak monthly gross revenue occurred in **July 2023 ($1,105,402.88)**, while peak transaction volume occurred in **January 2024 (2,190 orders)**.
4. **Geographic Parity:** All 10 international markets contribute evenly (~$2.5M each). **USA** generates the highest Average Order Value (**$510.39**), while **France ($2.55M)** leads total gross volume.
5. **Payment Method Balance:** Traditional **Cash on Delivery ($4.28M)** and digital **UPI ($4.26M)** lead adoption, demonstrating that emerging and digital payment channels must coexist.
6. **Age-Price Independence:** Pearson correlation between Age and Spend is **r = -0.0036**. Age does not predict basket size; customers across all ages purchase across all price tiers.
7. **Senior Demographic Spending Power:** The **56–70 age group** accounts for **28.2% ($7.09M)** of total sales across 14,113 orders due to demographic breadth and repeat purchasing consistency.
8. **High-Value Account Concentration:** The 100 customer account labels average 500 transactions each. The top account, **Sophia Harris**, contributed **$296,354.98** across 568 orders, justifying an exclusive VIP account concierge program.

---

## 🚀 How to Run & Reproduce This Project

### 1. Prerequisites
Ensure Python 3.10+ is available.
```bash
cd apexplanet-data-analytics
```

### 2. Activate Virtual Environment & Install Dependencies
```bash
# Windows
.venv\Scripts\activate

# Install requirements
pip install pandas numpy matplotlib seaborn plotly jupyter
```

### 3. Open the Jupyter Notebook
```bash
jupyter lab task_3_visualization/notebooks/Task_3_Data_Visualization.ipynb
```
*(All cells are pre-executed with tables, plots, and markdown notes fully embedded).*

### 4. Launch the Interactive Dashboard in Browser
Double-click or open:
```text
task_3_visualization/powerbi/PowerBI_Interactive_Dashboard.html
```

---

## 🎓 How to Explain This Project in a Viva (Student Guide)

### Elevator Pitch:
> *"In Task 3, I developed an end-to-end data visualization and business intelligence solution analyzing 50,000 e-commerce transactions totaling $25.16 million in gross sales. I utilized Matplotlib for publication-grade static figures, Seaborn for statistical distribution and correlation modeling, Plotly for responsive web charts, and structured an executive Power BI dashboard with DAX measures, dynamic slicers, and cross-tabulation matrices."*

### 15 Essential Viva Questions & Model Answers

1. **Q: Why did you choose three different Python visualization libraries?**  
   *A:* Matplotlib provides low-level procedural control over every figure element for static publications; Seaborn automates statistical modeling (KDE, boxen plots, regression fits); Plotly generates interactive, client-side HTML charts using JavaScript.
2. **Q: What is the key advantage of an interactive chart (HTML) over a static image (PNG)?**  
   *A:* Interactive charts allow users to hover for dynamic metadata, zoom into specific time ranges, and toggle series on and off without modifying or re-executing code.
3. **Q: Why did you use a Boxen Plot instead of a standard Box Plot?**  
   *A:* In large datasets (50,000 rows), standard box plots flag thousands of normal tail observations as cluttering outliers. Boxen plots calculate recursive quantiles into the tails, giving an accurate picture of tail distribution.
4. **Q: What is Kernel Density Estimation (KDE)?**  
   *A:* KDE applies a continuous Gaussian smoothing kernel over every data point to estimate the true Probability Density Function (PDF) independent of arbitrary histogram bin widths.
5. **Q: What does a Pearson correlation of r = -0.0036 between Age and Purchase Amount signify?**  
   *A:* It indicates virtually zero linear correlation, meaning customer age has no linear association with transaction amount.
6. **Q: Does correlation imply causation?**  
   *A:* No. Correlation only quantifies statistical co-movement. Causation requires controlled experiments, domain mechanisms, or randomized trials.
7. **Q: Why compare the Mean and Median of purchase amounts?**  
   *A:* Because Mean is sensitive to extreme values while Median is resistant. Here, Mean ($503.16) and Median ($503.11) are nearly identical, demonstrating that the distribution is symmetrical and unskewed.
8. **Q: What are KPI Cards in Power BI and where should they be placed?**  
   *A:* KPI cards display high-level aggregate numbers. According to visual hierarchy design principles, they should be placed across the top where stakeholders scan first.
9. **Q: What is DAX in Power BI and how does it differ from Power Query M-code?**  
   *A:* Power Query M-code is an ETL language executed during data loading. DAX (Data Analysis Expressions) is evaluated in-memory post-load to dynamically calculate measures based on user filter contexts.
10. **Q: Explain the DAX measure for Total Sales.**  
    *A:* `Total Sales = SUM(ecommerce_transactions[Purchase_Amount])`. It aggregates gross sales dynamically under the active slicer context.
11. **Q: Why did you use DISTINCTCOUNT for customer labels instead of COUNT?**  
    *A:* `COUNT` counts rows (50,000), whereas `DISTINCTCOUNT` counts unique customer account labels (100 distinct profiles).
12. **Q: How do Slicers operate in Power BI?**  
    *A:* Slicers pass filter parameters to the in-memory data engine, instantly recalculating all DAX measures and redrawing all canvas visuals.
13. **Q: What is the purpose of the Matrix visual?**  
    *A:* It provides a cross-tabulation table (Country rows x Product Category columns x Total Sales values) allowing cross-border category comparisons.
14. **Q: Why treat `User_Name` as a customer label rather than verified legal identities?**  
    *A:* Good data governance avoids assuming unverified synthetic strings represent real individual identities; they represent account cohorts or account labels.
15. **Q: What is the #1 commercial takeaway for management?**  
    *A:* With demand balanced evenly across all categories, management should avoid price discounting and instead implement cross-selling recommendations and VIP account retention programs for top accounts.
