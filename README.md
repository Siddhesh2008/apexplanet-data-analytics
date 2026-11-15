# 🛒 ApexPlanet Data Analytics Internship — Master Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458.svg)](https://pandas.pydata.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-336791.svg)](https://www.postgresql.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-3776ab.svg)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3f4f75.svg)](https://plotly.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML%20Pipelines-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Hypothesis%20Testing-8CAAE6?logo=scipy&logoColor=black)](https://scipy.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Executive%20Dashboard-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Internship](https://img.shields.io/badge/Internship-ApexPlanet%20Solutions-orange.svg)](#-internship-context)

Master repository documenting the completed data analytics projects for the **ApexPlanet Solutions Data Analytics Internship**, encompassing exploratory data analysis, relational SQL database modeling, advanced statistical visualization, and interactive business intelligence dashboarding.

---

## 📌 Internship Context
- **Organization:** **ApexPlanet Solutions**
- **Intern:** Siddhesh
- **Role:** Data Analytics Intern
- **Academic Background:** 1st Year B.Tech in Artificial Intelligence & Data Science
- **Dataset:** 50,000 Global E-Commerce Transactions (\$25.16M Gross Sales)

---

## 🗺️ Roadmap & Project Navigation

```text
apexplanet-data-analytics/
├── data/
│   └── ecommerce_transactions.csv                      # Master source dataset (50,000 rows x 8 columns)
│
├── task_1_eda/                                         # Task 1: Exploratory Data Analysis & Data Hygiene
│   ├── data/
│   │   └── ecommerce_transactions.csv                  # Standalone dataset copy
│   ├── notebooks/
│   │   ├── Task_1_Exploratory_Data_Analysis.ipynb      # Master executed EDA Notebook
│   │   ├── Ecommerce.ipynb                             # Original EDA exploration notebook
│   │   └── 01_data_cleaning_eda.ipynb                  # Environment verification & smoke test
│   ├── reports/
│   │   └── Task_1_Summary.md                           # Executive EDA & Data Quality Summary Report
│   ├── requirements.txt                                # Task 1 dependencies
│   └── README.md                                       # Detailed Task 1 Guide & 15+ Viva Voce Questions
│
├── task_2_sql_database/                                # Task 2: SQL & PostgreSQL Relational Analytics
│   ├── data/
│   │   └── ecommerce_transactions.csv                  # Dataset for database ingestion
│   ├── scripts/
│   │   ├── ecommerce.sql                               # Comprehensive DDL, DML & Window Function Queries
│   │   └── db_utils.py                                 # Modular SQLAlchemy connection & query execution utility
│   ├── notebooks/
│   │   ├── Task_2_Postgres_Analytics.ipynb              # Executed PostgreSQL analytics notebook
│   │   ├── Postgres.ipynb                              # Original PostgreSQL exploration notebook
│   │   └── db_utils.ipynb                              # Connection utility notebook
│   ├── reports/
│   │   └── Task_2_Summary.md                           # Executive SQL & Relational Analytics Summary Report
│   ├── requirements.txt                                # Task 2 dependencies (SQLAlchemy, psycopg2-binary)
│   └── README.md                                       # Detailed Task 2 Guide & 15+ Viva Voce Questions
│
├── task_3_visualization/                               # Task 3: Comprehensive Data Visualization & Dashboarding
│   ├── data/
│   │   └── ecommerce_transactions.csv                  # Standalone dataset copy
│   ├── dashboards/
│   │   └── Ecommerce_Sales_Dashboard.html              # Interactive Executive Dashboard Application
│   ├── notebooks/
│   │   └── Task_3_Data_Visualization.ipynb             # Fully executed Task 3 Notebook (Matplotlib, Seaborn, Plotly)
│   ├── visualizations/                                 # 10 High-Res Exported Charts (PNG & HTML)
│   │   ├── monthly_revenue.png                         # Matplotlib Line Chart
│   │   ├── category_revenue.png                        # Matplotlib Bar Chart
│   │   ├── purchase_distribution.png                   # Matplotlib Histogram + KDE
│   │   ├── age_purchase_scatter.png                    # Matplotlib Scatter Plot + Trendline
│   │   ├── correlation_heatmap.png                     # Seaborn Correlation Matrix Heatmap
│   │   ├── pairplot.png                                # Seaborn Multivariate Pairplot
│   │   ├── category_boxen.png                          # Seaborn Letter-Value Boxen Plot
│   │   ├── monthly_revenue.html                        # Plotly Interactive Dual-Axis Time Series
│   │   ├── category_revenue.html                       # Plotly Interactive Category Breakdown
│   │   └── country_revenue.html                        # Plotly Interactive Global Choropleth Map
│   ├── powerbi/                                        # Power BI Assets, DAX Library & Manuals
│   │   ├── ecommerce_transactions_cleaned_for_powerbi.csv # Cleaned CSV for Power BI Desktop
│   │   ├── DAX_Measures_and_Data_Model.md             # Complete DAX Formula Library
│   │   ├── Power_BI_Step_by_Step_Build_Guide.md        # Step-by-Step Power BI Desktop Construction Guide
│   │   └── PowerBI_Interactive_Dashboard.html          # Interactive Executive Dashboard (Client-Side DAX Engine)
│   ├── reports/
│   │   └── Task_3_Summary.md                           # Executive Analytical Summary Report
│   ├── requirements.txt                                # Task 3 dependencies
│   └── README.md                                       # Detailed Task 3 Documentation & Viva Voce Guide
│
└── task_4_advanced_analytics/                          # Task 4: Advanced Analytics & Basic Predictive Modeling
    ├── data/
    │   └── ecommerce_transactions.csv                  # Standalone dataset copy
    ├── notebooks/
    │   └── Task_4_Advanced_Analytics.ipynb             # Fully executed Task 4 Notebook (SciPy, K-Means, ML Pipeline)
    ├── visualizations/                                 # 8 High-Res Publication Figures (PNG)
    │   ├── statistical_analysis.png                    # Distribution, Welch's t-test boxplot, Chi-Square heatmap
    │   ├── monthly_revenue.png                         # Monthly gross revenue & order volume dual-axis chart
    │   ├── moving_average_forecast.png                 # Rolling 3-month moving average forecast vs actual test data
    │   ├── time_series_decomposition.png               # Additive time-series decomposition (Trend, Seasonality, Residual)
    │   ├── elbow_method.png                            # Inertia (WCSS) & Silhouette score diagnostics
    │   ├── customer_clusters.png                       # 2D PCA projection of K-Means customer segments
    │   ├── actual_vs_predicted.png                     # Actual vs predicted purchase amount scatter plot
    │   └── residual_plot.png                           # Residual distribution and homoscedasticity check
    ├── models/
    │   └── linear_regression_pipeline.joblib           # Serialized scikit-learn Pipeline (ColumnTransformer + Model)
    ├── reports/
    │   └── Task_4_Summary.md                           # Comprehensive executive summary report
    ├── requirements.txt                                # Task 4 environment dependencies
    └── README.md                                       # Detailed Task 4 documentation & 20+ Viva Voce questions
```

---

## 🚀 Tasks Overview & Milestones

### 📍 [Task 1: Exploratory Data Analysis & Data Hygiene](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_1_eda/)
- **Primary Deliverables:** [`task_1_eda/notebooks/Task_1_Exploratory_Data_Analysis.ipynb`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_1_eda/notebooks/Task_1_Exploratory_Data_Analysis.ipynb) & [`task_1_eda/README.md`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_1_eda/README.md)
- **Key Focus:** Dataset ingestion, missing value audit (0 nulls), duplicate removal (0 duplicates), datetime parsing, summary statistics, and categorical cardinality checks across 10 countries and 8 product categories.

### 📍 [Task 2: SQL & Relational Database Analytics](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_2_sql_database/)
- **Primary Deliverables:** [`task_2_sql_database/scripts/ecommerce.sql`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_2_sql_database/scripts/ecommerce.sql) & [`task_2_sql_database/notebooks/Task_2_Postgres_Analytics.ipynb`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_2_sql_database/notebooks/Task_2_Postgres_Analytics.ipynb)
- **Key Focus:** Relational schema design, PostgreSQL database ingestion via SQLAlchemy, `GROUP BY`, `HAVING` filters, aggregate financial calculations, and analytical `ROW_NUMBER()` window functions to rank transactions and customers.

### 📍 [Task 3: Data Visualization & Executive Dashboarding](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_3_visualization/)
- **Primary Deliverables:** [`task_3_visualization/`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_3_visualization/) & [`task_3_visualization/README.md`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_3_visualization/README.md)
- **Key Focus:**
  - **Matplotlib:** Publication-quality static charts (Line, Bar, Histogram+KDE, Scatter+Trendline).
  - **Seaborn:** Advanced statistical graphics (Correlation Heatmap, Multivariate Pairplot, Letter-Value Boxen Plot).
  - **Plotly:** Interactive web visualizations with hover tooltips, zooming, and date range sliders.
  - **Power BI:** Executive dashboard architecture, comprehensive DAX formula library (`Total Sales`, `Total Orders`, `Distinct Customer Names`, `AOV`), dynamic slicers, matrix cross-tabulation, and an in-memory interactive web replica (`PowerBI_Interactive_Dashboard.html`).
  - **Documentation & Viva Prep:** Detailed executive summary report and 15 student viva questions with answers.

### 📍 [Task 4: Advanced Analytics & Basic Predictive Modeling](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_4_advanced_analytics/)
- **Primary Deliverables:** [`task_4_advanced_analytics/`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_4_advanced_analytics/) & [`task_4_advanced_analytics/README.md`](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_4_advanced_analytics/README.md)
- **Key Focus:**
  - **Inferential Statistics (SciPy):** Two-sample Welch's $t$-test (UPI vs Cash on Delivery: $t = -1.0362, p = 0.3001$) and Chi-Square ($\chi^2$) test of categorical independence ($\chi^2 = 34.4129, p = 0.4963$).
  - **Parametric Estimation:** 95% Confidence Interval for global mean spend ($[\$500.65, \$505.67]$ USD).
  - **Time-Series Analysis (statsmodels):** Monthly revenue velocity tracking (~$1.05M/month run-rate), additive seasonal decomposition, and rolling 3-month moving average forecasting evaluated on held-out test data (MAPE = 3.08%).
  - **Customer Segmentation (scikit-learn):** Account-level feature engineering across 100 customer labels, `StandardScaler`, Elbow Method & Silhouette optimization ($K=4$, peak score = 0.398), 2D PCA projection (99.4% variance explained), and 4 behavioral segment profiles.
  - **Predictive Modeling:** Production scikit-learn `Pipeline` (`StandardScaler` + `OneHotEncoder` + `LinearRegression`) predicting `Purchase_Amount`, data leakage prevention, chronological vs random split diagnostics, residual homoscedasticity checks, and feature coefficient auditing.
  - **Deliverables & Viva Prep:** Fully executed 1.29 MB Jupyter Notebook, 8 high-res PNG plots, serialized model pipeline (`.joblib`), executive report, and 20+ viva interview questions.

---

## 📊 High-Level Business Insights Summary

- **Total Gross Sales:** **\$25,157,989.23** across **50,000 transactions**.
- **Average Order Value (AOV):** **\$503.16** (Median: \$503.11, Std Dev: \$286.56).
- **Balanced Product Portfolio:** Revenue across all 8 product categories is evenly distributed, led by **Sports (\$3.20M)** and anchored by **Beauty (\$3.06M)** (variance < 4.5%).
- **Predictable Revenue Run-Rate:** Consistent monthly revenue between **\$1.00M and \$1.11M**, peaking in **July 2023 (\$1.11M)**, with peak order volume in **January 2024 (2,190 orders)**.
- **Geographic Spend Parity:** 10 international markets contribute ~\$2.5M each; **USA** drives the highest Average Order Value (**\$510.39**), while **France (\$2.55M)** leads gross volume.
- **Payment Method Coexistence:** **Cash on Delivery (\$4.28M)** and **UPI (\$4.26M)** lead adoption, demonstrating the parity of digital and traditional settlement rails.
- **Price-Age Independence:** Pearson correlation between customer age and spend is **r = -0.0036**, showing price sensitivity is uniform across age cohorts.
- **Senior Demographic Power:** Customers aged **56–70** contribute **28.2% (\$7.09M)** of total sales across 14,113 orders.
- **VIP Customer Loyalty:** 100 customer account labels generate the 50,000 transactions (averaging 500 orders each), led by **Sophia Harris** (\$296,354.98 across 568 orders).

---

## 🛠️ Tech Stack & Environment
- **Languages & Frameworks:** Python 3.10+, SQL (PostgreSQL dialect)
- **Data Science Libraries:** Pandas 3.x, NumPy 2.x, SciPy 1.18, statsmodels 0.15, SQLAlchemy
- **Machine Learning & Modeling:** scikit-learn 1.9, joblib
- **Data Visualization:** Matplotlib 3.11, Seaborn 0.13, Plotly 7.1
- **Business Intelligence:** Microsoft Power BI Desktop, DAX, Power Query
- **Development Tools:** JupyterLab, VS Code, Git, pgAdmin 4

---

## 👤 Author & Acknowledgments
- **Intern:** Siddhesh
- **Role:** Data Analytics Intern
- **Organization:** [ApexPlanet Solutions](https://apexplanetsolutions.com/)
- **Academic Discipline:** B.Tech Artificial Intelligence and Data Science (1st Year)
