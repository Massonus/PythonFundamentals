import pandas as pd

data = pd.read_csv('../pandas_numpy_guide/sales.csv')

data.dropna(inplace=True)

data['SalesRevenue'] = data['Quantity'] * data['UnitPrice']

sales = data.groupby('Category')['SalesRevenue'].sum().nlargest(3)
# print(sales)

avg_rate = data.groupby('Category')['Rating'].mean()

print(avg_rate)
