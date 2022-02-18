
# 7143CEM Programming for Data Science
# Live coding -- Week 3 -- Tuesday

# Introduction to pandas
# -- included in Anaconda

# 1. Portfolio tasks
#    see Aula

# 2. Academic Integrity and Plagiarism
#    see Aula notice

# 3. "Cheat sheets" for numpy and pandas
#    see Aula | Overview of Week 3


#---
# 4. Pandas Series (one-dimensional data)
import pandas as pd
S = pd.Series([5,9,2,7,-4]) # constructor
print(S)
print(type(S))
# can think of a pandas Series as like a 1D numpy array
print(S[1:3]) # slice - index goes with the slice
A = S[1:3]
print(A)
print(A[1]) # preserves the index
#! print(A[3]) # KeyError (there is no value for index 3)
# 1,2 are index and 9,2 are the values

T = pd.Series([3,6,-4,8,25])
print(T)
B = T[2:5]
print(B)
print(S+T) # like numpy <----------
print(A)
print(B)
print(A+B) # adds by index
# in an index is missing it gets NaN
# common index then adds
# NaN is a float

import numpy as np
print(type(np.nan)) # IEEE standard

W = pd.Series([4,6,3],index=['a','b','c'])
print(W)
print(W['a']) # like dictionary <---------
print(W['b':'c']) # quite dangerous!!!

Z = pd.Series((1,2,3)) # can use a tuple
print(Z)

print(B)
#! print(B[0]) # KeyError
print(B.iloc[0]) # location by index (row 0) <- numpy
print(B.loc[3])  # location by value (key is 3) <- dictionary

print(B[2]) # <-- same as loc not iloc <- like dictionary
# nothing is loc
# be kind to your human if it is confusing

# chocolate bars (values are weights)
D = {'mars': 30,
     'snickers': 100,
     'bounty': 20,
     'dairy milk': 1000}
print(D)
print(type(D))
E = pd.Series(D)
print(E)
print(E['snickers'])
print(E.iloc[2])
# in pandas Series, index=key (same thing)
# for slice use iloc
print(E.iloc[1:3]) # <- slice IS a pandas Series

print(E)
print(E+2)

F = {'kit kat': 90,
     'snickers': 100,
     'batman oreos': 45,
     'dairy milk': 1000}
G = pd.Series(F)
print(G)
print(E)
print('E+G ...')
print(E+G)

#! print(D+F) Python cannot add dictionaries

# Index can be anything immutable:
#   number, string, tuple
H = pd.Series(['Hulk','green',3.0,'treasure'],
              index=['name','colour','height',(3,2)])
print(H)
print(H[(3,2)])

print(G)
print(G**2)

# Main idea: we don't care which row the information is
# stored in, only need keys


# Break time: come back at 7:05pm


#---
# 5. Pandas DataFrame (two-dimensional data)
# "tidy data" (rows and columns)
#   rows are individuals/objects/countries/observations
#   columns are variables/attributes/features
#   each cell/element represents ONE value
# if we have tidy data, we can use DataFrame

A = [['Cat Stevens', 80,  2, 99],
     ['John Lennon', 90, 10, 37],
     ['Eminem',      18,  1, 12],
     ['Genesis',     65,  5, 60]]
B = pd.DataFrame(A,
                 columns = ['artist','score','fans','age'])
# could also have index=[list of keys]
print(B)
C = B.set_index('artist') # make one column into the index
print(C)

D = {'mars': 100,
     'bounty': 200}
E = {'mars': 10,
     'bounty': 0}
F = pd.DataFrame({'price': D, 'sales': E})
print(F)
# can think of a DataFrame as a matrix (rows/columns)
# or can think of a DataFrame as dictionary of dictionaries
# don't have to have unique keys
# helps to have unique keys

print(C)
G = C['score']
print(G) # index comes with the column
print(type(G)) # G is a series
# --> if we pull one column, we get a Series
list_of_column_names = ['age','fans']
Ha = C[list_of_column_names]
print(Ha) # get index as well
print(list_of_column_names)
print(type(list_of_column_names))
Hb = C[['age','fans']] # <-- often see double []
print(Hb)
print(type(Hb))
J = C[['age']]
print(J)
print(type(J)) # <-- DataFrame

print(D)
print(D['mars'])


# Aula: download yob1880.csv
#                baby_names.csv
# put into the same folder as this Python code

# Baby names born/registered in USA
# CSV file = comma separated values (text file)
# yob1880.csv = all births in year 1880 in USA
baby = pd.read_csv('yob1880.csv',
                   names=['Name','Gender','Babies'])
print(baby)
print(baby.shape)

A = baby['Gender']
print(type(A))
print(A.describe()) # summary

# Remember this is just Python
print(baby['Gender'].describe())
print(baby.Gender.describe())
print(baby.Name.describe())

# Excitement starts here
girls = baby.query("Gender=='F'") # pull out rows
print(girls)
print(girls.Gender.describe())
girls_top10 = girls.iloc[0:10]
print(girls_top10)

import matplotlib.pyplot as plt
plt.figure()
plt.barh(girls_top10.Name,girls_top10.Babies)
plt.figure()

boys = baby.query("Gender=='M'")
boys_top10 = boys.iloc[0:10]
plt.figure()
plt.barh(boys_top10.Name,boys_top10.Babies)
plt.figure()


G = girls.set_index('Name')
print(G)
B = boys.set_index('Name')
print(B)
A = B+G
D = A.dropna() # get rid of rows that have NaN in them
print(D)

print(baby.query("Name=='Mary'"))
print(baby.query("Name=='Walter'"))


# babynames.csv --> USA baby names 1880-2015
bigbaby = pd.read_csv('babynames.csv')
print(bigbaby.shape) # 1.8 million rows
print(bigbaby)
print(bigbaby.head())
print(bigbaby.tail(10))

person = bigbaby.query("(Name=='Leonardo') and (Gender=='M')")
print(person.shape)
print(person)

plt.figure()
plt.plot(person.Year, person.Babies)
plt.show()

this_year = bigbaby.query("Year==1992")
print(this_year.Babies.sum())

year = 1992
q = 'Year=='+str(year)
print(q)
this_year = bigbaby.query(q)
print(this_year.Babies.sum())
print(q)

for year in range(1880,2016):
    q = 'Year=='+str(year)
    this_year = bigbaby.query(q)
    print('Year',year,' Babies',this_year.Babies.sum())

# Warning! -- this is VERY SLOW
# Golden rule -- don't use loops with Pandas!!!!!!!!
# --> there must be a better way

# -- the end --
