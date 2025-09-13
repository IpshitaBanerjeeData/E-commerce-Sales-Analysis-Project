import pandas as pd
import sqlite3

# Load the Excel file from Google Sheets into a pandas DataFrame
df = pd.read_excel('Online Retail.xlsx')

# --- Data Cleaning & Pre-processing ---
# Remove rows with missing CustomerID
df.dropna(subset=['CustomerID'], inplace=True)

# Convert Quantity and UnitPrice to correct numeric types
# Coerce errors will set invalid parsing to NaT, which is handled by dropna
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Drop rows with missing values after type conversion
df.dropna(inplace=True)

# Create a 'TotalSales' column
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# --- Save Cleaned Data to CSV ---
# This will create a file named 'cleaned_sales_data.csv' in your project folder
df.to_csv('cleaned_sales_data.csv', index=False)
print("Cleaned data successfully saved to 'cleaned_sales_data.csv'")

# --- Load to SQLite Database (for analysis) ---
conn = sqlite3.connect('sales_data.db')
df.to_sql('sales_data', conn, if_exists='replace', index=False)
conn.close()
print("Data also loaded into 'sales_data.db' for analysis.")