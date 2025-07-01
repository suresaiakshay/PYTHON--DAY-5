import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV using Pandas
try:
    df = pd.read_csv("C:\\Users\\SURE SAI AKSHAY\\Desktop\\Sales_Report_January_2023.csv")
    print("CSV loaded successfully!")
except FileNotFoundError:
    print("File not found. Creating sample data...")
    data = {
        'Date': pd.date_range('2023-01-01', periods=30).strftime('%Y-%m-%d'),
        'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'] * 7 + ['Laptop', 'Phone'],
        'Region': ['North', 'South'] * 15,
        'Sales': [round(x, 2) for x in np.random.uniform(100, 1000, 30)]
    }
    df = pd.DataFrame(data)
    df.to_csv('sample_sales_data.csv', index=False)
    df = pd.read_csv('sample_sales_data.csv')

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 2. Basic analysis using groupby(), sum(), and plot()

# Sales by Product
print("\nSales by Product:")
product_sales = df.groupby('Product')['Sales'].sum()
print(product_sales)

# Plot sales by product
product_sales.plot(kind='bar', title='Total Sales by Product', 
                   ylabel='Sales Amount', xlabel='Product', figsize=(8,4))
plt.show()

# Sales by Region
print("\nSales by Region:")
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# Plot sales by region
region_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Region',
                 figsize=(6,6))
plt.show()

# Monthly Sales (assuming Date column exists)
if 'Date' in df.columns:
    df['Month'] = pd.to_datetime(df['Date']).dt.month_name()
    monthly_sales = df.groupby('Month')['Sales'].sum()
    
    print("\nMonthly Sales:")
    print(monthly_sales)
    
    monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend',
                      ylabel='Sales', xlabel='Month', figsize=(8,4))
    plt.show()