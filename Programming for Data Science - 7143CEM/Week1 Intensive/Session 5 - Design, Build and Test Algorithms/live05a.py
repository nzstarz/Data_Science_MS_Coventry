
# 7143CEM Programming for Data Science
# Live coding -- Week 1 -- Friday (part one)

# Design, Build and Test Algorithms


#---
# 0. Notices
#    -- part-time students, please make contact with Mark Johnston
#    -- Week 3 reading: Python Data Science Handbook
#       https://jakevdp.github.io/PythonDataScienceHandbook/
#    -- exercises on Aula


#---
# 1. Sorting algorithms
#    -- http://anim.ide.sk/sorting_algorithms_1.php
#    -- https://www.geeksforgeeks.org/sorting-algorithms/
#    -- selection sort
#    -- bubble sort
#    -- insertion sort


#---
# 2. Insertion Sort (with magnifying glass)
#    -- https://en.wikipedia.org/wiki/Insertion_sort

L = [6,4,10,8,2,3,5,9]
# Task: sort from low to high (ascending order)
# Idea: left-part of the list is already sorted
#       right-part of the list is yet to be sorted
# L = [6,       4,10,8,2,3,5,9]
# See the left part is list [6] all by itself, already sorted
# Take the first element of the right part (4)
# Try to work out where to "insert" that number (4) in the
# left-part which is already sorted
# To do this, we scan right-to-left through the left-part
# Compare the new one (4) with the tallest in the left-part
# -- if it is taller than the 6 then we have found where it goes
# -- otherwise we swap (6 and 4 swap places)
# -- continue scanning down the left-part list
#    no more in the left-part to look at
# L = [4,6,     10,8,2,3,5,9]
# left-part already sorted, take the 10
# compare 10 with 6, it is bigger, so NO SWAP, no more work
# L = [4,6,10,     8,2,3,5,9]
# left-part already sorted, take the 8
# compare 8 with 10, it is smaller, so SWAP
# L = [4,6,8,10,     2,3,5,9]
# compare 8 with 6, it is larger, so NO SWAP, we have found its home
# L = [4,6,8,10,     2,3,5,9]
# left-part already sorted, take the 2
# compare 2 with 10, SWAP
# L = [4,6,8,2,10,     3,5,9]
# compare 2 with 8, SWAP
# L = [4,6,2,8,10,     3,5,9]
# compare 2 with 6, SWAP
# L = [4,2,6,8,10,     3,5,9]
# compare 2 with 4, SWAP
# L = [2,4,6,8,10,     3,5,9]
# left-part already sorted, take 3
# compare 3 with 10, SWAP, with 8, SWAP, with 6, SWAP,
# with 4, SWAP, with 2, don't SWAP
# L = [2,3,4,6,8,10,     5,9]
# left-part already sorted, take 5
# compare 5 with 10, SWAP, with 8, SWAP, with 6, SWAP,
# with 4, don't SWAP
# L = [2,3,4,5,6,8,10,     9]
# left-part already sorted, take 9
# compare 9 with 10, SWAP, with 8, don't SWAP
# L = [2,3,4,5,6,8,9,10]

def insertion_sort(L_input):
    """Sort a list of values into ascending order
    using Insertion Sort"""
    L = L_input.copy()
    for i in range(1,len(L)):
        # suppose we have sorted left part L[0:i]
        #   not including index i
        # right part is L[i:]
        print('---- top of loop ----')
        print('Left-part is ',L[0:i])
        print('Right part is ',L[i:])
        print('Take index',i,' which as value',L[i])
        
        # need ANOTHER loop to scan down the left-part list
        # k loop with scan right-to-left
        for k in range(i,0,-1):
            print('Compare index',k,'with index',k-1)
            print(' --> compare value',L[k],' with value ',L[k-1])
            if (L[k]<L[k-1]):
                print('Swap')
                L[k-1],L[k] = L[k],L[k-1] # multiple assignment
                print('List is now',L)
            else:
                print('No swap needed')
                # --> somehow we need to STOP the k loop!!!!
                print('List is now',L)
    
# Modelling: incremental development

L = [6,4,10,8,2,3,5,9]
print('Before we start:',L)
insertion_sort(L)
print('After we finish:',L) # L is untouched!!!!

# Key little idea: there are two variables called L
# -- one with no indenting (global L)
# -- one that only exists within the function (local L)


# We need to understand when copies are made.
print('Understanding ...')
A = [5,7,11,13]
print(A)
B = A[1:3]
print(B)
B[0] = 999999
print(B)
# is B a copy of the slice or is B a window into A?
print(A)
# Conclusion: slices are a copy!

C = A
print(C)
C[1] = 88888
print(C)
# is C a copy of A or is C a window into A?
print(A)
# Conclusion: C=A did NOT make a copy, called a "view"
# C is pointing at the same bit of memory as A

C = A[:] # will make a copy
C = A.copy() # will make a copy [this one is clear]


# Break time: come back at 11:50am


A = [5,7,11,13]
C = A
print(id(A)) # memory location
print(id(C)) 


#---
# 3. More on loops (convert for loop to while loop, break)

print('@@@@@@@')
for a in range(0,4):
    # start of block (body of loop)
    print(a)
    # end of block

# easy to translate a for loop into a while loop
a = 0
while (a<4):
    # start of block (body of loop)
    print(a)
    # end of block
    a = a+1

# Why?
# *for* loop is used when we know exactly how many times it
#   with run through the loop body
# *while* is used when we keep running through the body body
#   until something happens

# we can use the "break" statement/instruction to drop out
# of a loop (either for, while)
# -- but break is bad practice, try your best to avoid it



def insertion_sort_version2(L_input):
    """Sort a list of values into ascending order
    using Insertion Sort"""
    L = L_input.copy()
    for i in range(1,len(L)):
        # suppose we have sorted left part L[0:i]
        #   not including index i
        # right part is L[i:]
        print('---- top of loop ----')
        print('Left-part is ',L[0:i])
        print('Right part is ',L[i:])
        print('Take index',i,' which as value',L[i])
        
        # need ANOTHER loop to scan down the left-part list
        # k loop with scan right-to-left
        
        k = i
        keep_going = True
        while (k>0 and keep_going):
            print('Compare index',k,'with index',k-1)
            print(' --> compare value',L[k],' with value ',L[k-1])
            if (L[k]<L[k-1]):
                print('Swap')
                L[k-1],L[k] = L[k],L[k-1] # multiple assignment
                print('List is now',L)
            else:
                print('No swap needed')
                # --> somehow we need to STOP the k loop!!!!
                keep_going = False
                print('List is now',L)
            k = k-1

L = [6,4,10,8,2,3,5,9]
print('Before we start:',L)
insertion_sort_version2(L)
print('After we finish:',L) # L is untouched!!!!


#---
# 4. Snakes and ladders
import random
def snakes_and_ladders():
    """Play the snakes and ladders
    board game for one player."""
    print('---------------')
    print('Welcome earthling')
    position = 1
    while (position<25):
        print('You are at position:',position)
        # roll the dice
        dice = random.randint(1,6)
        print('dice roll:',dice)
        # update the position
        position = position+dice
        if (position==5):
            print("climb the ladder to 15")
            position = 15
        if (position==12):
            print("climb the ladder to 21")
            position = 21
        if (position==9):
            print("slide down the snake to 4")
            position = 4
        if (position==24):
            print("slide down the slake to 13")
            position = 13
    print("Game over")

snakes_and_ladders()

# incremental development

def snakes_and_ladders_version2():
    """Play the snakes and ladders
    board game for one player."""
    # setup the board
    ladders = { 5: 15,
               12: 21 }
    snakes =  { 9:  4,
               24: 13}
    number_of_squares = 25
    
    print('---------------')
    print('Welcome earthling')
    count_rolls = 0
    count_ladders = 0
    count_snakes = 0

    position = 1
    while (position<number_of_squares):
        print('You are at position:',position)
        # roll the dice
        dice = random.randint(1,6)
        count_rolls = count_rolls+1
        print('dice roll:',dice)
        # update the position
        position = position+dice
        # check for ladder
        if (position in ladders.keys()):
            print("climb the ladder")
            count_ladders = count_ladders+1
            top_of_ladder = ladders[position]
            position = top_of_ladder
            print("  to",position)
        if (position in snakes.keys()):
            print("slide down the snake")
            count_snakes = count_snakes+1
            bottom_of_snake = snakes[position]
            position = bottom_of_snake
            print("  to",position)
    print("Game over")
    result = {'rolls': count_rolls,
              'ladders': count_ladders,
              'snakes': count_snakes}
    return(result)

output = snakes_and_ladders_version2()
print(output)


# Long break time: come back at 1:40pm


all_rolls = []
all_ladders = []
all_snakes = []
for q in range(1000):
    output = snakes_and_ladders_version2()
    all_rolls.append(output['rolls'])
    all_ladders.append(output['ladders'])
    all_snakes.append(output['snakes'])

import matplotlib.pyplot as plt
plt.figure()
plt.plot(all_rolls,all_ladders,'g.',markersize=10)
plt.plot(all_rolls,all_snakes,'r.')
plt.show()


#---
# Question: Can you create a dictionary
# at run time?
# Answer: Yes
a = random.randint(1,10)
b = random.randint(21,30)
D = {}
D[a] = b
print(D)


#---
# Question: How can you avoid using a break?
b = 5
while (b<10):
    print(b)
    if (b==8):
        break
    b = b+1

b = 5
keep_going = True
while (b<10 and keep_going):
    print(b)
    if (b==8):
        keep_going = False
    b = b+1

# -- the end --
