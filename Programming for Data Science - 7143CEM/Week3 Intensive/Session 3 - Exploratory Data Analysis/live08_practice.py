import pandas as pd
import matplotlib.pyplot as plt


import pandas as pd
bigbaby = pd.read_csv('E:\\Data Science\\Coventry\\Programming for Data Science - 7143CEM\\Week3 Intensive\\Session 2 - Introduction to Pandas\\babynames.csv')
print(bigbaby)

print('Total=',bigbaby.Babies.sum()) # 340 million babies

AA = bigbaby.groupby('Gender')
print(AA.Babies.sum()) # sum of each group

BB = bigbaby.groupby('Year')
CC = BB.Babies.sum()
print(CC)
print(type(CC))

plt.figure()
CC.plot.line()
plt.show()




import gapminder
gap = gapminder.gapminder
print(gap)
# alternatively
gap = pd.read_csv("https://raw.githubusercontent.com/OHI-Science/data-science-training/master/data/gapminder.csv")
print(gap)
# or another way

## gap = pd.read_csv('gapminder.csv')
## print(gap)

## pwd

print(gap.columns)
print(list(gap.columns))
print(gap.country.describe())

print(gap.year.describe())
print(gap.year.unique())
print(gap.continent.describe())
print(gap.continent.unique())

print(gap.describe())

gapsub = gap.query("year==1987")
print(gapsub.shape)

print(gapsub)

print(gapsub['pop'].sum())

AAA = gap.groupby('year')
BBB = AAA['pop'].sum()
print(BBB)

# or
print(gap.groupby('year')['pop'].sum())
plt.figure()
BBB.plot.line()
plt.show()

CCC = gapsub.groupby('continent')
PP = CCC['pop'].sum()
print(PP)

plt.figure()
PP.plot.bar()
plt.show()

DDD = gap.groupby(['year', 'continent'])
EEE = DDD['pop'].sum()
print(EEE)



print(EEE[1997]['Europe'])


FFF = EEE.reset_index()
print(FFF)
GGG = FFF.query("(year==1997) and (continent=='Europe')")
print(GGG)

HHH = (gap.
           groupby(['year', 'continent'])['pop'].
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

## another one

plt.figure()
(gap.
     groupby(['continent','year'])['pop'].
     sum().
     loc['Oceania'].
     plot.line()
)
plt.show()

## Typical data query




