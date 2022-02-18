
# 7143CEM Programming for Data Science
# Live coding -- Week 1 -- Tuesday

# Think Python 2e -- Chapters 1,2,3,5,8
# Variables, functions, strings, Booleans, if-else

#---
# 1. Review: values, types, expressions
print('this is a string') # string
print(10) # integer
print(4.72) # floating point numbers
print(True) # logic values / Boolean / bool
print(type('this string'))
print(type(10))
print(1+1)
print('1'+'1')
print(type('1'+'1'))
print(2*3)
print('hello '*4)


#---
# 2. Variables
# variable is a box with a label
# inside the box is a value
# the label is the variable name
name = 'Mark'
# take the value which is the string 'Mark'
# and put it in a box labelled name
# = is called assignment, take value on right
# and put in the box on the left
# not the same as maths
# usually we use descriptive variable names
bank_balance = -5982
area_of_square = 100
# use letters, digits and underscore _
# in variable names, but cannot start with
# a digit
pi = 3.1415927
# variable names are case sensitive
# unusual to have all capitals
# usually use "snake case" my_name
#   underscores instead of spaces
# in Python don't usual use CamelCase

name = 'Mark'
print(type(name))
name = 52
print(type(name))
# Python uses dynamic typing, looks at the
# value stored to work out the type of the
# variable
# giving you alot of rope, but easier to
# hang yourself

age = 5
# then you have a birthday
age = age + 1
# mathematicians will say that is impossible (0=1)
# remember = is assignment
# value on right goes in variable on left

# powers
print(2**4)
# same as
print(2*2*2*2)


#---
# 3. Built-in functions
print(3.14)
print(round(3.14)) # to investigate for homework!
print(round(6.51))
print(round(6.49))
print(round(5.5))
# what is going on here???
# Banker's rounding -- try to explain

# Function takes input and gives output
print(print(1))
print(type(1))
print(type(type(1)))
print(float(1))
print(str(1))
print(type(str(1)))
print(int(3.14))
print(int(-3.14)) # stripping off the decimal
print(int('12345')*2)
print('12345'*2)

# sometimes (very rarely) do:
if (False):
    response = input('Type a number here:')
    print(response)
    print(type(response))
    # be careful, it is a string
    number = float(response)
    print(number)
    print(type(number))

# if -- we will do later

# There are lots of built-in functions in Python

# Key idea: function has input and ouput values


#---
# 4. Functions (make your own)
# Physics:
#   kinetic energy: E = 0.5*m*(v**2)

m = 50
v = 10
E = 0.5*m*(v**2)
print(E)

m = 10
v = 5
E = 0.5*m*(v**2)
print(E)

def kinetic_energy(m,v):
    E = 0.5*m*(v**2)
    return(E)

# function name follows same rules as variable name
# m, v are inputs (arguments, parameters)
# return gives the output value
# 4-spaces indenting (NO TABS EVER EVER EVER)
# indenting tells Python where our function
# starts and stops
# intented bit is the body of the function
# def line is the header of the function

# now a function call:
print(kinetic_energy(50,10))
print(kinetic_energy(10,5))

def kinetic_redo(mass,velocity):
    """Calculate the kinetic energy of an object
    with given mass and velocity"""
    kinetic_energy = 0.5*mass*(velocity**2)
    return(kinetic_energy)

print(kinetic_redo(50,10))

# Triple-quotes straight after function header
# is a docstring, provides the help for the function

# One way to build a function is to copy-paste
# the guts of it (formula) and then wrap it up
# in header, return, docstring

# Another approach ... want a function to calculate
# the area of a circle

def area_of_circle(radius):
    """Calculate the area of a circle
    with a given radius."""
    pi = 3.1415927
    area = pi*(radius**2)
    return(area)

print(area_of_circle(10))

def any_old_thing():
    pass
    
any_old_thing()
print('here')
print(any_old_thing())
print(type(None))


#---
# 5. String methods
print('Twinkle twinkle little star')
print('Twinkle twinkle little star,'+
      'how I wonder what you are,'+
      'up above the world so high,'+
      'like a diamond in the sky.')
print("""Twinkle twinkle little star,
how I wonder what you are,
up above the world so high,
like a diamond in the sky.""")
# Triple quotes let you have strings that
# cover multiple lines.
song = """Twinkle twinkle little star,
how I wonder what you are,
up above the world so high,
like a diamond in the sky."""
print(song)
print(len(song))
print(len('a\nb'))

# Methods are like functions that belong to a
# particular type
print(str.upper(song))

sentence = 'hello. my name is "mark"'
print(str.capitalize(sentence))
print(str.split(song)) # result is a list
# just breaks up by spaces


# Break time: come back at 7:10pm


# we will come back to strings another time

print('a\nb')
# \n is the newline character
print('Dear Mark,\nHere is your pay rise.')
# \something is an escape sequence
print('Here is a backslash \\')
print(len('\\'))
print('a/nb')
# dear human reader: this is a newline all by itself
a = """
"""
print(len(a))
#! print(str.upper(1))

print(str.upper(song))
# is the same as
print(song.upper())
# basic view of "objects" or "object oriented"


#---
# 6. Boolean operators (logic)
print(True)
print(False)
print(type(True))
print(type(False))
print('-----')
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# and gives True if both sides True, otherwise False
# "truth table"
print('-----')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# or gives True if either argument True, otherwise False
print('-----')
print(not True)
print(not False)
# not is the opposite
# NOTICE: purple and or not def pass return
# keywords / protected words

# Boolean Expressions
a = True
b = False
c = True
print(a or b)
print(a or not b)
# order of operations (BEDMAS):
# brackets, not, and, or
print(a or not b and c)
# remember your human reader:
print(a or ((not b) and c))
# brackets are free


#---
# 7. Relational operators
print('----')
# In language we say a statement:
# "I am wearing glasses"
# you say: False
print(1<3)
print(10<8)
print(1>3)
print(1>=1)
print(8<=27)
print(10*13<=17) # order of operations
# arithmetical operators are higher precedence
#   than relational operators
#! print(10=10)
# using 10=10 gives
# Syntax error means that Python does not understand
# what you have written
# = is assignment
print(10==10)
# use == for checking equals
print(1==0)
print(1!=0)
print('--- how about strings ---')
print('a'<'b') # alphabetical order
print('0'>'z')
# letters
print(ord('a')) # ASCII value 0-255 / UTF
print(ord('\n'))
print(chr(98))
print('hello'<'goodbye')
print('abcde'<'abcdf') # dictionary order
print(' '<'k')
print(ord(' '))
print(ord('k'))
print(ord("'"))
print("'"<'"')
print("\""<'\'')
# backslash something is called an escape sequence
# trying to type a special character usually
# not on my keyboard

# leap year
year = 2022
# is there a February 29?
# looking for divisible by 4
print(year/4)
print(year//4) # integer division
print(year%4) # remainder
print(year%4==0) # is year divisible by 4?
print(year%100==0) # 1900 is not a leap year
print(year%400==0) # 2000 is a leap year

print(1<4 and 3<7)
# relational operators are higher precedence
# than logic operators
# brackets, arithmetic, relational, logic
print((1<4) and (3<7))

print(4/1)
#! print(4/0) # doesn't work

print(True or True)
print(1<3 or 5<2)
print(4/1<10 or 4/1>99)
print(4/1<10 or 4/0>99) # actually True
# but incredibly bad programming
# Python takes a shortcut
print(4/1>10 and 4/0<9)
# short circuit
# concept called "lazy evaluation"
#! print(4/0>99 or 1<2)

def f1():
    print('Hello')
    return(True)

def f2():
    print('Goodbye')
    return(False)

print(f1() and f2())
print(f2() and f1())
# "side effect"


#---
# 8. if-else (conditional execution)
# condition is an expression that is evaluated
# (ends up being) True or False
height = 5.75 # height in feet
if (height<2):
    # do this bit if condition is True
    print('you are short')
else:
    # do this bit otherwise
    print('you might not be short') 

if (height<2):
    print('you are short')
else:
    if (height>10):
        print('basketball needs you')
    else:
        print('you are normal')

if (height<2):
    print('you are short')
elif (height>10):
    print('basketball needs you')
elif (height<5):
    print('maybe you will grow still')
else:
    print('you are normal')
print('all the way out')


# To write code:
# (1) sequence: line, line, line, line
# (2) conditional execution: if, if-else, if-elif-else
# (3) loops: while, for


# -- the end --
