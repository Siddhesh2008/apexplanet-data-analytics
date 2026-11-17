
SELECT *
FROM ecommerce_transactions
LIMIT 5;

SELECT DISTINCT country
FROM ecommerce_transactions;

SELECT COUNT(*)
FROM ecommerce_transactions;

SELECT *
FROM ecommerce_transactions
ORDER BY purchase_amount DESC
LIMIT 10;

SELECT *
FROM ecommerce_transactions
ORDER BY purchase_amount ASC
LIMIT 10;

SELECT *
FROM ecommerce_transactions
ORDER BY transaction_date ASC
LIMIT 5;

-- Calculate total revenue for each country
SELECT
    country,
    SUM(purchase_amount) AS total_revenue
FROM public.ecommerce_transactions
GROUP BY country
ORDER BY total_revenue DESC;

-- Select each country
SELECT
    country,

    -- Calculate total revenue for each country
    SUM(purchase_amount) AS total_revenue

-- Read data from our transactions table
FROM public.ecommerce_transactions

-- Group transactions by country
GROUP BY country

-- Keep only countries whose total revenue exceeds 15 million
HAVING SUM(purchase_amount) > 15000000

-- Sort the remaining countries by highest revenue
ORDER BY total_revenue DESC;

SELECT
    payment_method,
    COUNT(*) AS total_transactions

FROM public.ecommerce_transactions

-- Group transactions by payment method
GROUP BY payment_method

-- Keep only methods with more than 8,300 transactions
HAVING COUNT(*) > 8300

-- Sort by transaction count, highest first
ORDER BY total_transactions DESC;

-- Display transactions whose purchase amount is above average
SELECT *
FROM public.ecommerce_transactions

-- Compare each transaction against the overall average
WHERE purchase_amount > (

    -- Calculate the average purchase amount
    SELECT AVG(purchase_amount)
    FROM public.ecommerce_transactions

);

-- Select the transaction details
SELECT
    user_name,
    country,
    purchase_amount,

    -- Assign a sequential number to each transaction
    -- Highest purchase amount gets number 1
    ROW_NUMBER() OVER (
        ORDER BY purchase_amount DESC
    ) AS row_num

-- Read data from our transactions table
FROM public.ecommerce_transactions

-- Display only the first 10 results
LIMIT 10;

SELECT
    user_name,
    country,
    purchase_amount,

    -- Restart numbering separately for each country
    ROW_NUMBER() OVER (
        PARTITION BY country
        ORDER BY purchase_amount DESC
    ) AS country_rank

FROM public.ecommerce_transactions;

-- Rank transactions separately within each country
SELECT
    user_name,
    country,
    purchase_amount,

    RANK() OVER (
        PARTITION BY country
        ORDER BY purchase_amount DESC
    ) AS country_rank

FROM public.ecommerce_transactions

-- Show the first 20 rows
LIMIT 20;

-- Compare each transaction with the previous transaction
SELECT
    transaction_date,
    user_name,
    purchase_amount,

    -- Get the purchase amount from the previous row
    LAG(purchase_amount) OVER (
        ORDER BY transaction_date
    ) AS previous_purchase

FROM public.ecommerce_transactions

-- Display the first 10 rows
ORDER BY transaction_date
LIMIT 10;

-- Compare each transaction with the next transaction
SELECT
    transaction_date,
    user_name,
    purchase_amount,

    -- Get the purchase amount from the next row
    LEAD(purchase_amount) OVER (
        ORDER BY transaction_date
    ) AS next_purchase

FROM public.ecommerce_transactions

-- Display the first 10 rows
ORDER BY transaction_date
LIMIT 10;

-- Create a reusable view showing revenue by country
CREATE VIEW country_revenue AS
SELECT
    country,
    COUNT(*) AS total_transactions,
    SUM(purchase_amount) AS total_revenue,
    AVG(purchase_amount) AS average_purchase
FROM public.ecommerce_transactions
GROUP BY country;

-- Retrieve the existing country revenue view
SELECT *
FROM public.country_revenue
ORDER BY total_revenue DESC;

-- Read data from the existing view
SELECT *
FROM public.country_revenue
ORDER BY total_revenue DESC;

