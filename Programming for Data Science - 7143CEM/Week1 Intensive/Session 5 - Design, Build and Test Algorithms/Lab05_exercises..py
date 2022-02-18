# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 01:00:24 2022

@author: USER
"""

# Lab05_exercises

#  Problem No 1
# convert minutes to days, hours, and minutes
import math
def convert(minute):
    days = math.floor(minute /1440)
    mints_remaining = minute % 1440
    
    hours = math.floor(mints_remaining /60)
    mins = minute - (days*1440) - (hours*60)
    
    return  days, hours, mins
    


convert(minute=3456)


# convert minutes to days, hours, and minutes

import math

def transform_minutes(total_minutes):

    days = math.floor(total_minutes / (24*60))
    leftover_minutes = total_minutes % (24*60)
    
    hours = math.floor(leftover_minutes / 60)
    mins = total_minutes - (days*1440) - (hours*60)
    
    #out format = "days-hours:minutes:seconds"
    out = (days, hours, mins)
    return out

transform_minutes(3456)


# Python Program to Convert seconds into hours, minutes and seconds
  
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# Driver program
n = 12345
print(convert(n))

# https://www.geeksforgeeks.org/converting-seconds-into-days-hours-minutes-and-seconds/?ref=lbp


# Question 2.
a = 4
b = 6
a = a + b 
b = a - b 
a = a - b

print(a)
print(b)



a = True
b = False
a = a + b 
b = a - b 
a = a - b

print(a)
print(b)

# Tuple swap
x, y = y, x

# Question 3.

A = 'dog cat' 
print(type(A + 'cow'))
B = ['dog','cat'] 
print(B+[3])
C = {'dog','cat'} 
C.add('bat')
print(C)
D = ('dog','cat') 
print(type(D + 'mouse'))
E = {'dog': 'cat'}
E['dog']='can'
print(E)


# https://www.programiz.com/python-programming

# Question 4.

S = 'First, solve the problem. Then, write the code.'



# Question 5.

def  check_card(card):
    