import pandas as pd
import matplotlib.pyplot as plt



msleep = pd.read_csv('E:\\Data Science\\Coventry\\Programming for Data Science - 7143CEM\\Week3 Intensive\\Session 2 - Introduction to Pandas\\msleep.csv')
msleep.head()


# A

print(msleep.shape)

# B

GG = msleep.order.unique()
print(len(GG))

# or
print(msleep['order'].nunique())
print(msleep['order'].describe()['unique'])
print(msleep['order'].value_counts().shape)
print(len(set(msleep['order'])))


# C

AA = (msleep.vore.value_counts())
print(AA)

# or
C = msleep.groupby('vore').vore.count()
print(C)


plt.figure()
AA.plot.barh()
plt.show()



#  D

BB = msleep.query('(order == "Rodentia")')
print(BB)


CC = BB['sleep_cycle'].dropna()

DD = BB['sleep_rem'].dropna()
print(CC)
print(DD)

columns = [CC, DD]

fig, ax = plt.subplots()
ax.boxplot(columns)
plt.show()

# Or

DD = msleep.query("order=='Rodentia'") 
print(DD)

EE = DD[['sleep_cycle', 'sleep_rem']]
print(EE)

plt.figure()
EE.plot.box()
plt.show()

# Or

plt.figure()
DD.boxplot(['sleep_cycle', 'sleep_rem'])
plt.show()

print(DD.sort_values('brainwt'))
