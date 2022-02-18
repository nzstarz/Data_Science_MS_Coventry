
# 7143CEM Programming for Data Science
# Live coding -- Week 1 -- Wednesday (part one)

# Think Python 2e -- Chapters 3
# Functions, libraries

# Checklist:
# -- access to Aula and MS Teams
#      https://coventry.aula.education/
# -- installed Anaconda and using Spyder
#      Anaconda -- https://www.anaconda.com/products/individual
#      Spyder IDE -- integrated development environment
# -- had a look at Think Python book
#      https://greenteapress.com/wp/think-python-2e/
# -- course director/module leader
#      Mark Johnston: ad4039@coventry.ac.uk


#---
# 1. Recap on Python
#     values, types
#     operators, expressions (including // and %)
#     variables
#     functions, string methods
#     operators (arithmetic, boolean, relational)
#     expressions (order of precedence)
#     if-elif-else


#---
# 2. Building functions

def leap_year(year):
    """Find out whether a given year
    is a leap year"""
    if (year%400==0):
        result = True
    elif (year%100==0):
        result = False
    elif (year%4==0):
        result = True
    else:
        result = False
    return(result)

print(leap_year(2022))
print(leap_year(2020))
print(leap_year(2000))
print(leap_year(1900))

# Challenge: how many days are in 400 years?
days = 365*400 + 100 - 4 + 1
print(days)
# Answer: 146097

# Is this number of days a whole number of weeks
# i.e., is it a multiple of 7?
print(days%7==0)
# True

# Summary: 400 years is a whole number of weeks
# 2022 calendar will be reusable in 2422

def day_of_1January(year):
    """Find the day of the week of 1 January
    in a given year."""
    # Zeller's algorithm
    Y = year-1
    y = Y%100
    c = Y//100
    d = 1
    m = 13 # Jan=13 Feb=14 of previous year
    w = ((13*(m+1))//5 + y//4 + c//4 + d + y - 2*c) % 7
    # 0=Saturday, 1=Sunday, ... 6=Friday
    return(w)

print(day_of_1January(2022)) # SATURDAY
print(day_of_1January(2023)) # SUNDAY
print(day_of_1January(2024)) # MONDAY
print(day_of_1January(2025)) # WEDNESDAY

# Question: how many calendars are there?
# One possible answer: 14 (7 days for 1 Jan, for each leap year or not)
# Objection: Easter, bank holidays

print(day_of_1January(2028)) # SATURDAY
print(leap_year(2028))
print(day_of_1January(2033)) # SATURDAY
print(leap_year(2033))

# Reuse 2022 calendar in 2033 (sell it to your friend)

# Break #1: come back at 3:55pm

# Demo of the debugger with leap_year

def int_to_hex(number):
    """Converts an integer 0-15 into a
    hexadecimal code (base 16)
    0 1 2 3 4 5 6 7 8 9
    A=10 B=11 C=12 D=13 E=14 F=15"""
    if (number<10):
        result = chr(48+number)
    else:
        result = chr(55+number)
    return(result)

print(int_to_hex(0))
print(int_to_hex(9))
print(int_to_hex(10))
print(int_to_hex(15))

# On webpages, colours like 00FFAA
# red/green/blue, red=0 to 255 (8-bits)
# 00 (hexadecimal) = 16*0 + 1*0 = 0 (no red)
# FF = 16*15 + 1*15 = 255 (full green)
# AA = 16*10 + 1*10 = 170 (2/3 blue)


#---
# 3. Modules, methods, random (rolling dice)
# Python is free, and people give away their
# code for free, so how to we get it?
# Python packages/libraries

print(2**5)
print(2**0.5) # square root

import math
# brings in all the functions from the math library
print(math.sqrt(2))
print(math.pi)

import sympy
print(sympy.pi)
# computer algebra and calculus
print(sympy.pi.evalf(1000))

import keyword
print(keyword.kwlist)
# keywords, reserved words
# (cannot use for variable names)

import random
print(random.randint(1,6))
print(random.randint(1,6))
print(random.randint(1,6))
print(random.randint(1,6))
# rolling dice


# LONG break: come back at 5:30pm

# -- continued in next Python file --
