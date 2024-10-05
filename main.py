import pandas as pd
import numpy as np
# import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

dataframe = {
    'Name':'',
    'Age':'',
    'City':''
    }
data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
    }
df = pd.DataFrame(data)
print(df)
dfcsv = pd.read_csv('World-happiness-report-2024.csv')
print(dfcsv.head(10))
print(dfcsv.info())
print('describe ',dfcsv.describe())
# print('columns ',dfcsv.columns)
print(dfcsv.loc[dfcsv['Healthy life expectancy'] > 0.7])

animals = pd.read_csv('animal.csv')
print(animals)
print(animals.info())
animals.fillna(0, inplace=True)
print(animals)
print('---')
group = animals.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

