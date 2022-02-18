
# 7143CEM Programming for Data Science
# Live coding -- Week 1 -- Thursday (part one)

# Think Python 2e -- Chapters 11,12
# Data Structures:
#   Sets, tuples, dictionaries
#   mutable? ordered?

#---
# 0. Parking list:
# -- practice exercise
# -- food: amala

# Every value has a type:
# string, int, float, bool, list, ...

print(bool(0)) # only zero becomes False
print(bool(1)) # everything not zero becomes True


#---
# 1. String '' or ""
s = 'Optimus Prime'
print(s)
print(s[2:5])
# s[5] = 'r' # string is IMMUTABLE (cannot change it)
# string is ORDERED because we index 0,1,2,...


#---
# 2. List []
L = [1,3,8,4]
print(L)
M = [1,'hello',[2,'goodbye'],['red',True]]
print(M)
print(M[2])
print(M[2][1])
print(M[2][1][5])

# h from hello and the red
print([M[1][0],M[3][0]])
print(M[1][0],M[2][1][0],M[3][0][0])

M[1] = 'hola'
print(M)
# List is MUTABLE (can change)
# List is ORDERED (index 0,1,2,...)


#---
# 3. Set {}
# interested in membership only
S = {'red','orange','yellow','green','blue','indigo','violet'}
print(S)
#! print(S[0]) # Set is NOT ORDERED, there is no indexing
print('red' in S) # in is a keyword (it is a set operator)
print('lime' in S)
set.add(S,'brown')
S.add('brown')
print(S) # only one brown is in the set
# Important idea of a set: something is or is not an element
# no counting
T = {'blue','white'}
print(T)
print(set.intersection(S,T)) # set method
print(set.union(S,T))
S.discard('green')
print(S)

# Sets are MUTABLE (can change, add elements)
# Sets are UNORDERED (no indexing)

# empty things:
print('')
print([])
print({})
print(type({})) # empty curly brackets is NOT a set, it is a dictionary
print(type({'red'}))
print(type(set()))
print(type(list()))
print(type(str()))

P = set()
print(P)
P.add('green')
print(P)

L = ['pizza','icecream','sandwich','cake','chocolate','amala','pizza']
print(L)
W = set(L)
print(W) # WARNING!!! -- set is unordered
print(W)

# set and list are used in different ways
# set: ask about does an element belong to the set
# list: where are you in the list, could occur multiple times
# these are as fast as possible at answering these questions

A = [6,9,3,4]
print(A)
B = set(A)
print(B)
C = list(B)
print(C)


#---
# 4. Tuple ()
T = (2,5) # remember points at school with coordinates
print(T)
print(T[0])
print(T[1])
# tuple is ORDERED
#! T[0] = 3 # tuple is IMMUTABLE
# permanently glued together
U = (10,5)
print(U)
print(T+U)
print([1,2]+[3,4,5])

#! print((1,2,3)+[7,8,9]) # mixed types

# Summary:
# string:   ordered    immutable
# list:     ordered    mutable
# set:      unordered  mutable
# tuple:    ordered    immutable
# what is missing?:  unordered   immutable
#    --> frozenset (investigate this)


# Break time: come back at 11:43am (20 minutes)


#---
# 5. Dictionary also {}
# Idea: interested in a word, and look up the meaning
# e.g. sausage

# Python: dictionary has keys and values
# know the key and lookup the value that goes with that key

snack = {'name': "Pringles",
         'price': 70,
         'weight': 100,
         'flavour': 'onion',
         'healthy': False,
         'best before': '21 Feb 2023',
         'location': (3,7,2)}
print(snack)
#! print(snack[0]) # dictionary is NOT ORDERED
print(snack['name'])
print(snack['price']) # use key as 

# you might say we could use a list
snack_list = ["Pringles",70,100,"onion",False,"21 Feb 2023",(3,7,2)]
# this is be very old old old old thinking

print(type(snack)) # dict
print(dict.keys(snack))
print(list(dict.keys(snack)))

print(snack.keys())
print(snack.values())

print(list(snack.keys()))

heros = {'Superman': 95,
          'Batman': 23,
          'Wonder Woman': 87,
          'Iron Man': 63,
          'Hulk': 10,
          'Spiderman': 34}
print(heros['Batman'])

# Dictionary is UNORDERED
heros['Batman'] = -4
print(heros)
heros['Black Widow'] = 78
heros['Green Lantern'] = 350
heros['Princes Shuri'] = 100000
print(heros)
heros.pop('Superman') # remove a key/value pair
print(heros)
# Dictionary is MUTABLE

E = {'greeting': 'hello',
     'greeting': 'vanakam',
     'greeting': 'bulla',
     'greeting': 'bonjour',
     'greeting': 'kemchho',
     'greeting': 'namaste'}
print(E) # keys are UNIQUE in a dictionary
# can only have one value for each key

F = {'english': 'hello',
     'tamil': 'vanakam',
     'fijian': 'bulla',
     'french': 'bonjour',
     'marathi': 'kemchho',
     'hindi': 'namaste'}
print(F)

# Dictionary is very very very fast at looking up a
# value for a given key
# -- uses hash functions
# Dictionary is MUTABLE but NOT ORDERED (like a set)

# What can be used as a key in a dictionary?
# -- anything that is IMMUTABLE
D = {'name': 'Jack Sparrow',
     23: 'Michael Jordan',
     (3,10): 'Treasure is here',
     3.1415926: 'pi'
     }
# Could we use a list as a key: NO
# Could we use a set as a key: NO
# Could we use a frozenset as a key: YES
print(D)
print(D[23])
print(D[3.1415926]) # party trick
a = 4
a = a*1


#---
# 6. Loops over data structures
# string, list, set, tuple, dictionary
s = 'namaste'
for a in s:
    print(a)
L = ['red','green','red',54]
for b in L:
    print(b)
W = {'mercedes','bentley','mustang','bmw'}
for c in W:
    print(c) # order is not guaranteed by Python because set is UNORDERED
D = {'name': 'Boris',
     'job': 'PM',
     'party': True}
print(D) # dictionary is NOT ORDERED, unpredictable what order they appear
for k in D:
    print(k) # only the keys
for k in D:
    print(k,D[k])
for k,v in D.items():
    print(k,v)
T = (2,9,(3,4),'red',{1,2,3})
for f in T:
    print(f)


# Big long break time: come back at 1:30pm (43 minutes time)

# -- continued in next Python file --

