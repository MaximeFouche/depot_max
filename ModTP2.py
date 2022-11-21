# -*- coding: utf-8 -*-

#TP2

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.special import factorial
from math import exp


"""Exercice 1"""

def pseudoal(a,b,N,n):
    y=int(N*random.random())
    x=y/N
    X=[x]
    for i in range(1,n):
        y=(a*y+b)%N
        x=y/N
        X.append(x)
    return X

a,b,N,n=16807,0,2**31-1,1000
X=pseudoal(a, b, N, n)
plt.hist(X,density="True")

"""Exercice 2"""
def marchal(p1,p2,p3,p4,n):
    x,y=0,0
    X,Y=[x],[y]
    for i in range(n):
        a=random.random()
        if a<p1:
            x+=1
        elif a<p1+p2:
            y+=1
        elif a<p1+p2+p3:
            x-=1
        else:
            y-=1
        X.append(x)
        Y.append(y)
    return X,Y

p1,p2,p3,p4=0.25,0.25,0.25,0.25
n=1000000
X,Y=marchal(p1, p2, p3, p4, n)
plt.plot(X,Y,'b')
plt.show()   

"""Exercice 3"""
#1
def Poisson(lamb):
    pk=0
    k=0
    U=random.random()
    while (pk<U): 
        pk+=((lamb**k)/factorial(k))*exp(-lamb)
        k+=1
    pkfinal=((lamb**k)/factorial(k))*exp(-lamb)
    return k,pkfinal

lamb=1
print(Poisson(lamb))


#2 et 3
def Poissonmult(N,lamb):
    X=np.zeros(N)
    Y=np.zeros(N)
    for i in range(N):
        K=Poisson(lamb)
        X[i]=K[0]
        Y[i]=K[1]
    return X,Y

N=10000
lamb=10
Y,X=Poissonmult(N, lamb)
#X donne la vraie densité vers laquelle les N variables tendent, Y est juste un amas de résultats pas proportionnés
A=[]
i=0
while not IndexError:
    k=Y.count(i) #Faux, trouver la fonction correspondante pour compter les occurences dans un array
    A.append(k)    
print(f"loi exacte: {X}")
print(f"loi simulée: {A}") 
plt.hist(X,label="loi exacte", alpha=0.5)
plt.hist(A,label="loi simulée",alpha=0.7)
plt.legend()

     
    
