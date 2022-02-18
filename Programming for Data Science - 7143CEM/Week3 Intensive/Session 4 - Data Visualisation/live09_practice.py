import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


A = np.array(['cricket','football','squash','hockey','kabbadi'])
print(A)
B = A[3:]
print(B)
B[1] = 'sking'
print(B)
print(A)

print('-------')

A = np.array(['cricket','football','squash','hockey','kabbadi'])
print(A)
B = A[3:].copy()
print(B)
B[1] = 'sking'
print(B)
print(A)



bigbaby = pd.read_csv('E:\\Data Science\\Coventry\\Programming for Data Science - 7143CEM\\Week3 Intensive\\Session 4 - Data Visualisation\\babynames.csv')

print(bigbaby.shape)
print(bigbaby)

q1 = "(Name== 'Emma') and (Gender=='F')"
AAA = bigbaby.query(q1)

q2 = "(Name== 'Charles') and (Gender=='M')"
BBB = bigbaby.query(q2)


print(AAA)
plt.figure()
AAA.plot.line('Year', 'Babies')
BBB.plot.line('Year', 'Babies')

plt.show()

print(q1)
print(q2)
Q = q1 + ' or ' + q2
print(Q)

CCC = bigbaby.query(Q)
print(CCC)

EEE = CCC.pivot(index = 'Year', columns = 'Name', values='Babies')
print(EEE)

plt.figure()
EEE.plot.line()
plt.show()



GGG = bigbaby.query("Gender=='F'")
FFF = GGG.pivot(index = 'Year', columns = 'Name', values='Babies')
plt.figure()
FFF.plot.line()
plt.show()

# Thats was an stupid thing to do, dont try this

# Break Time 20mn : 5:40pm, 3rd february 2022 ; Came back at 6:00pm


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


print(EEE)
print(EEE['Charles'].count())
print(EEE['Charles'].mean())
print(EEE['Charles'].sum() / EEE['Charles'].count())


print(EEE)
print(EEE['Emma'].count())
print(EEE['Emma'].mean())
print(EEE['Emma'].sum() / EEE['Emma'].count())


print(EEE['Charles'].std())

m = EEE['Charles'].mean()
s = np.sqrt(((EEE['Charles'] - m)**2).sum() / 
            (EEE['Charles'].count() - 1))

print(s) # STD function explained

print(EEE)
plt.figure()
EEE.plot.box()
plt.show()
print(EEE.describe())

# For Emma
uq = 4364.5
lq = 1588.75

iqr = uq - lq
print(iqr)
upper_fence = uq + 1.5*iqr
print('Emma Upper Fence : ', upper_fence)
lower_fence = lq - 1.5*iqr
print('Emma Upper Fence : ', lower_fence)
# Working with outliers


# Some People Are Too Superstitious To Have A Baby On Friday The 13th(DataSet)
url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv'
birth = pd.read_csv(url)
print(birth)
print(birth.describe())
AA = birth.query("day_of_week == '5'")
print(AA)
BB = AA.query("date_of_month =='13'")
print(BB)

print('mean Fri 13:' , BB.births.mean())

print('mean Fri:' , AA.births.mean())




# Seaborn
import seaborn as sns
print(sns.__version__)


import gapminder
gap = gapminder.gapminder

# gap = pd.read_csv("https://raw.githubusercontent.com/OHI-Science/data-science-training/master/data/gapminder.csv")

print(gap)
# matplotlib
AA = gap.query("year==1992")
plt.figure()
plt.plot(AA['gdpPercap'], AA['lifeExp'],'.')
plt.show()

# pandas
plt.figure()
AA.plot.scatter('gdpPercap', 'lifeExp')
plt.show()

# seaborn

plt.figure()
sns.scatterplot(x='gdpPercap', y='lifeExp', data=AA, size = 'pop', hue = 'continent')
plt.xscale('log')
plt.title('Health vs Wealth (1992)')
plt.legend(bbox_to_anchor=(1,1))
plt.show()

# Animation

for y in range(1952,2008,5):
    q = "year=="+str(y)
    AA = gap.query(q)
    
    plt.figure()
    sns.scatterplot(x='gdpPercap', y='lifeExp', data=AA, size = 'pop', hue = 'continent')
    plt.xscale('log')
    plt.title('Health vs Wealth ('+str(y)+')')
    plt.legend(bbox_to_anchor=(1.01,1))
    plt.ylim(25, 85)
    plt.xlim(200,120000)
    plt.show() 
    
# End    