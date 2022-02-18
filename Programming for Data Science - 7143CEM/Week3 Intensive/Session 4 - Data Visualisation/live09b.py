
# 7143CEM Programming for Data Science
# Live coding -- Week 3 -- Thursday (part two)

# Data Visualisation

# Longer break: come back at 2pm

#---
# 7. Introduction to seaborn
# https://www.mygreatlearning.com/blog/seaborn-tutorial/

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
print(sns.__version__)
# 0.11.2 -- 0 tells us "still in development"
# Character in the West Wing tv show
# Samuel Norman Seaborn (Rob Lowe actor)

import gapminder
gap = gapminder.gapminder
# or
# gap = pd.read_csv("https://raw.githubusercontent.com/OHI-Science/data-science-training/master/data/gapminder.csv")
print(gap)
# 1952 to 2007 in jumps of 5 years

AAA = gap.query("year==1992")

# matplotlib (Hans Rosling)
plt.figure()
plt.plot(AAA['gdpPercap'],AAA['lifeExp'],'.')
plt.show()

# pandas
plt.figure()
AAA.plot.scatter('gdpPercap','lifeExp')
plt.show()
# https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.plot.scatter.html

# seaborn
plt.figure()
sns.scatterplot(data=AAA,x='gdpPercap',y='lifeExp',
                size='pop',hue='continent')
plt.xscale('log')
plt.title('Health vs Wealth (1992)')
plt.legend(bbox_to_anchor=(1,1))
plt.show()

# Animation
for y in range(1952,2008,5):
    q = "year=="+str(y)
    AAA = gap.query(q)
    plt.figure()
    sns.scatterplot(data=AAA,x='gdpPercap',y='lifeExp',
                    size='pop',hue='continent')
    plt.xscale('log')
    plt.title('Health vs Wealth ('+str(y)+')')
    plt.legend(bbox_to_anchor=(1.01,1))
    plt.ylim(25,85)
    plt.xlim(200,120000)
    plt.show()

print(gap.sort_values('gdpPercap'))


#---
# 8. Lab 07 exercises
msleep = pd.read_csv('msleep.csv')

# (d)
RRR = msleep.query("order=='Rodentia'")
print(RRR)
SSS = RRR[['sleep_cycle','sleep_rem']]
print(SSS)
plt.figure()
SSS.plot.box()
plt.show()
 
plt.figure()
RRR.boxplot(['sleep_cycle','sleep_rem'])
plt.show()

# Two ways of doing boxplots in pandas

print(RRR.sort_values('brainwt'))


#---
# 9. Break out rooms
#    Lab 08 exercises (fruit.csv)

# -- the end --
