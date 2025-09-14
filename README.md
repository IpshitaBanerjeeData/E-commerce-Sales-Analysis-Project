# E-commerce Sales and Customer Analysis

### Project Overview
This project provides an end-to-end analysis of a year-long e-commerce sales dataset. It demonstrates a full data analysis lifecycle, from data cleaning and transformation to business intelligence visualization. The primary goal was to uncover key sales trends and customer behaviors to inform business strategy.

### Raw Data
The dataset used for this analysis is available for download at the following link:
(https://archive.ics.uci.edu/dataset/352/online+retail)

### Tools & Technologies
* **Python:** Used for initial data cleaning and creating the SQLite database.
    * `pandas` for data manipulation.
    * `sqlite3` for database management.
* **SQL:** Used for data querying and advanced analysis (RFM analysis).
* **Tableau:** Used for designing a professional and interactive dashboard.

### Key Findings
* **Overall Sales Performance:** The analysis of over 540,000 sales records revealed a total revenue of **$8.3 million**.
* **Top Products:** The "REGENCY CAKESTAND 3 TIER" was identified as the highest-performing product, generating over **$132,000** in sales.
* **Geographic Analysis:** The United Kingdom accounts for over **81%** of all sales, highlighting a significant market concentration.
* **Customer Segmentation:** A customer segmentation analysis identified key customer groups based on their recency, frequency, and monetary value, allowing for targeted marketing strategies.

### Repository Contents
* `analysis_script.py`: The Python script used for data cleaning and loading the data into the database.
* `queries.sql`: A file containing all the SQL queries used to perform the analysis.
* `Sales_Book.twb`: The Tableau workbook file.
* `screenshots/`: A folder containing screenshots of the final dashboard and key visualizations.

### View the Live Dashboard
Click here to view the interactive dashboard on Tableau Public:
(https://public.tableau.com/app/profile/ipshita.banerjee/viz/Sales_Book_17577915273040/E-commerceSalesCustomerAnalysisDashboard)
