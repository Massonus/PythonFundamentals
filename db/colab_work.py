import pandas as pd
import numpy as np

data = pd.read_csv('../pandas_numpy_guide/data.csv')

print(data['Number of bytes'].sum())
print(data['Number of bytes'].mean())
print(data.groupby('Country')['Number of bytes'].sum().idxmax())
print(data.groupby('Username')['Number of bytes'].sum().nlargest(3))
print(data.loc[data['Country'] == ' Ukraine', 'Number of bytes'].sum())
print(len(data['Username'].unique()))
print(data.loc[data['Country'] == ' Ukraine', 'Number of bytes'].mean() - data.loc[
    data['Country'] == ' UK', 'Number of bytes'].mean())
mean = data.groupby('IP')['Number of bytes'].sum()
print(np.mean(mean))
print(data['Country'].unique())
