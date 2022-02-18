
# 7143CEM Programming for Data Science
# Live coding -- Week 1 -- Monday

# Checklist:
# (1) Install Anaconda Individual edition (free)
# (2) Launch Spyder IDE
# (3) Think Python 2e (free book)

# Think Python 2e -- Chapters 1,2
# Values, types, expressions


#---
# 1. Values
print('Hello world')
# this is a comment (for humans)
# between quotes is a string of text
print("Hello world")
print('Susie says "Goodbye"')
print('')
print('qpoeor12387867$£$%^')
print('backslash has a\n meaning here')

print(42) # whole number
print(-5) # integers
print(0)
print(999999999999999999999999)

print(3.14) # float
print(3.0) # float
print(0.999999999)

print(True) # logic values / Boolean
print(False)

print(None)


#---
# 2. Types
print(type('data'))
print(type(42))
print(type(3.14))
print(type(True))
print(type([]))
print(type(None))


#---
# 3. Expressions
print(1+2)
print(1+2+3+4+5)
print(type(1+2))

print(1.5+2.5)
print(type(1.5+2.5))
print(1+2.0)
print(type(1+2.0))

print('hello'+'goodbye')
print(type('hello'+'goodbye'))
# concatenation of strings

# summary: + is smart plus

#! print('hello'+2) # this doesn't work

print(2*3)
print(type(2*3))
print(type(2*3.5))
#! print('hello'*'goodbye')
print('Happy birthay\n'*21)
print('a'*100)
print('clap '*9)

print(5-2)
print(2.5-1.5)
#! print('hello'-'h')

print(10/2)
print(type(10/2))
# / for division gives float

print(20/6)
print(20//6) # integer division
# how many 6s fit into 20
print(20%6) # remainder
# what is left over when we fit 6s into 20

print((5+2)*10-6*17) # BEDMAS/BODMAS/PEMDAS
# order of operations


# -- the end --
