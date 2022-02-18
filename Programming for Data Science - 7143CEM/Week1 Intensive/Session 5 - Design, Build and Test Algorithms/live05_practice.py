# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 22:55:00 2022

@author: USER
"""

# Insertion Sort

def insertion_sort(L_input):
    """Sort a list of values into ascending order
    using Insertion Sort"""
    L = L_input.copy()
    for i in range(1, len(L)):
        
        print('---- top of loop ----')
        print('Left-part is :', L[0:i])
        print('Right-part is :', L[i:])
        print('Take index ',i, 'which as value', L[i])
        
        for k in range(i,0,-1):
            print('Compare index',k, 'with index',k-1)
            print('---> compare value', L[k], 'with value', L[k-1])
            if (L[k]<L[k-1]):
                print('Swap')
                L[k-1],L[k] = L[k],L[k-1] # multiple swap
                print('list is now', L)
            else:
                print('No Swap needed')
                print('list is now', L)
        
L = [6,4,10,8,2,3,5,9]
print('Before we Start :', L)
insertion_sort(L)
print('After we finish:',L)



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

