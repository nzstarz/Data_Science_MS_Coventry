
# 7143CEM Programming for Data Science
# Live coding -- Week 1 -- Wednesday (part two)

# Think Python 2e -- Chapters 7,10
# Lists, iteration


#---
# 4. More on strings, methods, slicing
s = "road runner"
print(s)
print(type(s))
print(len(s))

# string methods
print(str.upper(s))
print(str.capitalize(s))

t = str.upper(s)
print(t) # t is a copy of s, then changed
print(s)
# https://www.w3schools.com/python/python_ref_string.asp

print(s.upper()) # s says do upper to me
print(s.find('r')) # first occurrence
print(s.rfind('r'))
# 0 is the FIRST index in the string
#   Python is zero-based indexing
# 10 is the ELEVENTH index in the string

print(s[0]) # first character in s
print(s[10]) # last character because len is 11
print(s[3])
print(s[-1]) # last (shortcut)
print(s[-2])

# slice
print(s[0:4]) # start at index 0
              # stop at index before 4 (not including 4)
print(s[3:8])
print(s[0:2],s[2:4])

print(s[3:])
print(s[:3])
print(s[:])
print(s[:-1])
print(s[2:-2])
print(s[-8:8])
print(s[8:-8]) # empty string

# Think of a string as a sequence of characters
# start indexing from 0


#---
# 5. Lists, slicing, split
# string has ''
# list has square brackets []
L = [1,4,7,2]
# values separated by commas, surrounded by []
print(L)
M = ['a','e','i','o','u']
print(M)
P = ['hello',3.14,-8,True,None]
print(P)
# each element in the list has its own type
Q = []
print(Q)
print(len(Q))
print(len(L))
print(type(L))

# indexing
print(M[0])
print(M[4])
print(M[-1])
print(M[1:4])
print(M[1:2])
print(M[1])
print(type(M[1:2]))
print(type(M[1]))
#! print(M[999]) too far
print(type(L[2]))

print(list('hello'))
print(str(M)) # not what you think it is!!!!!!!
print(''.join(M))

print(L)
print(list.sort(L))
print(L)
# Notice, sort changes L

J = [4,9,2,5,7]
print(J)
print(sorted(J)) # does not change list J
print(J)

# how are strings different from lists
s = 'hello'
print(s)
print(s[0])
#! s[0] = 't'
# cannot change an existing string
# strings are IMMUTABLE
a = s[0]+'y'+s[2:]
print(a)

print(J)
J[1] = 99999
print(J)
# can change an existing list
# lists are MUTABLE

# strings and list are both ORDERED, indices

# garbage collector
s = 'hello'
print(s.upper())
print('goodbye'.upper())


# Break time: 10 minutes -- come back at 7pm
    

#---
# 6. Loops, for/range, while, chat bot, dice games
L = ['red','green','blue',10,7,True]
print(L)
for x in L:
    print('hello',x)

P = [2,3,5,7,11,13]
for w in P:
    print('next one:',w,w**2,w**3,w**4)

print('bonnie',end='')
print('wee lad')

for a in range(5):
    print(a)
for b in range(0,5):
    print(b)
print(range(0,5))
print(list(range(0,5)))
for c in [0,1,2,3,4]:
    print(c)
    
# Add up the numbers is a list
print(P)
sum = 0
for a in P:
    sum = sum + a
print(sum)

for i in range(3,11,2):
    print(i)
for i in range(20,3,-3):
    print(i)
# third argument is the jump
# arguments are: start, stop, jump but don't include stop


print(P)
for k in range(0,len(P)):
    print(k,P[k])

# Task: find the smallest number in a list
def min_value(L):
    """Find the minimum value in a given
    list of numbers"""
    # Idea: work left to right through the list
    smallest_so_far = L[0]
    for k in range(1,len(L)):
        print('current smallest',smallest_so_far)
        print('  k=',k,' now considering value',L[k])
        if (L[k]<smallest_so_far):
            smallest_so_far = L[k]
            print('    updated now smallest',smallest_so_far)
        else:
            print('    ignored that one')
    return(smallest_so_far)

M = [3,8,6,0,9,4,1]
print(M)
print(min_value(M))


# randomness
print('dice game ...')
import random
def roll_a_six():
    """Keep rolling a dice until we get a 6."""
    count = 0
    d = random.randint(1,6)
    print(d)
    count = count+1
    while (d!=6):
        d = random.randint(1,6)
        print(d)
        count = count+1
    print('well done to you')
    print('number of rolls:',count)

roll_a_six()

# -- the end --
