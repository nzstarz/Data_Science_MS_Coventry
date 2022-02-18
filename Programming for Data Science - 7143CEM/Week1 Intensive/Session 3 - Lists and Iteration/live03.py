# 2. Building Functions

def leap_year(year):
    """Find out whether a given year is a leap year"""
    
    if(year%400==0):
        result = True
    elif(year%100==0):
        result = False
    elif(year%4==0):
        result = True
    else:
        result=False
    return (result)

print(leap_year(2022))
print(leap_year(2020))
print(leap_year(2000))
print(leap_year(2040))
print(leap_year(1900))
print(leap_year(2050))



def day_of_1January(year):
    # Zeller's algorithm
    Y = year-1
    y = Y%100
    c = Y//100
    d = 1
    m = 13
    w = ((13*(m+1))//5 + y//4 + c//4 + d + y - 2*c) % 7
    
    return(w)
print(day_of_1January(2022))
print(day_of_1January(2023))
print(day_of_1January(2024))
print(day_of_1January(2025))

"""Question: How many calender are there"""

print(day_of_1January(2028))
print(leap_year(2028))


print(day_of_1January(2033))
print(leap_year(2033))









print(2**5)
import math

print(math.sqrt(2))
print(math.pi)

import sympy
print(sympy.pi)
print(sympy.pi.evalf(2000))


import random
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))



r = "road runner"
print(r)
print(type(r))
print(len(r))

print(str.upper(r))
print(str.capitalize(r))

t = str.upper(r)
print(t)
print(r)

print(r.upper())
print(r.find('r'))
print(r.rfind('r'))

print(r[3])
print(r[-1])
print(r[-2])

#slice

print(r[0:4])
print(r[:6])
print(r[0:3],r[2:4])
print(r[3:])


print(list('hello'))

J = [4,9,2,5,7]
print(sorted(J))

print(J)


L = ['red', 'green', 'blue', 10, 7, True]
print(L)

for x in L:
    print('hi', x)
    
P = [2,3,5,7,11,13]
for w in P:
    print(w,w**3,w**2,w**4)


print('bonnie', end='')
print('wee lad')

for a in range(5):
    print(a)
for b in range(0,5):
    print(b)
    
print(range(0,5))
print(list(range(0,5)))

for c in [0,1,2,3,4]:
    print(c)
    
print(P)
sum = 0
for a in P:
    sum = sum + a
print(sum)

for i in range(3,15,2):
    print(i)

for i in range(20,-13,-2):
    print(i)

print(P)
for k in range(0,len(P)):
    print(k,P[k])

def min_value(L):
    smallest_so_far = L[0]
    for k in range(1,len(L)):
        print('current smallest', smallest_so_far)
        print('k=', 'now considering value', L[k])
    
        if (L[1]<smallest_so_far):
            smallest_so_far = L[k]
            print('updated now smallest', smallest_so_far)
        else:
            print(' ignored that one')
    return(smallest_so_far)
    
M =[3,8,6,9,0,4,1]
print(M)
print(min_value(M))


print("Dice game")
import random
def roll_a_six():
    """Keep rolling a dice untill we got a 6. """
    count = 0
    d = random.randint(1, 6)
    print(d)
    count = count+1
    while(d!=6):
        d = random.randint(1, 6)
        print(d)
        count = count+1
        print('Well done you')
        print('NUmber of rolls', count)

roll_a_six()
        