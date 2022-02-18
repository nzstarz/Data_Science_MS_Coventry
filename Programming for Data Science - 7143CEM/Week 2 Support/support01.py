
# 7143CEM Programming for Data Science
# Live coding -- Week 2 -- Wednesday

# Support session

# (1) Catchup / Aula / recordings

# (2) Books / resources / cheatsheets

# (3) Overview of the Portfolio (Task 1 only)

#---
# (4) What support do you need?  Any and all questions welcome
# -- Think Python
def myfunction(a):
    result = a*2
    print(result)

b = myfunction(3)
print(b)


#---
# (5) Lab 5 exercises
# -- Question 5
#    each card is a tuple (suit,number)
def check_card(card):
    suit = card[0]
    number = card[1]
    # suit, number = card
    if ((suit=='Hearts') or (suit=='Diamonds') or
        (suit=='Clubs') or (suit=='Spades')):
##  if (suit in {'Hearts','Diamonds','Clubs','Spades'}):
        if (number>=2) and (number<=14):
            result = True
        else:
            result = False
    else:
        result = False
    return(result)

cardA = ('Hearts',13)
cardB = ('Hearts',14)
flush = (cardA[0]==cardB[0])
print(flush)
straight = ((cardB[1]-cardA[1]==1) or
            (cardA[1]-cardB[1]==1))
straight = (abs(cardB[1]-cardA[1])==1)
print(straight)
# abs is "absolute value" function
royal_flush = (flush and straight and
     ((cardA[1]==14) or (cardB[1]==14)))
print(royal_flush)


#---
# Other Questions

# 2pm, what is the time in 51 hours
now = 14 # 2pm in 24 hour clock
later = now + 51
future = later % 24
print(future)
# answer: 5pm

# computer time is seconds since 1 Jan 1970
# year 2038 problem
seconds = (2038-1970)*365*24*60*60
print(seconds)
print(2**31)

def hello(a):
    print('here we are')

hello('red')

# a = 1
# a(5) # not callable

b = 8
print(b)
b = 99
print(b)
b = 'hello'
print(b)

d = 5
if (d<10):
    print('great')
elif (d>5):
    print('amazing')
    
# if-elif is good for one case out of many

import random
print('about to start')
for k in range(0,5):
    colour = random.choice(['red','orange','green'])
    print(colour)
    if (colour=='red'):
        print('stop')
    elif (colour=='orange'):
        print('get ready')
    elif (colour=='green'):
        print('go go go')
    else:
        print('***Dear Mark, this should NEVER happen***')
    print('take a sip of tea')
print('all done')


# add up numbers one two ten
print(1+2+10)
# add up numbers one to ten
print(1+2+3+4+5+6+7+8+9+10)    

import numpy as np
print(np.sum(range(1,11)))

output = input('Type a number:')
print(output)
print(type(output))
number = int(output)
print(number)
print(type(number))

keep_going = True
while (keep_going):
    line = input('Tell me a fact: ')
    if (line=='please stop'):
        keep_going = False
    else:
        print('I do not understand ',line)
        print('Please can you explain a bit more')
    

# (6) conda update conda (DON'T do it now!)
#     -- see Useful Resources | Software

# -- the end --
