# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:10:31 2022

@author: USER
"""


# list

L = [None, 'red', True, 17,3.45,['a','b'],{3,4,5}]
print(L)

print(L[3:6])
L[2] = False
print(L)
print(L[-1])
L[-1].add(6)
print(L)

# Set

fruit = {'mango', 'apple', 'pineapple', 'watermelon', 'strawberry'}
print(fruit)
print('mango' in fruit)
fruit.remove('apple')
print(fruit)

#  Dictionary(Look for things)

house = {'chair': 'Living room',
         'table': 'dinning room',
         'jewelery': 'second drawer down',
         'blender': 'cupboard',
         'bed': 'bedroom #01',
         'rent': '100',
         'occupants': '5',
         'temparature': 18.4}

print(house)
print(house['rent'])

for k in house:
    print(k, house[k])
print(list(house.keys))