
# 7143CEM Programming for Data Science
# Live coding -- Week 3 -- Thursday (part one)

# Data Visualisation

#---
# 1. Recap: numpy/pandas
# * numpy arrays, behave like lists, but also have
#   mathematics, add, sum, apply universal functions
#   think vector operations
# * random.randint(1,6) includes 6
#   but np.random.randint(1,6) does not include 6
# * slice never include the right number,
#   so 4:8 means 4 upt to 8 not including 8
#   be careful about copy vs view
# * random.choice(['red','green','blue'])
# * numpy arrays are order and mutable (like list)
# * numpy array has a dtype (all elements same type)
#   be careful about overflow
#---
# * pandas Series (1D array, can only have 1 column)
#   like numpy arrays (index initially 0,1,2,3)
#     take slices, remember the index is preserved
#     add, but only for the common indices (otherwise NaN)
#   like dictionary, index could be anything immutable
#     so could be tuple, number, string
#   pandas calls both index and key the same (called index)
#   use iloc for row numbers 0,1,2,...
#   use loc for "keys" (default one)
#   can plot itself: s.plot.line() <-- pandas plotting
#   matplotlib is OLDER than pandas
# * pandas DataFrame (2D array, rows and columns)
#   loc and iloc work to select rows
#   generally we use [['name','height']] to select columns
#   generally use query to filter out rows
#   groupby(somevariable) internally organises the rows
#     into groups by the values in that variable
#     kind of invisible when printing (all internal)
#     gap.groupby('continent')
#   apply a summary function to a column
#     fish.groupby('species').length.mean()
#   set_index -- move only (or more) columns to the index
#   reset_index -- move the index columns to be normal columns
#---
# * aiming for DataFrame in, DataFrame out
#     but sometimes we get a Series out (be careful)
# * pandas is generally good at choosing dtypes
# * e.g. when using pd.read_csv()


#---
# Explain view vs copy

import numpy as np
A = np.array(['cricket','football','squash','hockey','kabbadi'])
print(A)
B = A[3:]
print(B)
B[1] = 'skiing'
print(B)
print(A) # telling us that B is a view into A
# any changes to B will also change A

# To avoid this
print('---')
A = np.array(['cricket','football','squash','hockey','kabbadi'])
print(A)
B = A[3:].copy()
print(B)
B[1] = 'skiing'
print(B)
print(A) # telling us that B was a copy of slice from A

# What to come back to:
#   reset_index


#---
# 2. Pivot tables, pandas plots
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

import pandas as pd
import matplotlib.pyplot as plt

bigbaby = pd.read_csv('babynames.csv')
print(bigbaby.shape)
print(bigbaby)
# each row has both name and year
# called "narrow" format data
#  (good for computers, not great for humans)

q1 = "((Name=='Emma') and (Gender=='F'))"
AAA = bigbaby.query(q1)
q2 = "((Name=='Charles') and (Gender=='M'))"
BBB = bigbaby.query(q2)

print(AAA)
plt.figure()
AAA.plot.line('Year','Babies')
BBB.plot.line('Year','Babies')
plt.show()
# pandas plotting, labels x-axis (Year)
#   legend box (Babies)

# What we need is a table with
# rows for each year
# and columns for each name
# called "wide" format data
#   (good for humans, not great for computers)

print(q1)
print(q2)
Q = q1+' or '+q2
print(Q)
CCC = bigbaby.query(Q)
print(CCC)
# only want Name for column names
#           Year for row names (index)
#           Babies for the values
EEE = CCC.pivot(index='Year', columns='Name', values='Babies')
print(EEE)

plt.figure()
EEE.plot.line()
plt.show()

# Don't try this at home ...
# GGG = bigbaby.query("Gender=='F'")
# FFF = GGG.pivot(index='Year', columns='Name', values='Babies')
# plt.figure()
# FFF.plot.line()
# plt.show()


# Break time: come back at 12:00 noon


# The opposite of pivot is melt
#   narrow->wide is pivot
#   wide>-narrow is melt


#---
# 3. Summary statisics, boxplots
print(EEE)
print(EEE.describe())
# five-number summary (distribution of values):
#   min, lower quartile (LQ), median, upper quartile (UQ), max
# median is middle value, 50% of values <= median
# LQ is value where 25% of values <= LQ
# UQ is value where 75% of values <= UQ
# min is 0% of values <= min
# max is 100% of values <= max
#   0%, 25%, 50%, 75%, 100%
print(EEE['Charles'].mean())
print(EEE['Charles'].sum() / EEE['Charles'].count())

print(EEE['Charles'].std()) # standard deviation
m = EEE['Charles'].mean()
s = np.sqrt( ( (EEE['Charles']-m)**2 ).sum() /
             (EEE['Charles'].count()-1))
print(s)

print(EEE)

plt.figure()
EEE.plot.box()
plt.show()
print(EEE.describe())
# For Emma you see alot of outliers (dots)
uq = 4364.5
lq = 1588.75
# inter-quartile range
iqr = uq - lq
print(iqr)
upper_fence = uq + 1.5*iqr
print('Emma upper fence:',upper_fence)
lower_fence = lq - 1.5*iqr
print(lower_fence)
# everything above upper_fence is drawn with a dot ("outlier")
# everything below lower_fence is dot ("outlier")
# When there are outliers, the top of whisker is highest
#   values <= upper_fence



#---
# 4. Install plotting libraries on Anaconda
# -- seaborn, plotnine, plotly
#    see the instructions on Aula

#---
# 5. Python graph gallery
# https://www.python-graph-gallery.com/
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html


#---
# 6. Sources of data (kaggle, 538, UCI, seaborn)
# Kaggle: kaggle.com
# UCI: https://archive.ics.uci.edu/ml/index.php
# Google trends: https://trends.google.com/
# 538 website: https://fivethirtyeight.com/

# Article:
# https://fivethirtyeight.com/features/some-people-are-too-superstitious-to-have-a-baby-on-friday-the-13th/

import pandas as pd
url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv'
birth = pd.read_csv(url)
print(birth)
# 1 Jan 2000 was Saturday (day_of_week=6)
# So Friday is day_of_week 5
print(birth.describe())

# Write a query to pick out all the Fridays
AAA = birth.query("day_of_week==5")
print(AAA)

# Write a query to pick out all the Friday 13th
BBB = birth.query("(day_of_week==5) and (date_of_month==13)")

print(BBB)
# or
CCC = AAA.query("date_of_month==13")
print(CCC)

print('mean Fri 13:',BBB.births.mean())
print('mean Fri 13:',CCC.births.mean())
print('mean Fri:',AAA.births.mean())

# Homework: read article, and write down the question they
#           are trying to answer in their own plot


# Longer break: come back at 2pm


# -- continued in next Python file --
