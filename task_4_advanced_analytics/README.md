# 📊 Task 4: Advanced Analytics & Basic Predictive Modeling
### E-Commerce Transaction Analysis & Machine Learning Pipeline

**Internship Program:** ApexPlanet Data Analytics Internship — Roadmap Task 4 (Days 21–26)  
**Author:** Siddhesh (1st Year B.Tech Artificial Intelligence and Data Science)  
**Date:** November 2026  
**Status:** Completed, Fully Tested, and Peer-Reviewed  
**Project Workspace:** `task_4_advanced_analytics/`

---

## 📖 Table of Contents
1. [Project Overview & Internship Roadmap](#-project-overview--internship-roadmap)
2. [Dataset Overview & Architectural Hygiene](#-dataset-overview--architectural-hygiene)
3. [Technologies & Tools Used](#-technologies--tools-used)
4. [Phase 1: Inferential Statistics & Hypothesis Testing](#-phase-1-inferential-statistics--hypothesis-testing)
5. [Phase 2: Time-Series Analysis & Forecasting](#-phase-2-time-series-analysis--forecasting)
6. [Phase 3: Customer Segmentation (K-Means Clustering)](#-phase-3-customer-segmentation-k-means-clustering)
7. [Phase 4: Supervised Predictive Modeling (Linear Regression)](#-phase-4-supervised-predictive-modeling-linear-regression)
8. [Consolidated Business Insights & Action Plan](#-consolidated-business-insights--action-plan)
9. [Project Directory & Deliverables](#-project-directory--deliverables)
10. [How to Run the Project](#-how-to-run-the-project)
11. [Viva Voce Technical Defense Guide (20+ Q&A)](#-viva-voce-technical-defense-guide-20-qa)
12. [Professional LinkedIn Showcase Post](#-professional-linkedin-showcase-post)

---

## 🎯 Project Overview & Internship Roadmap

As part of the **ApexPlanet Data Analytics Internship**, Task 4 marks the transition from foundational business intelligence into advanced statistical science, unsupervised machine learning, and predictive modeling:
- **Task 1 (Days 1–7):** Data Cleaning, Hygiene Auditing, and Exploratory Data Analysis.
- **Task 2 (Days 8–14):** Relational Schema Design, PostgreSQL Ingestion, and Advanced SQL Querying.
- **Task 3 (Days 15–20):** Interactive Visualization, Power BI DAX Modeling, and Executive Dashboards.
- **Task 4 (Days 21–26):** **Inferential Hypothesis Testing, Time-Series Forecasting, K-Means Clustering, and Supervised Linear Regression Modeling.**

### Analytical Scope & Deliverables
- **Hypothesis Testing:** Two-sample Welch's $t$-test (UPI vs Cash on Delivery) and Chi-Square ($\chi^2$) test of categorical independence using SciPy.
- **Parametric Estimation:** 95% Confidence Interval for global mean spend.
- **Time-Series Analysis:** Monthly resampling, additive seasonal decomposition via `statsmodels`, and rolling 3-month moving average forecasting.
- **Customer Segmentation:** Account-level behavioral feature engineering, Euclidean feature scaling (`StandardScaler`), Elbow & Silhouette optimization, 2D Principal Component Analysis (PCA) projection, and cluster profiling.
- **Predictive Machine Learning:** Leak-free scikit-learn `Pipeline` and `ColumnTransformer` architecture for transaction-level `Purchase_Amount` regression, chronological vs randomized data split diagnostics, residual homoscedasticity evaluation, and transparent feature influence auditing.

---

## 🗂️ Dataset Overview & Architectural Hygiene

The analysis utilizes the authoritative transactional dataset located at `data/ecommerce_transactions.csv`:
- **Total Records:** 50,000 transaction events.
- **Feature Dimensions:** 8 attributes (`Transaction_ID`, `User_Name`, `Age`, `Country`, `Product_Category`, `Purchase_Amount`, `Payment_Method`, `Transaction_Date`).
- **Data Hygiene:** 0 missing values (0.00%), 0 duplicate records (0.00%).
- **Temporal Horizon:** March 9, 2023 to March 8, 2025 (730 calendar days / 24 full months).
- **Target Metric Span:** \$5.04 to \$999.98 USD (Mean: \$503.16, Median: \$503.11, Standard Deviation: \$286.56).

### Strict Methodological Rules Observed:
1. **No Data Fabrication:** All statistical parameters, $p$-values, cluster profiles, and model metrics are computed directly from actual data.
2. **Account Label Integrity:** `User_Name` is recognized as an account-level cohort label (100 distinct labels averaging 500 orders each), rather than verified individual identities.
3. **No Target Leakage:** Training and testing partitions are strictly isolated, and preprocessing transformers are fitted exclusively on training sets.
4. **Distinction Between Association and Causation:** Statistical correlation is never conflated with causal business mechanisms.

---

## 💻 Technologies & Tools Used

- **Python 3.14:** Core analytical programming environment.
- **pandas & NumPy:** Data wrangling, array manipulation, and temporal resampling.
- **SciPy (`scipy.stats`):** Two-sample $t$-tests, Levene's test, Chi-Square contingency tests, and confidence interval estimation.
- **statsmodels:** Time-series seasonal decomposition (`seasonal_decompose`).
- **scikit-learn:** `StandardScaler`, `OneHotEncoder`, `ColumnTransformer`, `Pipeline`, `KMeans`, `silhouette_score`, `PCA`, `LinearRegression`, and regression evaluation metrics (`r2_score`, `mean_absolute_error`, `mean_squared_error`).
- **Matplotlib & Seaborn:** Publication-grade visual figures and diagnostic plots.
- **joblib:** Model serialization and persistence.
- **Jupyter Notebook & nbclient:** Programmatic notebook execution and documentation.

---

## 🔬 Phase 1: Inferential Statistics & Hypothesis Testing

### 1. Descriptive Statistics Summary Table

| Metric | Mean | Median | Mode | Std Dev | Min | Max | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Purchase Amount ($)** | \$503.16 | \$503.11 | \$447.06 | \$286.56 | \$5.04 | \$999.98 | -0.0027 | -1.1989 |
| **Customer Age (Years)** | 43.97 | 44.00 | 43 | 15.26 | 18 | 70 | 0.0059 | -1.1969 |

- **Distributional Insight:** Parity between mean (\$503.16) and median (\$503.11) and near-zero skewness (-0.0027) confirm that purchase amounts follow an exceptionally balanced, platykurtic uniform distribution across the \$5 to \$1,000 product catalog.

![Statistical Analysis](visualizations/statistical_analysis.png)

### 2. Independent Two-Sample $t$-Test: UPI vs Cash on Delivery (COD)
- **Hypothesis Formulation:**
  - $H_0: \mu_{\text{UPI}} = \mu_{\text{COD}}$ (Mean spending is equal across UPI and Cash on Delivery).
  - $H_1: \mu_{\text{UPI}} \neq \mu_{\text{COD}}$ (Mean spending differs significantly).
- **Group Statistics:**
  - **UPI:** $N = 8,477$, Mean = \$502.46, Std Dev = \$285.40, Variance = 81,453.34
  - **Cash on Delivery:** $N = 8,434$, Mean = \$507.03, Std Dev = \$287.75, Variance = 82,797.91
- **Levene's Variance Test:** Statistic = $1.5141, p = 0.2185$ (Confirms homoscedasticity).
- **Welch's $t$-test Result:** $t = -1.0362, p = 0.3001$
- **Decision:** **FAIL TO REJECT $H_0$** ($\alpha = 0.05$). There is no statistically significant difference in mean spend between UPI and Cash on Delivery. Payment rail selection does not drive cart value.

### 3. Chi-Square ($\chi^2$) Test of Independence: Category vs Payment Method
- **Hypothesis Formulation:**
  - $H_0$: Product Category and Payment Method are independent.
  - $H_1$: Product Category and Payment Method are dependent.
- **Contingency Dimensions:** 8 categories $\times$ 6 payment channels = 48 cells ($\text{dof} = 35$).
- **Assumption Check:** Minimum expected cell frequency is $993.14$, far exceeding the minimum threshold of 5.0.
- **Result:** $\chi^2 = 34.4129, p = 0.4963$.
- **Decision:** **FAIL TO REJECT $H_0$**. Product category selection is statistically independent of payment method. Customers do not restrict payment channels to specific product departments.

### 4. 95% Confidence Interval for Global Mean Purchase Amount
- **Sample Size:** $n = 50,000$
- **Sample Mean ($\bar{x}$):** \$503.1598
- **Standard Error of the Mean ($\text{SEM}$):** \$1.2816
- **Degrees of Freedom:** $49,999$
- **Margin of Error ($ME$):** \$2.5118
- **95% Confidence Interval:** **[\$500.6479, \$505.6716] USD**
- **Methodological Takeaway:** We can state with 95% confidence that the true global mean transaction value lies within this narrow \$5.02 band. This applies strictly to the population mean, not individual purchase spreads.

---

## ⏳ Phase 2: Time-Series Analysis & Forecasting

### 1. Resampling & Revenue Run-Rate
- Transaction timestamps were resampled to month-end frequency (`ME`), revealing an extraordinarily steady sales velocity of **\$1.00M to \$1.11M USD** across 23 full calendar months.
- Peak gross sales occurred in **July 2023 (\$1,105,402.88)**; peak order volume occurred in **January 2024 (2,190 orders)**.
- Partial boundary periods (March 2023: 23 days, \$802,390; March 2025: 8 days, \$273,129) were isolated to avoid misinterpreting cutoff dates as economic downturns.

![Monthly Revenue](visualizations/monthly_revenue.png)

### 2. Time-Series Decomposition & Methodological Limitations
- Decomposed monthly revenue into Trend, Seasonal, and Residual components using `statsmodels` (additive model, period = 12).
- **Critical Methodological Finding:** The series contains 25 monthly observations (exactly 2 complete annual cycles). Classical decomposition typically requires 3 to 5 full cycles (36–60 months) to distinguish true repeating annual seasonality from random monthly noise. We document this caveat transparently and provide a rolling moving average as an operational baseline.

![Time Series Decomposition](visualizations/time_series_decomposition.png)

### 3. Moving-Average Forecast Evaluation
- **Forecast Window:** 3-month rolling moving average ($k=3$).
- **Held-Out Test Window:** November 2024 to February 2025 (4 full months).
- **Performance:**
  - **Mean Absolute Error (MAE):** \$30,015.17
  - **Root Mean Squared Error (RMSE):** \$50,509.46
  - **Mean Absolute Percentage Error (MAPE):** **3.08%**
- **Conclusion:** Moving average forecasts track steady monthly revenue with ~3% margin of error, proving highly effective for baseline inventory procurement.

![Moving Average Forecast](visualizations/moving_average_forecast.png)

---

## 👥 Phase 3: Customer Segmentation (K-Means Clustering)

### 1. Account-Level Feature Engineering & Standardization
- Transactions were aggregated across the 100 distinct `User_Name` account labels into:
  - `Total_Spend`: Lifetime account value proxy.
  - `Transaction_Count`: Loyalty and order frequency proxy.
  - `Average_Purchase`: Purchasing power ticket proxy.
- Features were standardized using `StandardScaler` to ensure Euclidean distances were not distorted by the large variance of `Total_Spend`.

### 2. Elbow Method & Silhouette Optimization
- Evaluated $K \in [2, 8]$.
- **Inertia Inflection:** Clear elbow identified at $K = 4$ (Inertia drops from 120.12 at $K=3$ to 85.26 at $K=4$).
- **Silhouette Coefficient:** Peaks at **0.3977 at $K = 4$** (indicating optimal cluster cohesion and separation).

![Elbow Method](visualizations/elbow_method.png)

### 3. 2D Principal Component Analysis (PCA) & Cluster Profiles
- Applied PCA to project the 3 standardized features into 2 dimensions:
  - **PC1 (57.6% variance):** Driven by order count and total spend.
  - **PC2 (41.8% variance):** Driven by average order value (ticket size).
  - **Total Explained Variance:** **99.4%**.

![Customer Clusters PCA](visualizations/customer_clusters.png)

### 4. Segment Behavioral Profiles & Action Plans

| Cluster ID | Segment Title | Accounts | Avg Total Spend | Avg Orders | Avg Ticket (AOV) | Commercial Action Plan |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **Cluster 1** | **High-Volume Champions** | 8 | \$277,383.04 | 545.38 | \$508.57 | Elite enterprise buyers (>\\$2.2M gross sales). Assign dedicated account concierge and priority logistics. |
| **Cluster 2** | **High-Ticket Value Buyers** | 37 | \$258,896.83 | 502.65 | \$515.11 | Premium catalog consumers with highest AOV. Cross-sell luxury electronics and sports gear bundles. |
| **Cluster 3** | **Core Steady Spenders** | 33 | \$249,798.45 | 506.79 | \$492.90 | Recurring baseline accounts. Deploy subscription replenishment models and loyalty point multipliers. |
| **Cluster 0** | **Growth Potential Buyers** | 22 | \$232,563.34 | 468.86 | \$496.08 | Lower order frequency accounts. Deploy automated win-back re-engagement emails and flash promotions. |

---

## 🤖 Phase 4: Supervised Predictive Modeling (Linear Regression)

### 1. Problem Definition & Pipeline Architecture
- **Target Variable ($y$):** `Purchase_Amount` (USD, continuous).
- **Features ($X$):** `Age` (StandardScaler), `Country`, `Product_Category`, `Payment_Method` (OneHotEncoder, `drop='first'`).
- **Excluded Features:** `Transaction_ID` (database index) and `User_Name` (account label).
- **Partition:** 80% Training ($N=40,000$), 20% Held-Out Testing ($N=10,000$), `random_state=42`.
- Preprocessing and estimator integrated into a scikit-learn `Pipeline` to eliminate data leakage.

### 2. Model Performance on Unseen Test Data
- **Coefficient of Determination ($R^2$):** **-0.001197 ($\approx 0.00$)**
- **Mean Absolute Error (MAE):** **\$249.24**
- **Root Mean Squared Error (RMSE):** **\$287.83**
- **Model Intercept:** **\$513.06 USD**

![Actual vs Predicted](visualizations/actual_vs_predicted.png)
![Residual Plot](visualizations/residual_plot.png)

### 3. Senior Data Scientist Diagnostic Explanation of $R^2 \approx 0.00$
- In e-commerce analytics, reporting $R^2 \approx 0.00$ is **an authentic, empirically verified result**.
- Because prices range uniformly from \$5 to \$1,000 across *every country, every category, and every age group*, demographic and channel attributes provide zero linear price discrimination.
- In a uniform distribution $U(0, 1000)$, the theoretical standard deviation is $\sigma = \frac{1000}{\sqrt{12}} \approx 288.67$, and the theoretical MAE from predicting the mean is $\frac{1000}{4} = 250.00$. Our empirical results ($\text{MAE} = \$249.24, \text{RMSE} = \$287.83$) match these theoretical benchmarks with remarkable precision.
- **Takeaway:** Predicting individual cart spend requires **basket-level features** (item count, SKU price, discounts, session time), not broad customer demographics.

### 4. Top Influential Coefficients (Relative to Baseline)
1. **`Payment_Method_Net Banking`:** Coefficient = **-\$13.18 USD**
2. **`Country_UK`:** Coefficient = **-\$9.57 USD**
3. **`Payment_Method_UPI`:** Coefficient = **-\$8.48 USD**

---

## 💡 Consolidated Business Insights & Action Plan

1. **Maintain Parity Across Payment Rails:** UPI and COD exhibit identical spending patterns ($p = 0.3001$). Support both channels equally without discriminatory fees.
2. **Catalog-Wide Channel Freedom:** Payment method choice is independent of product department ($p = 0.4963$); avoid restricting payment options.
3. **Revenue Predictability:** Stable \$1.05M monthly revenue run-rate allows confident forward financial planning.
4. **Procurement Forecasting:** Adopt the 3-month moving average model (MAPE = 3.08%) for near-term inventory stocking.
5. **Protect VIP Accounts:** Launch a white-glove retention program for the 8 High-Volume Champions (Cluster 1, >\$2.2M gross sales).
6. **Cross-Sell Premium Bundles:** Target the 37 High-Ticket Buyers (Cluster 2, \$515.11 AOV) with luxury bundles.
7. **Automated Re-engagement:** Trigger win-back discounts for the 22 Growth Potential Accounts (Cluster 0) after 14 days of inactivity.
8. **Invest in Behavioral Tracking:** Expand telemetry to capture cart item count and session duration for future production machine learning.

---

## 📁 Project Directory & Deliverables

```text
task_4_advanced_analytics/
│
├── data/
│   └── ecommerce_transactions.csv          # Local dataset copy (50,000 records)
│
├── notebooks/
│   └── Task_4_Advanced_Analytics.ipynb     # Fully executed Jupyter notebook with all outputs
│
├── visualizations/
│   ├── statistical_analysis.png            # Distribution, Welch's t-test boxplot, Chi-Square heatmap
│   ├── monthly_revenue.png                 # Monthly gross revenue and order velocity dual-axis chart
│   ├── moving_average_forecast.png         # 3-Month moving average forecast vs actual test data
│   ├── time_series_decomposition.png       # Observed, Trend, Seasonal, Residual decomposition
│   ├── elbow_method.png                    # Inertia (WCSS) and Silhouette score diagnostics
│   ├── customer_clusters.png               # 2D PCA projection of K-Means customer segments
│   ├── actual_vs_predicted.png             # Scatter plot of actual vs predicted purchase amount
│   └── residual_plot.png                   # Residual error distribution and homoscedasticity check
│
├── models/
│   └── linear_regression_pipeline.joblib   # Serialized scikit-learn Pipeline (preprocessor + model)
│
├── reports/
│   └── Task_4_Summary.md                   # Comprehensive executive summary report
│
├── generate_assets.py                      # Standalone Python asset generation script
├── explore_task4.py                        # Statistical exploration and verification script
├── requirements.txt                        # Python library dependencies
└── README.md                               # Complete project documentation and viva defense guide
```

---

## 🚀 How to Run the Project

### 1. Activate Environment & Install Dependencies
```bash
# Ensure Python 3.10+ is available
cd task_4_advanced_analytics
pip install -r requirements.txt
```

### 2. Generate All Visualizations & Models
```bash
python generate_assets.py
```

### 3. Launch and Inspect the Notebook
```bash
jupyter notebook notebooks/Task_4_Advanced_Analytics.ipynb
```

---

## 🎓 Viva Voce Technical Defense Guide (20+ Q&A)

### Category A: Statistics & Hypothesis Testing
1. **Q: What is the difference between descriptive and inferential statistics?**  
   *A:* Descriptive statistics summarize observed sample data (mean, median, standard deviation). Inferential statistics use sample data to test hypotheses or estimate parameters about an entire population (e.g., $t$-tests, confidence intervals).
2. **Q: When should the median be preferred over the mean?**  
   *A:* When the distribution is skewed or has heavy outliers, as the median is robust. In our dataset, the mean (\$503.16) and median (\$503.11) are nearly identical, confirming symmetry.
3. **Q: What does a standard deviation of \$286.56 indicate?**  
   *A:* It measures the average dispersion of transaction values around the mean across the wide \$5 to \$1,000 catalog span.
4. **Q: What does near-zero skewness (-0.0027) mean?**  
   *A:* It confirms that transactions are distributed symmetrically above and below the center without long tails.
5. **Q: What is a null hypothesis ($H_0$)?**  
   *A:* The baseline proposition stating no effect or difference exists. In our $t$-test, $H_0$ stated that mean spend is equal between UPI and COD.
6. **Q: How do you interpret $p = 0.3001$ in the $t$-test?**  
   *A:* Since $p = 0.3001 > \alpha = 0.05$, there is a 30% chance the observed \$4.57 difference is due to random noise. We fail to reject $H_0$.
7. **Q: Why use Welch's $t$-test instead of Student's $t$-test?**  
   *A:* Welch's $t$-test does not assume equal population variances, making it more robust against unequal variances and sample sizes.
8. **Q: What does the Chi-Square test of independence evaluate?**  
   *A:* It tests whether two categorical variables are associated. With $\chi^2 = 34.41, p = 0.4963$, we confirmed product category and payment method are independent.
9. **Q: What does a 95% Confidence Interval represent?**  
   *A:* In 95 out of 100 hypothetical repeat samples, the calculated interval will contain the true population parameter. Our CI is $[\$500.65, \$505.67]$.
10. **Q: Does a 95% CI of $[\$500.65, \$505.67]$ mean 95% of individual purchases fall in this range?**  
    *A:* **No.** That is a common misconception. It applies strictly to the *population mean*, which has a tiny standard error due to $N=50,000$. Individual purchases range from \$5 to \$1,000.

### Category B: Time-Series Analysis
11. **Q: What is temporal resampling?**  
    *A:* Aggregating timestamps into standard intervals (e.g., daily, monthly) to analyze macro sales velocity.
12. **Q: What are the components of time-series decomposition?**  
    *A:* Trend (secular direction), Seasonality (repeating cyclical pattern), and Residuals (unexplained noise).
13. **Q: Why was seasonal decomposition limited on this dataset?**  
    *A:* The dataset covers 24 full months (2 annual cycles). Reliable seasonal estimation typically requires 3 to 5 full cycles (36–60 months).
14. **Q: What are the limitations of a moving-average forecast?**  
    *A:* It is a lagging filter; it smooths historical data but cannot anticipate trend reversals or sudden demand spikes.

### Category C: Unsupervised Customer Segmentation
15. **Q: Why aggregate data by `User_Name` before clustering?**  
    *A:* Clustering individual transactions segments *orders*, not *customers*. Aggregating to account metrics captures ongoing customer relationship value.
16. **Q: Why is `StandardScaler` necessary before K-Means?**  
    *A:* K-Means relies on Euclidean distance. Features with large numerical ranges (`Total_Spend`) would dominate features with smaller scales (`Average_Purchase`).
17. **Q: How does the Elbow Method determine optimal $K$?**  
    *A:* It plots within-cluster sum of squares (inertia) against $K$. The point where inertia reduction slows marks the optimal cluster count.
18. **Q: What role does PCA play in clustering?**  
    *A:* PCA reduces 3 standardized features into 2 orthogonal components (explaining 99.4% variance) for 2D visual inspection of cluster separation.

### Category D: Supervised Machine Learning
19. **Q: How does scikit-learn's `Pipeline` prevent data leakage?**  
    *A:* It encapsulates transformers and estimators so normalization parameters and encoders are fitted strictly on training data, preventing test set leakage.
20. **Q: Why did Linear Regression achieve $R^2 \approx 0.00$?**  
    *A:* Because demographic features (Age, Country) and payment methods exhibit zero linear correlation with transaction ticket size in this uniformly priced catalog. Predicting the mean is mathematically optimal given these features.

---

## 📱 Professional LinkedIn Showcase Post

```markdown
🚀 Excited to share the completion of Task 4 of my ApexPlanet Data Analytics Internship!

Over the past week, I expanded my analytical toolkit from exploratory data analysis and SQL modeling into advanced inferential statistics, time-series forecasting, unsupervised machine learning, and predictive modeling using Python.

🔍 Key Methodologies & Empirical Insights:
1️⃣ Inferential Hypothesis Testing (SciPy):
• Conducted an independent two-sample Welch's t-test comparing UPI vs Cash on Delivery (COD) transactions (t = -1.0362, p = 0.3001). Result: Failed to reject H0, confirming spend is statistically identical across payment rails ($502.46 vs $507.03).
• Performed a Chi-Square (χ²) Test of Independence between Product Categories and Payment Methods (χ² = 34.41, p = 0.4963), proving catalog purchases are independent of payment channel.
• Computed a 95% Confidence Interval for the global population mean spend: [$500.65, $505.67] USD.

2️⃣ Time-Series Analysis & Forecasting (statsmodels):
• Resampled 50,000 transactions across 24 full billing cycles, tracking an exceptionally steady gross revenue run-rate of ~$1.05M/month.
• Evaluated an additive seasonal decomposition and constructed a rolling 3-month moving average forecast achieving an impressive 3.08% Mean Absolute Percentage Error (MAPE) on held-out test data.

3️⃣ Customer Segmentation (scikit-learn K-Means & PCA):
• Engineered account-level features (Total Spend, Transaction Count, AOV) across 100 accounts.
• Applied StandardScaler and optimized K=4 using the Elbow Method and Silhouette Analysis (peak silhouette = 0.398).
• Visualized clusters via 2D Principal Component Analysis (PCA) and identified 4 distinct commercial personas, including High-Volume Champions (N=8 accounts contributing >$2.2M gross sales) and High-Ticket Value Buyers ($515.11 AOV).

4️⃣ Predictive Modeling & Pipeline Engineering:
• Built a leak-free scikit-learn Pipeline with ColumnTransformer (StandardScaler + OneHotEncoder) to model transaction Purchase_Amount.
• Transparently evaluated model behavior: demonstrated why demographic features yield R² ≈ 0.00 and an expected MAE of $249.24 in a uniformly distributed product catalog, highlighting the critical distinction between statistical association and causal prediction.

A huge thank you to the ApexPlanet mentors for this rigorous, industry-aligned learning journey!

#ApexPlanet #DataAnalytics #DataScience #MachineLearning #Python #Statistics #TimeSeries #CustomerSegmentation #ArtificialIntelligence
```
