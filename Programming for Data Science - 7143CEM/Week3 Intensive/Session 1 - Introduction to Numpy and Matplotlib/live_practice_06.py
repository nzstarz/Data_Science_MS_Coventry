L = [4,2,7,5,9]
print(L)
print(type(L))
print(L[0])
print(L[2:4])
L[3] = 66

#----------
M = [2,9,7,5,3,4]
print(L)
print(L+M)
# print(L+1) Type Error
print(L+[1])

import numpy
print(numpy. __version__)

import numpy as np
print(np.__version__)

A = np.array([3,7,9,2]) 
print(A)
print(type(A))
print(A.dtype)

B = np.array([1, 'hello'])
print(B)
print(type(B))
print(B.dtype)

C = np.array([4,5,6,10])
print(C)
print(A+C)
print(2*A)

d = 1000000000
print(d)
e = 99999999999999999999999999999999999999999999999
print(e**2)
print(type(e))

F = np.array([9999999999999999999999999999999999999999999999])
print(F)
print(F.dtype)

G = np.array([0,1,2,64])
print(G)
print(G.dtype)


H = np.array([0,1,2,127], dtype=np.int8)
print(H)
print(H.dtype)
print(H+1)


J = np.array([0, 2147483647])
print(J)
print(J+1)


K = np.array([3.14,5.97])
print(K)
print(K.dtype)


L = np.array([True, False, True, 1==5])
print(L)
print(L.dtype)

A = np.array([1,2,3])
print(A)
print(A**2)
print(4*A**2 +3*A+9)

B= (A>2)
print(B)
print(2**A)
print(2**(2**A))
C= list(range(3,10))
print(C)

D = np.arange(3,10)
print(D)

E = np.arange(-np.pi, np.pi, 0.01)
print(E)
print(np.sin(E))


import random
d = random.randint(1, 6)
print(d)

L = []
for i in range(100):
    d = random.randint(1, 6)
    L.append(d)
print(L)

print('week 3: ')
D = np.random.randint(1,6,100)
print(D)


print(np.min(D))
print(np.max(D))
print(np.sum(D))
print(np.mean(D))
print(np.std(D))
print(D.min())

E = np.array([2,3,5,7,11,13,17,23])
print(E)
print(E[3:6])


G = E[3:6]
print(G)
G[1] = 66666
print(G)
print(E)

E = np.array([2,3,5,7,11,13,17,23])
H = E[3:6].copy()
print(H)
H[1] = 99999999
print(H)
print(E)







W = np.array([[1,2,3],[4,5,6]])
print(W)
print(W.shape)
print(W.ndim)


# Matplotlib

import matplotlib
print(matplotlib. __version__)

import matplotlib.pyplot as plt

food = ['sushi', 'steak', 'pizza', 'meat', 'ice cream' ]
price = [8, 5, 2, 3, 4]      


plt.figure()
plt.bar(food, price)
plt.xlabel('Food item')
plt.ylabel('Price')
plt.title('Price of the different food Item')
plt.grid()
plt.show()

plt.figure()
plt.barh(food,price)
plt.show()


x = np.array([1,3,8])
y = np.array([-4,6,2])
plt.figure()
plt.plot(x,y, 'g.', markersize=20)
plt.plot(x,y, 'r-.', linewidth=5)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid()
plt.show()


# Missing Data

a = np.nan
print(a)
Z = np.array([1,2,5, np.nan, 8,3])
print(Z)
print(np.mean(Z))
print(np.sum(Z))
print(np.nanmean(Z))
print(np.nansum(Z))

# Taste of Pandas

import pandas
print(pandas. __version__)

import pandas as pd
H = [0.60, 1.30, 0.90, 1.37]
S = pd.Series(H)
print(S)

print(S.dtype)
plt.figure()
S.plot.line()
plt.show()