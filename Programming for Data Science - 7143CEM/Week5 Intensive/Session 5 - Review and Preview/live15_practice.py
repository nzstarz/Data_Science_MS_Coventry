# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 21:05:29 2022

@author: USER
"""

# 10 Pandas
# Penguin Dataset
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

df.head()

df

df['species'].unique()

df.describe()

df['species'].describe()
df['species'].value_counts()
df['island'].value_counts()

df['bill_length_mm'].describe()

plt.figure()
df[['bill_length_mm', 'flipper_length_mm' ]].plot.box()
plt.show()


df1 = df.pivot(columns='species', values='bill_length_mm')
print(df1)
plt.figure()
df1.plot.box()
plt.show()



plt.figure()
df.boxplot(by='species', column=['bill_length_mm','flipper_length_mm'])
plt.show()

import seaborn as sns
plt.figure()
sns.boxplot(data=df, y='species', x='bill_length_mm')
plt.show()


df2 = df.query("island=='Dream'")
df2['species'].value_counts()
df3 = df2.groupby('species')
df3['bill_length_mm'].mean()
df3.mean()

