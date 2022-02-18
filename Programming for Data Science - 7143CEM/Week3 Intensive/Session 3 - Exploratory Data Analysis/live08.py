
# 7143CEM Programming for Data Science
# Live coding -- Week 3 -- Wednesday

# Exploratory Data Analysis (EDA)


#---
# 0. Modules (full-time)
#   Jan-Apr 2022: 7143CEM + 7144CEM
#   May-Aug 2022: 7071CEM + 7072CEM + 7086CEM + 7082CEM/7153CEM
#   Sep-Dec 2022: 7050CRB + 7150CEM
# Registry is checking each person


#---
# 1. Prof Hans Rosling
#    YouTube clip: https://www.youtube.com/watch?v=ahp7QhbB8G4
#    "200 Countries, 200 years, in four minutes: Joy of Stats"
# positives -- based on data, visually clear, colour=Continent,
#   story (highlighting some dates), interesting, engaging,
#   explained, happening live, jokes, personalised
# negatives -- names of countries missing, limited by one graph,
#   blob, country-based, implied future is good,
#   health/wealth as single numbers, inflation adjusted?
#   presentation rather than exploring 

# Anaconda prompt (or terminal on MacOs):
#   pip install gapminder
import gapminder


#---
# 2. Pandas recap
import pandas as pd
bigbaby = pd.read_csv('babynames.csv')
print(bigbaby)

# Note: for loops are very slow
#       output was not in a useful form for further processing
#       do not use for loops (except in emergency)

# Aim: live in the world of pandas
#      DataFrame in, DataFrame out

# Cheat sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

# One hugely useful idea:
print('Total=',bigbaby.Babies.sum()) # 340 million babies

AAA = bigbaby.groupby('Gender')
print(AAA.Babies.sum()) # sum of each group

BBB = bigbaby.groupby('Year')
CCC = BBB.Babies.sum()
print(CCC)
print(type(CCC))

import matplotlib.pyplot as plt
plt.figure()
CCC.plot.line()
plt.show()
# 1e6 is 1*10**6 (millions)


#---
# 3. Gapminder
import gapminder
gap = gapminder.gapminder
print(gap)
# alternatively:
gap = pd.read_csv("https://raw.githubusercontent.com/OHI-Science/data-science-training/master/data/gapminder.csv")
print(gap)
# or another option:
gap = pd.read_csv('gapminder.csv')
print(gap)


# Break time: come bac kat 4:15pm


print(gap.columns) # names of columns
print(list(gap.columns))
print(gap.country.describe()) # summary of country column
# 142 counties
print(gap.year.describe()) # from 1952 to 2007
print(gap.year.unique())   # jumps of 5 years
print(gap.continent.describe())
print(gap.continent.unique())

print(gap.describe()) # number variables summary
# numbers look like: 2.960121e+07
# means this: 29601210.000000000
# what about this: 2.960121e-07
# means this: 0.0000002960121
# scientific notation for numbers


# year 1987
#   query is used to pull out rows
#   makes a copy
gapsub = gap.query("year==1987")
print(gapsub.shape) # 142 counties in 1987

# Don't do this (boolean indexing)
#    gap[gap['year']==1987]

# Q: what is the population of the world?
print(gapsub)
#! print(gapsub.pop.sum())
# Huge coincidence 
#   pop is a special word in Python
print(gapsub['pop'].sum()) # 4.6 billion

AAA = gap.groupby('year')
BBB = AAA['pop'].sum()
print(BBB)

# This is Python
print(gap.groupby('year')['pop'].sum())

plt.figure()
BBB.plot.line()
plt.show()

# 1987 population by continent
CCC = gapsub.groupby('continent')
print(CCC['pop'].sum())

# population by continent
DDD = gap.groupby(['year','continent'])
EEE = DDD['pop'].sum()
print(EEE)

print(EEE[1997]['Europe'])

# set_index moves a column to the index
# reset_index moves the index to a column
FFF = EEE.reset_index()
print(FFF)
GGG = FFF.query("(year==1997) and (continent=='Europe')")
print(GGG) # DataTable with one row

# Magic ...
HHH = (gap.
         groupby(['year','continent'])['pop'].
         sum().
         reset_index().
         query("(year==1997) and (continent=='Europe')")
       )
print(HHH)

plt.figure()
(gap.
   groupby(['continent','year'])['pop'].
   sum().
   loc['Europe'].
   plot.line()
)
plt.show()


#---
# 4. Typical data query

# Break down a typical data operation
# imagine a DataFrame called fish
# (1) filter out rows from fish: A = fish.query(...)
# (2) arrange to rows into groups: B = A.groupby(...)
# (3) apply some aggregation of some column:
#      C = B['thecolumn'].max()
#      --> C is a summary table (not fish anymore)
#          the index of C is whether the groupby was
# (4) filter out rows from summary table: D = C.query(...)
# (5) either plot or select some columns from D


#---
# 5. Lab 07 Exercises
#    https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

# Question 1 -- Pandas vs Excel
#   More choice/customisation for plots in Pandas
#   Excel limited to about 1 million rows
#   Maybe use more complicated functions
#   Pandas should be faster
#   More formats for obtaining data
#   Its Python so can link up to other Python code
#   Pandas is free

# Question 2 -- msleep.csv
import pandas as pd
import matplotlib.pyplot as plt
msleep = pd.read_csv('msleep.csv')
print(msleep)

# (a)
print(msleep.shape) # tuple

# (b)
print(msleep['order'].nunique())
print(len(msleep['order'].unique()))
print(msleep['order'].value_counts().shape)
print(msleep['order'].describe()['unique'])
print(len(set(msleep['order'])))

# (c)
B = msleep['vore'].value_counts()
print(B)
C = msleep.groupby('vore').vore.count()
print(C)

plt.figure()
B.plot.barh()
plt.show()


# Anything to come back to tomorrow?
# -- group discussions
# -- groupby / aggregation
# -- gapminder

# -- the end --
