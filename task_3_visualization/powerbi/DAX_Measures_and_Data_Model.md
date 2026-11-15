# 📐 DAX Measures, Calculated Columns & Data Model Reference
**Project:** Task 3 — E-Commerce Sales Performance Dashboard  
**Internship:** ApexPlanet Data Analytics Internship  
**Platform:** Microsoft Power BI Desktop  
**Data Source:** `ecommerce_transactions_cleaned_for_powerbi.csv` (50,000 rows)

---

## 🗄️ 1. Data Model Schema

The data model follows a high-performance **Single-Table Star Schema** (denormalized fact-dimension model) optimized for Power BI's VertiPaq in-memory columnar engine.

### Table: `ecommerce_transactions`

| Column Name | Data Type | Data Category | Description |
| :--- | :--- | :--- | :--- |
| `Transaction_ID` | Whole Number (`int64`) | None | Unique primary key for each transaction |
| `User_Name` | Text (`string`) | None | Customer account label (100 distinct labels) |
| `Age` | Whole Number (`int64`) | None | Customer age in years (18–70) |
| `Country` | Text (`string`) | **Country** | Geographic market (10 nations) |
| `Product_Category`| Text (`string`) | None | Merchandising category (8 categories) |
| `Purchase_Amount` | Decimal Number (`Currency`) | None | Gross transaction value in USD ($5.04 – $999.98) |
| `Payment_Method`  | Text (`string`) | None | Settlement gateway utilized (6 payment types) |
| `Transaction_Date`| Date (`date`) | None | Transaction timestamp (March 9, 2023 – March 8, 2025) |
| `Year` | Whole Number | None | Calendar Year (2023, 2024, 2025) |
| `Month_Number` | Whole Number | None | Numeric Month (1–12) |
| `Month_Name` | Text | None | Full Month name (e.g., January) |
| `Month_Short` | Text | None | 3-letter Month abbreviation (e.g., Jan) |
| `Year_Month` | Text | None | Formatted year-month string (`YYYY-MM`) |
| `Year_Month_Sort`| Whole Number | None | Numeric sort key (`YYYYMM`, e.g., 202303) |
| `Day_of_Week` | Text | None | Day name (e.g., Monday, Tuesday) |
| `Day_of_Week_Number` | Whole Number | None | Numeric Day index (0–6) |
| `Age_Group` | Text | None | Analytical demographic cohort |

> [!TIP]
> **Data Modeling Best Practice in Power BI:**  
> Ensure that `Year_Month` is configured with **Sort by Column** -> `Year_Month_Sort`. This guarantees that chronological sorting (2023-03 through 2025-03) is preserved across all visuals instead of alphabetical sorting.

---

## 📊 2. Core KPI DAX Measures

Create a dedicated empty table named `_Measures` in Power BI to centralize all analytical metrics.

### Measure 1: Total Sales (Gross Revenue)
```DAX
Total Sales = 
SUM(ecommerce_transactions[Purchase_Amount])
```
* **Format:** Currency (`$#,##0.00`)
* **Description:** Computes the total gross transaction revenue dynamically evaluated within the current visual filter context.
* **Empirical Total:** **$25,157,989.23**

### Measure 2: Total Orders (Transaction Count)
```DAX
Total Orders = 
COUNTROWS(ecommerce_transactions)
```
* **Format:** Whole Number with thousands separator (`#,##0`)
* **Description:** Counts the exact volume of orders processed.
* **Empirical Total:** **50,000**

### Measure 3: Distinct Customer Names (User Labels)
```DAX
Distinct Customer Names = 
DISTINCTCOUNT(ecommerce_transactions[User_Name])
```
* **Format:** Whole Number (`#,##0`)
* **Description:** Counts unique customer account identifiers in the dataset.
* **Important Data Interpretation Rule:** *We label this measure "Distinct Customer Names" because User_Name represents account labels provided by the dataset rather than legally verified individual identities.*
* **Empirical Total:** **100**

### Measure 4: Average Order Value (AOV)
```DAX
Average Order Value = 
DIVIDE([Total Sales], [Total Orders], 0)
```
* **Format:** Currency (`$#,##0.00`)
* **Description:** Evaluates the mean basket value per completed transaction. Uses `DIVIDE()` to protect against division-by-zero errors.
* **Empirical Total:** **$503.16**

### Measure 5: Average Revenue per Customer
```DAX
Average Spend per Customer = 
DIVIDE([Total Sales], [Distinct Customer Names], 0)
```
* **Format:** Currency (`$#,##0.00`)
* **Description:** Calculates average customer lifetime value across the 100 account labels.
* **Empirical Total:** **$251,579.89**

---

## 📈 3. Advanced & Time-Intelligence DAX Measures

### Measure 6: Month-over-Month (MoM) Sales Growth %
```DAX
Sales Prior Month = 
CALCULATE(
    [Total Sales],
    PREVIOUSMONTH(ecommerce_transactions[Transaction_Date])
)
```
```DAX
MoM Sales Growth % = 
DIVIDE(
    [Total Sales] - [Sales Prior Month],
    [Sales Prior Month],
    BLANK()
)
```
* **Format:** Percentage (`0.0%`)
* **Description:** Tracks month-over-month revenue velocity to monitor seasonal growth.

### Measure 7: Category Contribution Share (%)
```DAX
Category Revenue Share % = 
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALL(ecommerce_transactions[Product_Category])),
    0
)
```
* **Format:** Percentage (`0.0%`)
* **Description:** Computes the proportional revenue percentage of each product category against the global catalog total.

---

## 🧮 4. DAX Calculated Columns

### Calculated Column 1: Age Group Cohort
```DAX
Age_Group_DAX = 
SWITCH(
    TRUE(),
    ecommerce_transactions[Age] >= 18 && ecommerce_transactions[Age] <= 25, "18-25",
    ecommerce_transactions[Age] >= 26 && ecommerce_transactions[Age] <= 35, "26-35",
    ecommerce_transactions[Age] >= 36 && ecommerce_transactions[Age] <= 45, "36-45",
    ecommerce_transactions[Age] >= 46 && ecommerce_transactions[Age] <= 55, "46-55",
    ecommerce_transactions[Age] >= 56 && ecommerce_transactions[Age] <= 70, "56-70",
    "Other"
)
```

### Calculated Column 2: High-Value Customer Tier
```DAX
Customer_Tier = 
IF(
    ecommerce_transactions[Purchase_Amount] >= 750,
    "High Ticket (>$750)",
    IF(
        ecommerce_transactions[Purchase_Amount] >= 250,
        "Mid Ticket ($250-$749)",
        "Entry Ticket (<$250)"
    )
)
```

---

## 🎯 5. Verification Checklist for Power BI
Before finalizing your Power BI file, verify that the following measures match the exact ground-truth values:

- [x] **Total Sales:** `$25,157,989.23`
- [x] **Total Orders:** `50,000`
- [x] **Distinct Customer Names:** `100`
- [x] **Average Order Value:** `$503.16`
- [x] **Top Category:** `Sports` (`$3,195,335.90`)
- [x] **Top Country:** `France` (`$2,545,739.19`)
- [x] **Top Payment Method:** `Cash on Delivery` (`$4,276,269.38`)
