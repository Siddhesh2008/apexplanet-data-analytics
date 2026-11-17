# 🛠️ Power BI Step-by-Step Build & Implementation Manual
**Dashboard Title:** E-COMMERCE SALES PERFORMANCE DASHBOARD  
**Project:** Task 3 — Data Visualization & Dashboarding  
**Internship:** ApexPlanet Data Analytics Internship  
**Author:** Siddhesh (1st Year B.Tech AI & Data Science)

---

## 📋 Executive Overview
This guide provides an exhaustive, visual-by-visual manual for creating the **E-Commerce Sales Performance Dashboard** in **Microsoft Power BI Desktop**. It guides you from raw data ingestion and DAX modeling to building executive KPI cards, advanced charts, filter panels, and deploying to Power BI Service.

---

## 🚀 Step 1: Ingesting the Dataset
1. Launch **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV**.
3. Navigate to and select:
   ```text
   apexplanet-data-analytics\task_3_visualization\powerbi\ecommerce_transactions_cleaned_for_powerbi.csv
   ```
4. In the preview window, confirm delimiter is **Comma** and character encoding is **65001: UTF-8**.
5. Click **Transform Data** to open Power Query Editor:
   - Verify `Transaction_Date` is formatted as **Date**.
   - Verify `Purchase_Amount` is formatted as **Decimal Number**.
   - Verify `Age` is formatted as **Whole Number**.
6. Click **Close & Apply** in the top-left corner.

---

## ⚙️ Step 2: Configure Column Sorting & Data Categorization
To prevent alphabetical sorting errors in months and maps:
1. In the **Data Pane**, select the column `Year_Month`.
2. Go to the **Column Tools** ribbon at the top.
3. Click **Sort by Column** and choose **`Year_Month_Sort`**. *(This ensures months appear from March 2023 to March 2025 in exact chronological order).*
4. Select the column `Country`.
5. In **Column Tools**, set **Data Category** to **`Country`**. *(This tells Power BI to use geographic map geocoding).*

---

## 🧮 Step 3: Create the `_Measures` Table
1. On the **Home** ribbon, click **Enter Data**.
2. Name the table `_Measures` and click **Load**.
3. Right-click `_Measures` -> **New Measure** and create the core measures (see [DAX_Measures_and_Data_Model.md](file:///c:/Users/Siddhesh/Desktop/coding/apexplanet-data-analytics/task_3_visualization/powerbi/DAX_Measures_and_Data_Model.md)):
   - `Total Sales = SUM(ecommerce_transactions[Purchase_Amount])` *(Format: Currency $)*
   - `Total Orders = COUNTROWS(ecommerce_transactions)` *(Format: Whole Number #,##0)*
   - `Distinct Customer Names = DISTINCTCOUNT(ecommerce_transactions[User_Name])` *(Format: Whole Number #,##0)*
   - `Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)` *(Format: Currency $)*
4. Delete the blank "Column1" inside `_Measures` to make it a pure calculator icon.

---

## 🎨 Step 4: Canvas Layout & Corporate Styling Setup
1. Click on the canvas background.
2. In the **Format Pane** -> **Canvas Settings**:
   - **Type:** 16:9 (1280 x 720 px).
3. **Canvas Background:** Set color to `#F4F6F9` (light executive gray) with 0% transparency.
4. **Header Banner:**
   - Insert a **Rectangle Shape** across the top: `X: 0, Y: 0, Width: 1280, Height: 70`.
   - Fill Color: `#0F2C59` (Deep Executive Navy).
   - Insert a **Text Box** inside the banner:
     - Text: **E-COMMERCE SALES PERFORMANCE DASHBOARD**
     - Subtitle: *ApexPlanet Solutions — Data Analytics Internship Task 3*
     - Font: Segoe UI, Bold, White, Size 18pt.

---

## 📊 Step 5: Visual-by-Visual Configuration

### 1. KPI Cards Banner (Top Row: Y: 80, Height: 90)
Create 4 **Card** or **New Card (Preview)** visuals side by side:
* **Card 1 (Total Sales):**
  - Field: `[Total Sales]`
  - Callout Value: Bold, Color `#0F2C59`, Display units: Auto (displays `$25.16M`).
  - Category Label: "TOTAL GROSS SALES".
* **Card 2 (Total Orders):**
  - Field: `[Total Orders]`
  - Callout Value: displays `50,000`.
  - Category Label: "TOTAL COMPLETED ORDERS".
* **Card 3 (Distinct Customer Names):**
  - Field: `[Distinct Customer Names]`
  - Callout Value: displays `100`.
  - Category Label: "ACTIVE CUSTOMER LABELS".
* **Card 4 (Average Order Value):**
  - Field: `[Average Order Value]`
  - Callout Value: displays `$503.16`.
  - Category Label: "AVERAGE ORDER VALUE (AOV)".

---

### 2. Left Filter & Slicer Panel (X: 15, Y: 185, Width: 200, Height: 520)
Insert a light panel container (`#FFFFFF`, border `#E0E0E0`, rounded corners 6px) containing 3 slicers:
* **Slicer 1 (Date Range):**
  - Field: `ecommerce_transactions[Transaction_Date]`
  - Slicer Style: **Between (Slider)**.
* **Slicer 2 (Country Filter):**
  - Field: `ecommerce_transactions[Country]`
  - Slicer Style: **Dropdown** or **Vertical list with search**.
* **Slicer 3 (Product Category Filter):**
  - Field: `ecommerce_transactions[Product_Category]`
  - Slicer Style: **Vertical list**.

---

### 3. Visual 1: Monthly Sales Revenue Trend (Line Chart)
* **Visual Type:** **Line Chart**
* **Position:** `X: 230, Y: 185, Width: 520, Height: 250`
* **X-Axis:** `ecommerce_transactions[Year_Month]`
* **Y-Axis:** `[Total Sales]`
* **Formatting:**
  - Line Color: `#0D6EFD` (Blue), Stroke width: 3.
  - Turn **Data Markers** ON (Shape: Circle, Size: 5).
  - Title: *"Monthly Gross Revenue Trend (2023–2025)"*.
  - Turn Y-Axis gridlines ON (Dashed, light gray).

---

### 4. Visual 2: Revenue by Product Category (Clustered Bar Chart)
* **Visual Type:** **Clustered Bar Chart** (Horizontal)
* **Position:** `X: 765, Y: 185, Width: 495, Height: 250`
* **Y-Axis (Categories):** `ecommerce_transactions[Product_Category]`
* **X-Axis (Values):** `[Total Sales]`
* **Sort:** Sort descending by `[Total Sales]` (Sports on top).
* **Formatting:**
  - Bar Color: `#1F4E79`.
  - Turn **Data Labels** ON (Position: Outside end, Display units: Millions `$#.##M`).
  - Title: *"Revenue Breakdown by Product Category"*.

---

### 5. Visual 3: Payment Method Share (Donut Chart)
* **Visual Type:** **Donut Chart**
* **Position:** `X: 230, Y: 450, Width: 280, Height: 255`
* **Legend:** `ecommerce_transactions[Payment_Method]`
* **Values:** `[Total Sales]`
* **Formatting:**
  - Detail Labels: Category and Percentage of Total (`Data value, percent of total`).
  - Title: *"Payment Method Revenue Share"*.
  - Color Palette: Blues & Teals (`#1976D2`, `#0288D1`, `#0097A7`, `#00796B`, `#388E3C`, `#689F38`).

---

### 6. Visual 4: Global Geographic Sales (Map Visual)
* **Visual Type:** **Map** (Bubble Map) or **Filled Map** (Choropleth)
* **Position:** `X: 525, Y: 450, Width: 350, Height: 255`
* **Location:** `ecommerce_transactions[Country]`
* **Bubble Size:** `[Total Sales]`
* **Tooltips:** `[Total Sales]`, `[Total Orders]`, `[Average Order Value]`
* **Formatting:**
  - Map Style: Grayscale or Light.
  - Bubble Color: `#E65100` (Amber/Orange).
  - Title: *"Global Geographic Spend by Country"*.

---

### 7. Visual 5: Top 10 Customer Labels (Bar Chart)
* **Visual Type:** **Clustered Bar Chart**
* **Position:** `X: 890, Y: 450, Width: 370, Height: 255`
* **Y-Axis:** `ecommerce_transactions[User_Name]`
* **X-Axis:** `[Total Sales]`
* **Filter:** In the **Filters on this visual** pane:
  - Select `User_Name` -> Filter Type: **Top N**.
  - Show items: **Top 10**.
  - By value: Drag `[Total Sales]`.
  - Click **Apply filter**.
* **Formatting:**
  - Bar Color: `#2E7D32` (Forest Green).
  - Turn **Data Labels** ON.
  - Title: *"Top 10 Customer Labels by Total Spend"*.

---

### 8. Visual 6: Country vs. Category Matrix (Separate Tab / Drilldown)
* **Visual Type:** **Matrix**
* **Rows:** `ecommerce_transactions[Country]`
* **Columns:** `ecommerce_transactions[Product_Category]`
* **Values:** `[Total Sales]`
* **Formatting:**
  - Turn **Conditional Formatting** ON -> Data Bars (Color: Soft Blue).
  - Column Grand Totals & Row Grand Totals ON.
  - Title: *"Cross-Tabulation Matrix: Revenue by Country & Category"*.

---

## 🧪 Step 6: Testing Dashboard Interactivity
Before presenting or publishing, test the following checklist:

| Test Item | Action | Expected Behavior |
| :--- | :--- | :--- |
| **Date Slicer** | Drag date slider to Jan 1, 2024 – Dec 31, 2024 | Total Sales updates to ~$12.6M; Monthly chart shrinks to 12 months. |
| **Country Slicer** | Click "USA" | Map zooms to USA; Total Sales shows ~$2.54M; KPI cards update. |
| **Category Slicer** | Select "Sports" | All visuals reflect only Sports sales ($3.20M total). |
| **Bar Cross-Filter** | Click on "Electronics" in Visual 2 | Line chart, map, and donut highlight Electronics proportion. |
| **Clear Filters** | Click reset/eraser on slicers | All 50,000 transactions and $25.16M gross revenue restore. |

---

## 🌐 Step 7: Publishing to Power BI Service

If you have a corporate or student Microsoft account (`@college.edu` or organization email):
1. In Power BI Desktop, click **Save** (`Ecommerce_Sales_Dashboard.pbix`).
2. Click the **Publish** button on the **Home** ribbon.
3. Select **My Workspace** (or your team workspace) and click **Select**.
4. Once publication finishes, click the link: **Open 'Ecommerce_Sales_Dashboard.pbix' in Power BI**.
5. In Power BI Service:
   - Click **File** -> **Embed report** -> **Publish to web (public)**.
   - Click **Create embed code** -> **Publish**.
   - Copy the generated shareable URL and embed iframe.

> [!NOTE]
> **Licensing Transparency Note:**  
> If you are using a personal Microsoft account (`@gmail.com` or `@outlook.com`), Microsoft Power BI Service blocks "Publish to Web" due to security policies requiring an organizational/school tenant. In that scenario, submit your local project documentation, screenshots, and interactive HTML replica (`PowerBI_Interactive_Dashboard.html`), which reproduces 100% of the interactive functionality in any web browser.
