
# 7143CEM Programming for Data Science
# Live coding -- Week 3 -- Fun Friday (part one)

# Databases and Text Data

#---
# 0. Team joining code: 5l11d0w
    
#---
# 1. Portfolio Task 3

#---
# 2. Fruit harvest (Spain, UK) -- fruit.csv
# * break out groups


# Break time: come back at 12noon.


import pandas as pd
fruit = pd.read_csv('fruit.csv')
print(fruit)
print(fruit.shape) # attribute

# (a)
print(fruit['item'].nunique()) # method
print(fruit.item.nunique())
print(len(fruit.item.unique()))
print(fruit.item.describe()['unique'])
print(len(fruit.item.value_counts()))

# (b)
spain_rows = fruit.query("country=='Spain'")
spain_items = spain_rows['item']
#print(spain_items)
spain_set = set(spain_items)
print(spain_set)

uk_rows = fruit.query("country=='UK'")
uk_items = uk_rows['item']
#print(uk_items)
uk_set = set(uk_items)
print(uk_set)

# we have two Python sets
# stepped outside of pandas
# we want to intersect the two sets
common_items = set.intersection(spain_set,uk_set)
print(common_items)

common_items = spain_set.intersection(uk_set)
print(common_items)

try_it = set(spain_items).intersection(set(uk_items))
print(try_it)

# Forgotton how:
# another = pd.merge(spain_rows,uk_rows)
# Database join

# (c) 2019
YYY = fruit.query("year==2019")
print(YYY.year)

ZZZ = YYY.groupby('country')
print(ZZZ['area'].sum())

WWW = YYY.groupby('item')
TTT = WWW['area'].sum()
print(TTT.sort_values(ascending=False))
# Remember the pandas cheatsheet

# (d) Strawberries
import matplotlib.pyplot as plt
AAA = fruit.query("item=='Strawberries'")
print(AAA)
BBB = AAA.pivot(index='year',columns='country',values='yield')
print(BBB)
plt.figure()
BBB.plot.line()
plt.ylabel('yield (kg/hectare)')
plt.show()

CCC = BBB.reset_index()
print(CCC)
plt.figure()
CCC.plot.line(x='year', y=['Spain','UK'])
plt.ylabel('yield (kg/hectare)')
plt.show()

plt.figure()
CCC.plot.line()
plt.show()

# for yield make sure you use ['yield#] not .yield

# (e)
uk_rows = fruit.query("country=='UK'")
# want a table with one column for each fruit type
DDD = uk_rows.pivot(index='year',columns='item',values='yield')
print(DDD)

plt.figure()
DDD.plot.box(rot=60)
plt.title('Fruit yield in the UK')
# or this: plt.xticks(rotation=60)
plt.show()

# in pandas there are two ways to produce boxplot
# plot.box() is very primitive
# boxplot() is more sophisticated (don't need the pivot table)

plt.figure()
uk_rows.boxplot(column='yield', by='item', rot=60)
plt.title('Fruit yield in the UK')
plt.suptitle('')
plt.show()


# Break time: come back at 2pm (45 minutes)
    

import seaborn as sns
sns.set_style('darkgrid')
# darkgrid, whitegrid, dark, white, ticks

plt.figure()
ax = sns.boxplot(data=uk_rows, x='item', y='yield')
ax.set_title('Fruit yield in the UK')
ax.set_xticklabels(ax.get_xticklabels(),rotation=60)
ax.set_ylabel('yield (kg/hectare)')
ax.set_xlabel('category of fruit')
plt.show()

# Seaborn is good .. plotnine is amazing


# -- the end --
