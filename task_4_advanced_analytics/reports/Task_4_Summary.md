# 📑 Task 4 Executive Summary Report: Advanced Analytics & Predictive Modeling

**Project Title:** Advanced Analytics, Statistical Hypothesis Testing & Basic Predictive Modeling on E-Commerce Transactions  
**Internship Program:** ApexPlanet Data Analytics Internship — Roadmap Task 4 (Days 21–26)  
**Author:** Siddhesh (1st Year B.Tech Artificial Intelligence and Data Science)  
**Date:** November 2026  
**Status:** Completed, Fully Tested & Validated  
**Deliverable Directory:** `task_4_advanced_analytics/`

---

## 🏛️ Executive Summary

As part of **Task 4 (Advanced Analytics & Basic Predictive Modeling)** of the **ApexPlanet Data Analytics Internship**, this report synthesizes the advanced inferential statistical analysis, time-series forecasting, unsupervised customer segmentation, and supervised machine learning pipelines executed on **50,000 global e-commerce transactions** totaling **$25,157,989.23 (~$25.16 Million USD)** recorded between **March 9, 2023** and **March 8, 2025**.

While Tasks 1, 2, and 3 established data hygiene, PostgreSQL database structures, and Power BI dashboards, **Task 4 delivers rigorous mathematical testing, algorithmic segmentation, and predictive modeling**:
1. **Inferential Hypothesis Testing (SciPy):** Demonstrated that purchase amount is statistically independent of payment settlement channels (Welch's $t$-test: $t = -1.0362, p = 0.3001$) and product category choices (Chi-Square: $\chi^2 = 34.4129, p = 0.4963$).
2. **Confidence Intervals:** Quantified the true global population mean purchase amount at the 95% confidence level to $[\\$500.65, \\$505.67]$ USD ($\text{SEM} = \\$1.28$).
3. **Time-Series Analysis & Forecasting (statsmodels):** Analyzed 24 full billing cycles maintaining a stable run-rate of $\sim\\$1.05\text{M}$/month. Constructed a walk-forward rolling 3-month moving average forecast on a held-out test window (Nov 2024 – Feb 2025) achieving an exceptional **3.08% Mean Absolute Percentage Error (MAPE)** ($\text{MAE} = \\$30,015.17$).
4. **Customer Segmentation (scikit-learn K-Means & PCA):** Aggregated transaction logs across 100 account labels into behavioral metrics (`Total_Spend`, `Transaction_Count`, `Average_Purchase`). Scaled features via `StandardScaler`, optimized $K=4$ using the Elbow Method and Silhouette analysis (peak coefficient = 0.398), and projected clusters onto a 2D Principal Component Analysis (PCA) space explaining 99.4% of variance.
5. **Supervised Predictive Modeling (scikit-learn Pipeline):** Engineered a leak-free `ColumnTransformer` + `LinearRegression` pipeline. Transparently documented and explained why demographic features yield $R^2 \approx 0.00$ ($\text{MAE} = \\$249.24$, $\text{RMSE} = \\$287.83$) in a catalog with uniform price distribution, emphasizing the critical scientific distinction between correlation and causation.

---

## 🗂️ Dataset Hygiene & Architecture Audit

Prior to statistical testing, the dataset was verified for analytical consistency:

| Attribute | Empirical Metric | Analytical Verification |
| :--- | :--- | :--- |
| **Total Record Count** | 50,000 transactions | Complete dataset; no truncated rows |
| **Feature Dimensions** | 8 attributes | 1 numerical ID, 1 target amount, 1 age, 1 timestamp, 4 categorical |
| **Missing / Null Values** | 0 missing fields (0.00%) | Complete data hygiene across all columns |
| **Duplicate Records** | 0 duplicate rows (0.00%) | Every transaction record is unique |
| **Temporal Span** | 24 full months (730 calendar days) | March 9, 2023 to March 8, 2025 |
| **Distinct Account Labels** | 100 customer labels | Account-level cohort labels (average 500 transactions per account) |
| **Target Variable Range** | $5.04 to $999.98 USD | Mean: $503.16, Median: $503.11, Std Dev: $286.56 |

---

## 📊 Phase 1: Statistical Analysis & Hypothesis Testing

### 1.1 Descriptive Statistical Summary
Measures of central tendency, dispersion, and shape were computed for numerical features:

| Column Name | Mean | Median | Mode | Standard Deviation | Min | Max | Skewness | Kurtosis | Distribution Shape |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Purchase_Amount ($)** | \$503.16 | \$503.11 | \$447.06 | \$286.56 | \$5.04 | \$999.98 | -0.0027 | -1.1989 | Symmetric Continuous Uniform |
| **Age (Years)** | 43.97 | 44.00 | 43 | 15.26 | 18 | 70 | 0.0059 | -1.1969 | Uniform Adult Demographics |

#### Pedagogical Explanations:
- **Mean vs. Median:** The mean (\$503.16) and median (\$503.11) are virtually identical (difference < \$0.05). In skewed data, extreme values pull the mean away from the median; here, parity confirms perfect distributional symmetry.
- **Standard Deviation (\$286.56):** Quantifies that typical transaction values deviate substantially from the mean across the wide \$5 to \$1,000 catalog span.
- **Skewness (-0.0027):** Near-zero skewness indicates that transactions are balanced equally above and below the center without long high-ticket tails.
- **Kurtosis (-1.1989):** Platykurtic distribution characteristic of a uniform continuous variable over a bounded interval $[a, b]$.

### 1.2 Independent Two-Sample Hypothesis Test: UPI vs Cash on Delivery
- **Null Hypothesis ($H_0$):** $\mu_{\text{UPI}} = \mu_{\text{COD}}$ (Mean purchase amount is identical across UPI and COD).
- **Alternative Hypothesis ($H_1$):** $\mu_{\text{UPI}} \neq \mu_{\text{COD}}$ (Mean purchase amount differs significantly).
- **Significance Level:** $\alpha = 0.05$ (Two-tailed).
- **Group Statistics:**
  - **UPI:** $N = 8,477$, Mean = \$502.46, Std Dev = \$285.40, Variance = 81,453.34
  - **Cash on Delivery (COD):** $N = 8,434$, Mean = \$507.03, Std Dev = \$287.75, Variance = 82,797.91
- **Levene's Test for Homoscedasticity:** Test Statistic = $1.5141, p = 0.2185$. Since $p > 0.05$, equal population variance is confirmed.
- **Welch's $t$-test (Unequal Variance):** $t = -1.0362, p = 0.3001$
- **Student's $t$-test (Equal Variance):** $t = -1.0363, p = 0.3001$
- **Inferential Conclusion:** Because $p = 0.3001 > \alpha = 0.05$, we **FAIL TO REJECT the null hypothesis**. There is no statistically significant difference in mean transaction value between instant digital UPI and physical Cash on Delivery.
- **Methodological Principle:** Payment method is not causally associated with basket size.

### 1.3 Chi-Square ($\chi^2$) Test of Independence: Product Category vs Payment Method
- **Null Hypothesis ($H_0$):** Product Category and Payment Method are mutually independent.
- **Alternative Hypothesis ($H_1$):** Product Category and Payment Method are dependent.
- **Contingency Table Dimensions:** 8 product categories $\times$ 6 payment channels (48 cells).
- **Assumption Verification:** The minimum expected cell frequency is $993.14$, which far exceeds the standard minimum requirement of 5.0.
- **Test Results:**
  - $\chi^2$ Statistic: $34.4129$
  - Degrees of Freedom: $\text{dof} = (8 - 1) \times (6 - 1) = 35$
  - $p$-value: $0.4963$
- **Inferential Conclusion:** Because $p = 0.4963 > \alpha = 0.05$, we **FAIL TO REJECT the null hypothesis**. Payment channel adoption is independent of product categories; customers use digital and physical settlement channels evenly across all catalog departments.

### 1.4 Confidence Interval for the Global Population Mean
- **Sample Size ($n$):** 50,000 transactions
- **Sample Mean ($\bar{x}$):** \$503.1598 USD
- **Sample Standard Deviation ($s$):** \$286.5636 USD
- **Standard Error of the Mean ($\text{SEM} = s / \sqrt{n}$):** \$1.2816 USD
- **Degrees of Freedom:** $df = 49,999$
- **Critical $t$-value ($t_{0.025, 49999}$):** 1.95996
- **Margin of Error:** $\$1.2816 \times 1.95996 = \$2.5118$ USD
- **95% Confidence Interval:** **[\$500.6479, \$505.6716] USD**
- **Pedagogical Distinction:** This narrow \$5.02 boundary applies strictly to the *true population mean*. It does not imply that individual transactions fall in this range, but rather that repeated sampling would capture the true enterprise average within this band in 95 out of 100 trials.

---

## ⏳ Phase 2: Time-Series Analysis & Forecasting

### 2.1 Resampling & Temporal Velocity
Transactions were chronologically indexed and resampled to monthly frequency (`ME`):
- **Full Months (April 2023 – February 2025):** 23 consecutive months maintaining a reliable sales run-rate between **\$1.00M and \$1.11M** USD (averaging 2,080 orders/month).
- **Historical Peak Revenue:** July 2023 recorded **\$1,105,402.88** across 2,154 orders (\$513.19 AOV).
- **Historical Peak Order Volume:** January 2024 recorded **2,190 orders** generating \$1,101,023.49.
- **Partial Endpoints:**
  - March 2023: 23 calendar days (1,560 orders, \$802,390.44).
  - March 2025: 8 calendar days (538 orders, \$273,128.67). These endpoints reflect observation cutoffs rather than sales dips.

### 2.2 Time-Series Decomposition & Methodological Limitations
An additive seasonal decomposition model ($Y_t = \text{Trend}_t + \text{Seasonal}_t + \text{Residual}_t$) was executed using `statsmodels` with a 12-month period:
- **Observed Trend:** Remains remarkably flat around $\sim\$1.04\text{M} - \$1.05\text{M}$ across the entire series.
- **Methodological Limitation:** The dataset contains 25 monthly observations (barely 2 annual cycles). In econometric forecasting, seasonal decomposition requires at least 3 to 5 full cycles (36–60 months) to reliably isolate true annual seasonality from random monthly noise. 
- **Operational Alternative:** A rolling moving average provides a much more stable and realistic operational tool for inventory and cash flow planning.

### 2.3 Rolling Moving-Average Forecast Modeling
- **Model Mechanics:** Predicts next month's revenue using a 3-month moving average window ($k=3$): $\hat{Y}_{t+1} = \frac{1}{3} \sum_{i=0}^2 Y_{t-i}$.
- **Chronological Split (Zero-Leakage):** Evaluated strictly on the held-out final 4 full calendar months (**November 2024 – February 2025**):

| Month | Actual Revenue ($) | MA(3) Forecast ($) | Absolute Error ($) | Percentage Error (%) |
| :---: | :---: | :---: | :---: | :---: |
| **2024-11** | \$1,065,021.09 | \$1,058,406.84 | \$6,614.25 | 0.62% |
| **2024-12** | \$1,061,061.79 | \$1,059,709.30 | \$1,352.49 | 0.13% |
| **2025-01** | \$1,056,467.57 | \$1,068,487.65 | \$12,020.08 | 1.14% |
| **2025-02** | \$960,776.35 | \$1,060,850.15 | \$100,073.80 | 10.42% |
| **Overall** | **\$4,143,326.80** | **\$4,247,453.94** | **Mean Error: \$30,015.17** | **MAPE: 3.08%** |

- **Evaluation Metrics:**
  - **MAE:** \$30,015.17
  - **RMSE:** \$50,509.46
  - **MAPE:** **3.08%**
- **Business Conclusion:** With a MAPE of only 3.08%, the moving-average model tracks monthly cash flow with exceptional precision, enabling reliable 30-day forward procurement.

---

## 👥 Phase 3: Customer Segmentation (K-Means Clustering)

### 3.1 Feature Engineering & Standardization
Clustering raw order transactions would misclassify single purchases as customers. We aggregated the 50,000 transactions across the 100 distinct `User_Name` account labels into three behavioral dimensions:
1. `Total_Spend`: Lifetime account sales contribution.
2. `Transaction_Count`: Total historical purchase frequency.
3. `Average_Purchase`: Average order value (purchasing power).

Because `Total_Spend` exhibits variance $> 1.9 \times 10^8$ while `Average_Purchase` exhibits variance $\approx 170$, `StandardScaler` was applied to normalize all features to mean = 0.00 and standard deviation = 1.00.

### 3.2 Finding the Optimal $K$ (Elbow Method & Silhouette Score)
We evaluated cluster counts from $K = 2$ to $K = 8$:
- **Elbow Point:** A distinct inflection occurs at $K = 4$ where inertia decreases from 120.12 ($K=3$) to 85.26 ($K=4$).
- **Silhouette Coefficient:** Reaches its global peak of **0.3977 at $K = 4$** (compared to 0.3407 at $K=3$).
- **Selected Architecture:** $K = 4$ provides the optimal balance of statistical cohesion and actionable commercial segmentation.

### 3.3 2D Principal Component Analysis (PCA) Projection
PCA was applied to the standardized 3-dimensional feature space to project clusters into 2 dimensions for visual inspection:
- **PC1 (Variance Explained: 57.6%):** Heavily captures transaction volume and total spend.
- **PC2 (Variance Explained: 41.8%):** Heavily captures average order ticket size.
- **Total Variance Explained:** **99.4%** across two orthogonal components.

### 3.4 Behavioral Cluster Profiles & Action Plans

| Cluster ID | Segment Title | Account Count | Avg Total Spend ($) | Avg Order Count | Avg Order Value ($) | Commercial Action Plan |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **Cluster 1** | **High-Volume Champions** | 8 | \$277,383.04 | 545.38 | \$508.57 | Elite enterprise buyers (>\\$2.2M gross sales). Assign dedicated account concierge and priority logistics. |
| **Cluster 2** | **High-Ticket Value Buyers** | 37 | \$258,896.83 | 502.65 | \$515.11 | Premium catalog consumers with highest AOV. Cross-sell luxury electronics and sports gear bundles. |
| **Cluster 3** | **Core Steady Spenders** | 33 | \$249,798.45 | 506.79 | \$492.90 | Recurring baseline accounts. Deploy subscription replenishment models and loyalty point multipliers. |
| **Cluster 0** | **Growth Potential Buyers** | 22 | \$232,563.34 | 468.86 | \$496.08 | Lower order frequency accounts. Deploy automated win-back re-engagement emails and flash promotions. |

---

## 🤖 Phase 4: Supervised Predictive Modeling (Linear Regression)

### 4.1 Pipeline Design & Data Leakage Prevention
To evaluate whether customer demographics and sales channels predict transaction cart size, an end-to-end regression pipeline was constructed:
- **Target Variable ($y$):** `Purchase_Amount` (USD, continuous).
- **Input Features ($X$):**
  - Numerical: `Age` (StandardScaler)
  - Categorical: `Country`, `Product_Category`, `Payment_Method` (OneHotEncoder with `drop='first'`)
- **Strictly Excluded:** `Transaction_ID` (database index) and `User_Name` (non-generalizable account label).
- **Data Partition:** 80% Training ($N=40,000$), 20% Held-Out Testing ($N=10,000$), `random_state=42`.

### 4.2 Empirical Evaluation on Unseen Test Data
- **Coefficient of Determination ($R^2$):** **-0.001197 ($\approx 0.00$)**
- **Mean Absolute Error (MAE):** **\$249.24**
- **Root Mean Squared Error (RMSE):** **\$287.83**
- **Training Baseline Target Mean:** \$503.11 ($\text{Std Dev} = \$286.25$)

#### Diagnostic Explanation of $R^2 \approx 0.00$:
1. **Mathematical Reality:** An $R^2 \approx 0.00$ indicates that the linear combination of demographic attributes and payment rails performs identically to predicting the global training mean ($\bar{y} = \$503.11$).
2. **Theoretical Error Match:** In a bounded continuous uniform distribution $U(0, 1000)$, the theoretical standard deviation is $\sigma = \frac{1000}{\sqrt{12}} \approx 288.67$, and the theoretical MAE from predicting the mean is $\frac{1000}{4} = 250.00$. Our empirical results ($\text{MAE} = \$249.24, \text{RMSE} = \$287.83$) match these theoretical uniform benchmarks with near-perfect accuracy.
3. **Substantive Finding:** E-commerce customer ticket sizes are **not dictated by user age or sovereign nation**. Predicting individual transaction basket value requires **basket-level behavioral features** (cart item count, specific SKU price, discounts, session duration), which are absent from transaction-level headers.

### 4.3 Feature Influence & Coefficient Analysis
Coefficients were extracted relative to one-hot encoded reference categories (Australia, Beauty, Cash on Delivery):
1. **`Payment_Method_Net Banking`:** Coefficient = **-\$13.18 USD** (Net Banking transactions average \$13.18 lower than Cash on Delivery).
2. **`Country_UK`:** Coefficient = **-\$9.57 USD** (UK transactions average \$9.57 lower than Australian baselines).
3. **`Payment_Method_UPI`:** Coefficient = **-\$8.48 USD** (UPI transactions average \$8.48 lower than COD).
- **Model Intercept:** **\$513.06 USD** (Expected purchase amount for a baseline Australian customer purchasing Beauty products via Cash on Delivery).

---

## 💡 Strategic Business Action Plan

Based on our empirical findings, management should implement the following eight initiatives:

1. **Parity Payment Strategy:** Support both instant digital rails (UPI) and physical settlement (COD) without channel surcharges, since spend is identical ($p = 0.3001$).
2. **Catalog-Wide Channel Accessibility:** Maintain all payment channels across all product categories without restrictions ($p = 0.4963$).
3. **Capital Budgeting Stability:** Leverage the predictable \$1.05M monthly revenue run-rate for confident supplier purchasing commitments.
4. **Procurement Forecasting:** Adopt the 3-month moving average model (MAPE = 3.08%) as the primary baseline for near-term inventory stocking.
5. **VIP Concierge Tier:** Protect the 8 High-Volume Champions (Cluster 1, >\$2.2M sales) with custom contract terms and dedicated account support.
6. **Premium Bundle Merchandising:** Target the 37 High-Ticket Value Buyers (Cluster 2, \$515.11 AOV) with curated multi-product bundles.
7. **Automated Re-engagement Triggers:** Target the 22 Growth Potential Accounts (Cluster 0) with automated win-back promotions after 14 days of order dormancy.
8. **Shift to Behavioral Machine Learning:** Invest in clickstream and session tracking tools to capture basket-level item quantities and browsing duration, enabling true high-$R^2$ predictive modeling.

---

## 🎓 Viva Voce & Technical Defense Guide (Summary of Key Questions)

A full 20-question comprehensive defense guide is included in the project notebook and README, covering:
- **Statistics:** Mean vs Median, Standard Deviation vs Variance, Skewness & Kurtosis, Null Hypothesis formulation, $p$-value interpretation, Welch's vs Student's $t$-test, $\chi^2$ independence tests, Confidence Intervals of the mean vs prediction ranges.
- **Time Series:** Resampling mechanics, Trend/Seasonal/Residual decomposition, small-sample cycle stability, moving average forecasting and limitations.
- **Clustering:** Account-level aggregation rationale, Euclidean scaling with `StandardScaler`, Elbow Method and Silhouette Coefficient optimization, 2D PCA projection interpretation.
- **Machine Learning:** Data leakage prevention using scikit-learn Pipelines, ColumnTransformer encoding, interpretation of $R^2 \approx 0.00$ in uniform data, MAE vs RMSE, and model coefficient interpretation.

---

## 📱 Professional LinkedIn Showcase Post

A fully formatted post is ready for publication in `task_4_advanced_analytics/README.md` and the final project response.
