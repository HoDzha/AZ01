import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(5))
print(df.info())
print(df.describe())
print('------------------------------------------------------------')
dz = pd.read_csv('dz.csv')

dzgroup = dz.groupby('City')['Salary'].mean()

print('Средняя зарплата по городам:')
print(dzgroup)
