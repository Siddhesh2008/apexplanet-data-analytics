# 🗄️ Task 2: PostgreSQL Relational Database Analytics — E-Commerce Dataset

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-336791.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red.svg)](https://www.sqlalchemy.org/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458.svg)](https://pandas.pydata.org/)
[![Internship](https://img.shields.io/badge/Internship-ApexPlanet%20Solutions-orange.svg)](#-internship-context)

Master repository module for **Task 2: SQL & Relational Database Analytics** of the **ApexPlanet Data Analytics Internship**.

---

## 📌 Internship Context
- **Organization:** **ApexPlanet Solutions**
- **Internship Role:** Data Analytics Intern
- **Project Scope:** **Task 2: Relational Schema Modeling & SQL Business Analytics (Days 8–14)**
- **Author:** Siddhesh (1st Year B.Tech in Artificial Intelligence & Data Science)
- **Database:** PostgreSQL (`apexplanet_analytics`)
- **Dataset:** 50,000 Global E-Commerce Records (\$25.16M Gross Sales)

---

## 🎯 Task 2 Objectives
1. **Relational Database Design:** Architect a normalized PostgreSQL table schema with proper data types (`INT`, `VARCHAR`, `NUMERIC`, `TIMESTAMP`) and primary key integrity.
2. **Automated Pipeline Ingestion:** Build an automated SQLAlchemy/psycopg2 ingestion pipeline loading 50,000 transaction records from CSV into PostgreSQL.
3. **Core Business Aggregations:** Author SQL queries utilizing `SUM`, `AVG`, `COUNT`, `MIN`, and `MAX` to compute enterprise financial benchmarks.
4. **Grouped Multi-Dimensional Analytics:** Leverage `GROUP BY` and `HAVING` filters across Product Categories, Geographic Territories, and Payment Methods.
5. **Advanced Analytical Window Functions:** Implement `ROW_NUMBER()`, `RANK()`, and partitioned aggregates for customer lifetime expenditure ranking.
6. **Temporal Trend Analysis:** Execute `DATE_TRUNC()` monthly time-series queries to monitor sales velocity and seasonal volume.

---

## 📁 Repository & Folder Structure

```text
task_2_sql_database/
├── data/
│   └── ecommerce_transactions.csv                      # Source data for SQL table ingestion (50,000 records)
├── scripts/
│   ├── ecommerce.sql                                   # Complete DDL schema & analytical SQL query suite
│   ├── db_utils.py                                     # Modular Python SQLAlchemy connection & query execution utility
│   └── db_utils.ipynb                                  # Interactive database connection test notebook
├── notebooks/
│   ├── Task_2_Postgres_Analytics.ipynb                 # Master executed Jupyter Notebook running queries via Python
│   ├── Postgres.ipynb                                  # Original PostgreSQL exploration notebook
│   └── db_utils.py                                     # Local importable utility module
├── reports/
│   └── Task_2_Summary.md                               # Executive SQL & Database Analytics Summary Report
├── requirements.txt                                    # Environment dependencies (SQLAlchemy, psycopg2-binary)
└── README.md                                           # Comprehensive documentation & Viva Voce defense guide
```

---

## 🏗️ Database Schema & DDL Definition

```sql
CREATE DATABASE apexplanet_analytics;

\c apexplanet_analytics;

CREATE TABLE IF NOT EXISTS public.ecommerce_transactions (
    transaction_id INT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18 AND age <= 100),
    country VARCHAR(100) NOT NULL,
    product_category VARCHAR(100) NOT NULL,
    purchase_amount NUMERIC(10, 2) NOT NULL CHECK (purchase_amount > 0),
    payment_method VARCHAR(50) NOT NULL,
    transaction_date TIMESTAMP WITHOUT TIME ZONE NOT NULL
);

-- Indexing for Query Performance
CREATE INDEX idx_country ON public.ecommerce_transactions(country);
CREATE INDEX idx_category ON public.ecommerce_transactions(product_category);
CREATE INDEX idx_date ON public.ecommerce_transactions(transaction_date);
CREATE INDEX idx_user ON public.ecommerce_transactions(user_name);
```

---

## 💻 Sample SQL Analytical Queries

### 1. Top 5 Product Categories by Revenue
```sql
SELECT
    product_category,
    COUNT(*) AS total_transactions,
    ROUND(SUM(purchase_amount), 2) AS total_revenue
FROM public.ecommerce_transactions
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 5;
```

### 2. Geographic Revenue Breakdown & Average Ticket Size
```sql
SELECT
    country,
    COUNT(*) AS total_orders,
    ROUND(SUM(purchase_amount), 2) AS total_revenue,
    ROUND(AVG(purchase_amount), 2) AS average_order_value
FROM public.ecommerce_transactions
GROUP BY country
ORDER BY total_revenue DESC;
```

### 3. VIP Customer Spending Ranking using Window Functions
```sql
SELECT
    user_name,
    COUNT(*) AS total_transactions,
    ROUND(SUM(purchase_amount), 2) AS total_spent,
    ROW_NUMBER() OVER (ORDER BY SUM(purchase_amount) DESC) AS rank
FROM public.ecommerce_transactions
GROUP BY user_name
ORDER BY total_spent DESC
LIMIT 10;
```

---

## ⚙️ How to Setup & Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Database Connection:**
   Ensure PostgreSQL is running locally and update `scripts/db_utils.py` or set environment variables:
   ```bash
   export DB_USER=postgres
   export DB_PASS=your_password
   export DB_HOST=localhost
   export DB_PORT=5432
   export DB_NAME=apexplanet_analytics
   ```

3. **Ingest Dataset into PostgreSQL:**
   ```bash
   python -c "from scripts.db_utils import ingest_csv_to_postgres; ingest_csv_to_postgres()"
   ```

4. **Execute Analytics Notebook:**
   ```bash
   jupyter lab notebooks/Task_2_Postgres_Analytics.ipynb
   ```

---

## 🎓 Viva Voce Technical Defense Guide (15+ Q&A)

### Q1: Why use `NUMERIC(10, 2)` instead of `FLOAT` or `REAL` for financial data in PostgreSQL?
**Answer:** `FLOAT` and `REAL` use binary floating-point representation (IEEE 754), which introduces precision and rounding errors during arithmetic calculations. `NUMERIC(10, 2)` uses exact fixed-point decimal arithmetic, ensuring financial compliance and exact cent calculations.

### Q2: What is the operational difference between `WHERE` and `HAVING` in SQL?
**Answer:** `WHERE` filters individual rows **before** any aggregation takes place and cannot reference aggregate functions. `HAVING` filters aggregated groups **after** `GROUP BY` has evaluated aggregate functions (e.g., `HAVING SUM(purchase_amount) > 100000`).

### Q3: What is the purpose of `DATE_TRUNC('month', transaction_date)`?
**Answer:** `DATE_TRUNC` rounds a timestamp down to the specified precision (e.g., the first day of that month at 00:00:00). This enables grouping continuous timestamp records into discrete calendar months for time-series trend analysis.

### Q4: Explain the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`.
**Answer:**
- `ROW_NUMBER()` assigns a consecutive integer to every row regardless of ties (1, 2, 3, 4).
- `RANK()` assigns identical numbers to tied values and skips the subsequent rank (1, 2, 2, 4).
- `DENSE_RANK()` assigns identical numbers to tied values without skipping ranks (1, 2, 2, 3).

### Q5: What is an index in PostgreSQL, and how does it speed up queries?
**Answer:** An index (commonly B-Tree in PostgreSQL) is a separate data structure that stores column values and pointers to rows in sorted order. It allows the database engine to search in logarithmic time $O(\log n)$ rather than scanning the entire table sequentially $O(n)$.

### Q6: What is connection pooling in SQLAlchemy?
**Answer:** Establishing a new database handshake is resource-intensive. A connection pool maintains an active pool of open database connections that can be reused across queries, significantly boosting throughput and efficiency.

### Q7: Why is `CHECK (purchase_amount > 0)` included in the table DDL?
**Answer:** It enforces domain integrity at the database layer, preventing invalid or negative purchase transactions from entering the system even if application-level validation fails.

### Q8: What does `LIMIT` do, and why should it always be paired with `ORDER BY`?
**Answer:** `LIMIT` restricts the number of rows returned by the query. Without an `ORDER BY` clause, the order of returned rows is non-deterministic (arbitrary), meaning the results cannot be reliably interpreted as "top" or "bottom".

### Q9: How does `psycopg2` interact with SQLAlchemy?
**Answer:** SQLAlchemy is an Object Relational Mapper (ORM) and SQL abstraction toolkit, while `psycopg2` is the underlying low-level C-based PostgreSQL DBAPI driver that handles actual socket communication and protocol wire formatting with PostgreSQL.

### Q10: How do you handle database transactions to avoid partial writes?
**Answer:** By wrapping write operations in a transaction block (`BEGIN ... COMMIT / ROLLBACK`). In SQLAlchemy, using context managers (`with engine.begin() as conn:`) ensures that if an error occurs, the entire transaction is rolled back automatically (atomicity).

---

## 👤 Author
- **Intern:** Siddhesh
- **Role:** Data Analytics Intern, ApexPlanet Solutions
- **Academic Discipline:** B.Tech in Artificial Intelligence & Data Science
