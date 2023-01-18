#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
import matplotlib.pyplot as plt

#2)
lamb=2
n=100000
p=lamb/n

def f(x):
    return lamb*np.exp(-lamb*x)


X=np.linspace(0,10)
Y=f(X)

Xn=np.random.geometric(lamb/n,n)/n

plt.plot(X,Y,"r",label="Densité exponentielle")
plt.hist(Xn,density=True,label="Densité empirique",bins=200)
plt.xlim(0,3)
plt.legend()

#3)
F={0,1,2}
pas=20
P=np.array(([0.1,0.6,0.3],[0.4,0.2,0.4],[0.5,0,0.5]))
Z=[0]
for i in range(pas):
    d=random.random()
    if d<=P[Z[i]][0]:
        Z.append(0)
    elif d<=P[Z[i]][0]+P[Z[i]][1]:
        Z.append(1)
    else:
        Z.append(2)
    print(d)
print(Z)

#5)
n=10000
def sigm(x):
    Z=x
    s=0
    while Z==x:
        s+=1
        d=random.random()
        if d<=P[Z][0]:
            Z=0
        elif d<=P[Z][0]+P[Z][1]:
            Z=1
        else:
            Z=2
    return s

X=[sigm(0) for i in range(n)]
G=np.random.geometric(1-P[0][0],n)
 
plt.hist(X,density=True,label="Densité empririque")       
plt.hist(G,density=True,label="Densité géométrique",alpha=0.5)
plt.legend()

#6)
k=0

