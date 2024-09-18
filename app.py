import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'bin/st_data.csv'

try:
    data = pd.read_csv(file_path)
    print("Data from CSV:\n", data.head())
except FileNotFoundError:
    print(f"Error: The file at path {file_path} was not found.")
    exit()

data.columns = ['Date', 'Revenue A', 'Revenue B', 'Revenue C']

print("\nMissing Data Check:\n", data.isnull().sum())

numeric_data = data.drop(columns=['Date'])
numeric_data.fillna(numeric_data.mean(), inplace=True)

data['Date'] = pd.to_datetime(data['Date'])

data.set_index('Date', inplace=True)

print("\nBasic Statistics:\n", numeric_data.describe())

total_sales = numeric_data.sum()
print("\nTotal Sales:\n", total_sales)

sales_change = numeric_data.pct_change()
print("\nSales Change:\n", sales_change)

average_sales = numeric_data.mean()
print("\nAverage Sales:\n", average_sales)

plt.figure(figsize=(14, 7))

plt.subplot(2, 2, 1)
data.plot(kind='line', y=['Revenue A', 'Revenue B', 'Revenue C'], ax=plt.gca(), marker='o')
plt.title('Monthly Revenue Trends')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.legend(loc='best')

plt.subplot(2, 2, 2)
sales_change.plot(kind='line', ax=plt.gca(), marker='x')
plt.title('Monthly Sales Change (%)')
plt.xlabel('Date')
plt.ylabel('Percentage Change')
plt.legend(loc='best')

plt.subplot(2, 2, 3)
average_sales.plot(kind='bar', ax=plt.gca())
plt.title('Average Monthly Revenue')
plt.xlabel('Product')
plt.ylabel('Average Revenue')

plt.subplot(2, 2, 4)
sns.heatmap(sales_change, annot=True, cmap='coolwarm', fmt=".2%", cbar=True)
plt.title('Sales Change Heatmap')

plt.tight_layout()
plt.show()

if numeric_data.isnull().values.any():
    print("Error: Numeric columns contain NaN values.")
else:
    print("Data clean and ready for further analysis.")