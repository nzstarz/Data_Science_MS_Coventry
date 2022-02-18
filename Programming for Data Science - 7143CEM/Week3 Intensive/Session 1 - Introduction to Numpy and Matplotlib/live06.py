
# 7143CEM Programming for Data Science
# Live coding -- Week 3 -- Monday

# Introduction to numpy and matplotlib
# -- included in Anaconda

#---
# 0. Recap
# -- student portal:
#      https://share.coventry.ac.uk/students/
# -- block teaching: 7143CEM (weeks 1-6), 7144CEM (weeks 7-12)
# -- Aula: https://coventry.aula.education
#    "Everything you need to know so far"
# -- weeks 1-2: python (using Spyder)
#    summary sheets + exercises
# -- assessment: Portfolio due Friday 11 March (end of week 8)


#---
# 1. What kinds of things do we do with data?
# -- get information from, analyse, wrangling,
#    manipulate, clean, forecasting, debug (correct),
#    modelling, visualise, rearrange, make informed decisions,
#    plot, check quality, explore, extrapolate,
#    store, keep safe, protect, retrieve, predict,
#    process, secure, delete, encrypt, update,
#    write/read/delete, validate, represent, summarise,
#    queueing (first-in-first-out),
#    crud (create/replace/update/delete),
#    structure, download, transmit, group,
#    try to understand, collect, produce

# Idea: no such thing as "raw data" (audit trail)
# Idea: metadata = "data about data", units, locations


#---
# 2. Overview of Week 3 (Python libraries for Data Science)
# -- (free) book by Jake VanderPlas
#    https://jakevdp.github.io/PythonDataScienceHandbook/
# -- book by Daniel Chen: "Pandas for Everyone"
# -- cheat sheets for numpy and pandas


#---
# 3. Lists
# ordered (indexing 0, 1, 2, ...)
# mutable (values can change)
# square brackets
# duplicates allowed
# slice
L = [4,2,7,5,9,5]
print(L)
print(type(L))
print(L[0])
print(L[2:4])
L[3] = 9999
print(L)
#------
M = [2,9,4,8,0,7]
print(M)
print(L+M) # concatenation
#! print(L+1) # type error
print(L+[1]) # concatenation
# Python is not good at maths
P = [1,3.14,'hello',{'name': 'Mark'}]
print(P)
# Lists are very general in Python
# each element has its own type
print(type(P[3]))

# To the rescue: numpy
import numpy
print(numpy.__version__)


#---
# 4. Numpy arrays
# conventions in Python, e.g., snake_case for variable
import numpy as np
# alias for numpy
print(np.__version__) # __ is special Python
A = np.array([3,7,9,2]) # numpy array
print(A)
print(type(A)) # numpy multi-dimensional array
print(A.dtype) # int32 is 32 bit integer
# in numpy array, every elements has the SAME type

B = np.array([1,'hello'])
print(B)
print(type(B))
print(B.dtype) # unicode / string

C = np.array([4,5,6,10])
print(C)
print(A+C) # vector addition
print(2*A)

d = 1000000000 # one billion
print(d) # Python is very happy with large integers
e = 9999999999999999999999999999999999999999999999999999
print(e)
print(e**2) # a bit slow
print(type(e)) # Python class int is happy

F = np.array([99999999999999999999999999999999999])
print(F)
print(F.dtype) # object
# Need to be careful

G = np.array([0,1,2,64])
print(G)
print(G.dtype)
# int32 is 32-bit integer
# how many different numbers in 32-bit integer?
# 32 0/1 --> 2**32
#   from -2**31 to 2**31-1 (includes 0)

H = np.array([0,1,2,127], dtype=np.int8)
# 8-bit integer: -2**7 to 2**7-1 (-128 to 127)
print(H)
print(H.dtype)
print(H+1) # overflow / clocking

J = np.array([0,2147483647])
print(J)
print(J+1)

# Main idea: in numpy arrays, every element is the
# same type, much more efficent/fast
# but be careful of the dtype (overflow)

# https://numpy.org/devdocs/user/basics.types.html


# Break time: come back at 11:10am (20 minutes)


# VanderPlas book has nice little table of dtypes

K = np.array([3.14,5.97])
print(K)
print(K.dtype) # 64-bit floating point number (IEEE standard)
# double-precision = float64

L = np.array([True,False,True,1==5])
print(L)
print(L.dtype)
# numpy has its own types (separate from Python)

# Background on bits/bytes
# 8-bits = 8 0/1s, e.g., 01101110
# 8 bits = 1 byte (number 0 to 255 or number -128 to 127)
#                  unsigned vs signed
#                 (1 character)

# 1000 bytes = 1 kilobyte (KB)
# 1000 KB = 1 megabyte (MB)
# 1000 MB = 1 gigabyte (GB) -- memory chips 8 GB
# 1000 GB = 1 terrabtye (TB) -- one hard drive
# SI prefix (metre, kilometre, etc)

# Older terminolgy: 1024 bytes = 1 kibibyte (new word)


# Vector operations
A = np.array([1,2,3])
print(A)
print(A**2)
print(4*A**2 + 3*A + 9)
# apply the operations to all elements in parallel
# (don't use for loops)
B = (A>2) # relational operators
print(B)
print(2**A) # powers
print(2**(2**A))
C = list(range(3,10)) # 3 up to 10 but not including 10
print(C)
D = np.arange(3,10)
print(D)
E = np.arange(-np.pi,np.pi,0.01)
print(E)
print(np.sin(E)) # trig functions, etc
# functions are applied to every element of the vector
# numpy calls these "universal functions" or "u-funcs"

# Dice rolling (Week 1 version)
import random
d = random.randint(1,6) # random values from 1,2,3,4,5,6
print(d)
L = []
for i in range(100):
    d = random.randint(1,6)
    L.append(d)
print(L)

# Dice rolling (Week 3 version)
print('Week 3:')
D = np.random.randint(1,6,100) # random values from 1,2,3,4,5
print(D)

# Aggregation (one number summary)
print(np.min(D))
print(np.max(D))
print(np.sum(D))
print(np.mean(D))
print(np.median(D))
print(np.std(D)) # standard deviation
print(D.min()) # methods

# Slices (just like lists)
E = np.array([2,3,5,7,11,13,17,23])
print(E)
print(E[3:6]) # index 3 up to 6 not including 6

# Warning!
print('---')
print(E)
G = E[3:6]
print(G)
G[1] = 999999
print(G)
print(E)
# Conclusion: G is a NOT a copy of the slice from E
# in Python this is called a "view"
# changes to G will also change E

E = np.array([2,3,5,7,11,13,17,23])
H = E[3:6].copy()
print(H)
H[1] = 999999
print(H)
print(E)
# Be careful about slices: copy vs view

S = 'Good morning.'
print(S)
print(S[0])
print(S[-1]) # last element
print(S[2:6])

T = S[2:6] # string is immutable, cannot change


# Indexing
E = np.array([2,3,5,7,11,13,17,23])
J = np.array([1,5,2,7])
print(E[J])
K = (E<=5) # relational operator
print(K)
print(E[K]) # Boolean indexing

Q = np.array((3,5,7))
print(Q)
# But wait for Pandas!!

# So far 1D numpy array
E = np.array([2,3,5,7,11,13,17,23])
print(E)
print(E.shape)
print(len(E))
print(E.ndim) # number of dimensions

W = np.array([[1,2,3],[4,5,6]])
print(W)
print(W.shape) # 2 rows, 3 columns
print(W.ndim) # 2D numpy array

# 7143CEM mostly stick with 1D numpy arrays
# 7144CEM mostly stick with 2D numpy arrays (matrices)


#---
# 5. Basic plotting with matplotlib
import matplotlib
print(matplotlib.__version__) # 3.3.2
# matplotlib is 1990s style Matlab plotting library

import matplotlib.pyplot as plt

# Barchart
food = ['sushi','steak','chocolate','pizza','ice cream']
price = [8, 5, 1, 3, 2]
plt.figure()
plt.bar(food, price)
plt.xlabel('Food item')
plt.ylabel('Price')
plt.title('Price of different food items')
plt.grid()
plt.show()

plt.figure()
plt.barh(food,price)
plt.show()

# Linechart
x = np.array([1,3,8])
y = np.array([-4,6,2])
plt.figure()
plt.plot(x,y,'k.',markersize=20)
plt.plot(x,y,'r:.',linewidth=5)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid()
plt.show()

# Old school Matlab style (1990s)
# . is point, - is line, -- is dashed line
# : dotted line, -. dash-dot line
# k is black, r is red, b is blue, g is green
# c is cyan, y is yellow, m is magenta
# Very low level plotting
# Lots of control
# But a bit ugly


#---
# 6. Missing data
# old days, we might use 0, 9999 for values that are
#   missing or not available
a = np.nan # not a number (IEEE standard)
print(a)
Z = np.array([1,2,5,np.nan,8,3])
print(Z)
print(Z.dtype)
print(np.mean(Z))
print(np.sum(Z))
print(np.nanmean(Z))
print(np.nansum(Z))


# Wishlist: process tables (like spreadsheets)
#           nice looking plots
#           pull in data from files
#           database style operations


#---
# 7. Taste of pandas
import pandas
print(pandas.__version__)

import pandas as pd
print('=======')
H = [0.60, 1.30, 0.90, 1.37]
S = pd.Series(H) # one column dataset
print(S)         # like a numpy 1D array
# also prints the index 0,1,2,3
print(S.dtype)
plt.figure()
S.plot.line()
plt.show()


# -- the end ---
