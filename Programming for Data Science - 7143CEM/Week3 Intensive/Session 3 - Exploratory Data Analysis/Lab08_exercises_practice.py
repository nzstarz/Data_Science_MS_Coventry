import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fruit = pd.read_csv('E:\\Data Science\\Coventry\\Programming for Data Science - 7143CEM\\Week3 Intensive\\Session 3 - Exploratory Data Analysis\\fruit.csv')
print(fruit.shape)

print(fruit)
# a

f_unique=fruit.item.unique()
print(f_unique)
print(len(f_unique))

print(fruit.country.unique())

# b

print(fruit)

spain_rows = fruit.query("country == 'Spain'")
spain_items = spain_rows['item']
## print(spain_items)

spain_set = set(spain_items)
print(spain_set)

UK_rows = fruit.query("country == 'UK'")
UK_items = UK_rows['item']

## print(UK_items)
UK_set = set(UK_items)
print(UK_set)

# print Common Items
common_items =  set.intersection(spain_set, UK_set)
print(common_items)

# or

common_items = spain_set.intersection(UK_set)
print(common_items)

# or

common_items = UK_set.intersection(spain_set)
print(common_items)

# or
try_it = set(spain_items).intersection(set(UK_items))
print(try_it)

# c


df = fruit.query("year==2019")
print(df.shape)
print(df)

df1 = df.groupby(['country'])
print(df1['area'].sum())

df2 = df.groupby(['country','item'])
print(df2['area'].sum().sort_values(ascending=False))

# d

AAA = fruit.query( "item=='Strawberries'" )
print(AAA)
BBB = AAA.pivot(index= 'year', columns= 'country' , values= 'yield')
print(BBB)

CCC = BBB.reset_index()
print(CCC)

print(AAA.year.unique())
print(AAA['yield'].max())
print(AAA['yield'].min())


# yield is a key word in Python

plt.figure()
CCC.plot.line(x='year', y = ['Spain', 'UK'])
plt.ylabel('yield(kg/hectare')
plt.show()


# e

UK_rows = fruit.query("country == 'UK'")


DDD = UK_rows.pivot(index= 'year', columns= 'item' , values= 'yield')
print(DDD)

plt.figure()
DDD.plot.box(rot = 60)


plt.title('Fruit yield in the UK')
# plt.xticks(rotation=45)
plt.show()


plt.figure()
UK_rows.boxplot(column ='yield', by ='item', rot =60)
plt.title('Fruit yield in the UK')
plt.suptitle('')
plt.show()

# Try Seaborn
sns.set_style('darkgrid')
#Seaborn Themes: dark, darkgrid, whitegrid, white, ticks
plt.figure()
ax = sns.boxplot(x = 'item', y = 'yield', data = UK_rows)
ax.set_title('Fruit yield in the UK')
ax.set_xticklabels(ax.get_xticklabels(), rotation=60)
ax.set_ylabel('yield(kg/hectare)')
ax.set_xlabel('category of fruit')
plt.show()
