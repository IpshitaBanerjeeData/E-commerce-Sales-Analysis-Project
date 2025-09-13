-- Overall Sales Performance
SELECT SUM(TotalSales) AS TotalRevenue FROM sales_data;

-- Top 10 Products
SELECT Description, SUM(TotalSales) AS TotalSales FROM sales_data GROUP BY Description ORDER BY TotalSales DESC LIMIT 10;

-- Top 5 Countries
SELECT Country, SUM(TotalSales) AS TotalSales FROM sales_data GROUP BY Country ORDER BY TotalSales DESC LIMIT 5;

SELECT
    CustomerID,
    -- Recency: Days since the last purchase
    JULIANDAY('now') - MAX(JULIANDAY(InvoiceDate)) AS Recency,
    -- Frequency: Total number of unique purchases
    COUNT(DISTINCT InvoiceNo) AS Frequency,
    -- Monetary: Total sales value
    SUM(TotalSales) AS Monetary
FROM
    sales_data
GROUP BY
    CustomerID
ORDER BY
    Monetary DESC;