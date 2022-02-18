
# 7143CEM Programming for Data Science
# Live coding -- Week 5 -- Wednesday

# Absolute Beginners

#---
# 0. Big Data
# -- Mythbusters Demo GPU versus CPU

#---
# 1. Python -- values, types, expressions, variables, functions, strings

# values
print(10)
print('hello')
print(-1.2)
print(False)
print(None)
print([1,2,3])
print({1,2,3})

# types
print(type(10))
print(type('hello'))
print(type(None))

# expressions
print(2+3)
print(2.5+3.5)
print('red'+'blue')
print(3**2) # powers
print(19//4) # integer division
print(19%4) # remainder
print(3<=8)
print(3==8)
print(3!=8)
print((3<=8) or (9<2))
# precedene order: brackets, powers (exponents), div/mult, add/sub
# relational (< > <= >= == !=), not, and, or

# variables
password = 'iamnottelling'
age = 21
temperature = 18.7
age = 27
age = 4+18+7
# name these well, use snake_case

# functions
def addition(a,b):
    """Add two values"""
    result = a+b
    return(result)

print(addition(10,10))
print(addition(3,8))
print(addition('hello','goodbye'))

assert addition(3,8)==11

s = 'Manchester United 2 nil Brighton and Hove Albion'
print(s)
print(str.split(s)) # string methods
print(s.split())
print(s.upper())


#---
# 2. Python -- bool, if-else, random, lists, iterations, data structures
print(type(True))
print(type(False))
if (3<8):
    print('yes')
else:
    print('no')

mu_goals = 3
mc_goals = 0
if (mu_goals > mc_goals):
    print("MU wins")
elif (mu_goals==mc_goals):
    print("draw -- replay")
else:
    print("MU loses")

import random

def roll_a_five():
    """How many rolls does it take to roll a five"""
    count = 0
    dice = random.randint(1,6)
    count += 1
    #print(dice)
    while (dice!=5):
        dice = random.randint(1,6)
        count += 1
        #print(dice)
    #print('count is:',count)
    #print("Well done, you are a legend.")
    return(count)

roll_a_five()

all_results = []
for k in range(100000):
    rolls = roll_a_five()
    all_results.append(rolls)
#print(all_results)
print(sum(all_results)/len(all_results))
import numpy as np
print(np.mean(all_results))
    
# list []
L = [None,'red',True,17,3.45,['a','b'],{3,4,5}]
print(L)
# lists: mutable, ordered, duplicates allowed, slow
print(L[3:6])
L[2] = False
print(L)
print(L[-1])
L[-1].add(6)
print(L)

# set
fruit = {'mango','apple','pineapple','watermelon','strawberry'}
print(fruit)
# an element is or is not a member (elements are unique)
print('mango' in fruit)
fruit.discard('apple')
print(fruit)

# dictionary
house = {'chair': 'living room',
         'table': 'dining room',
         'jewelery': 'second drawer down',
         'blender': 'cupboard',
         'bed': 'bedroom #1',
         'rent': 100,
         'occupants': 5,
         'temperature': 18.4}
print(house)
print(house['rent'])

# Break time: come back at 4:05pm (20 minutes)



# dictionary (continued)
# fast for looking the value corresponding to a key
# unordered, mutable, keys are unique,
# key must be immutable: number, string, tuple

for k in house:
    print(k,house[k]) # keys+values
print(list(house.keys()))
print(list(house.items()))
for k,v in house.items():
    print(k,v)

D = {True: 1,
     False: 'red',
     None: 'wow'}
print(D)

# tuples ()
T = (4,9,'red')
print(T)


#---
# 3. Python -- debug, comment, critique, design, build, test

# Dice game: monopoly (1 player)
import random
def monnnnoply():
    """Play simplified Monnnnoply"""
    bank = 500
    position = 0
    laps = 0
    keep_going = True
    while (keep_going):
        print('position:',position)
        dice = random.randint(1,20)
        print('dice:',dice)
        position = position+dice
        if (position>=44):
            position = position - 44
            bank = bank+200
            laps = laps+1
            print('bank:',bank)
        if (position==33):
            # Go to jail
            position = 11
            bank = 0
        if (bank<=0):
            keep_going = False
    print('final position:',position)
    result = {'laps': laps,
              'bank': bank}
    return(result)

a = monnnnoply()
print(a)

def mm():
    return(monnnnoply())

# -- the end --
