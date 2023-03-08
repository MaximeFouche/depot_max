#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy.random as npr
import numpy as np
import math as m
import copy
import matplotlib.pyplot as plt

#1)
l=0.01

def exp(l):
    return -np.log(npr.rand())/l


def yule(x,tf):
    y=x
    t=0
    X=[y]
    Tsaut=[t]
    for i in range(1,tf):
        t+=exp(l*X[i-1])
        y+=1
        X+=[y]
        Tsaut+=[t]
    T=np.cumsum(Tsaut)
    return X,T

X,T=yule(2,100)
plt.plot(T,X)   
 

#2)
l=0.02
m=0.03

def file(x,tf):
    y=x
    t=0
    X=[y]
    Tsaut=[t] 
    for i in range(1,tf):
        tl=exp(l)
        tm=exp(m)
        if tl<tm or X[i-1]==0:
            y+=1
            X+=[y]
            Tsaut+=[tl]
        else:
            y+=-1
            X+=[y]
            Tsaut+=[tm]
    T=np.cumsum(Tsaut)
    return X,T
X,T=file(10,100)
plt.plot(T,X)

#la loi invariante existe pour l<m car on rebondit si on atteint 0
#c'est la loi géométrique de paramètre l/m


#3)
l=0.02
m=0.01

def naiss_mort(x,tf):
    i=0
    y=x
    t=0
    X=[y]
    Tsaut=[t] 
    while i<tf and X[i]>0:
        i+=1
        tl=exp(l*X[i-1])
        tm=exp(m*X[i-1])
        if tl<tm or X[i-1]==0:
            y+=1
            X+=[y]
            Tsaut+=[tl]
        else:
            y+=-1
            X+=[y]
            Tsaut+=[tm]
    T=np.cumsum(Tsaut)
    return X,T

X,T=naiss_mort(10,1000)
plt.plot(T,X)

#5)
#p10 la proba d'extinction pour i=10, ne pas oublier que l et m influent sur p10 aussi

l=0.03
m=0.02
morts=0
L=[]
n=50000
for i in range(n):
    print(i)
    X,T=naiss_mort(10,10000)
    L+=[X[len(X)-1]]
    morts+=(X[len(X)-1]==0)
p10=morts/n
print(p10)

#Bonus
a=0.5
m=0.02
def naiss_mort_immig(x,tf):
    i=0
    y=x
    t=0
    X=[y]
    Tsaut=[t] 
    while i<tf:
        i+=1
        tl=exp(a)
        tm=exp(m*X[i-1])
        if tl<tm or X[i-1]==0:
            y+=1
            X+=[y]
            Tsaut+=[tl]
        else:
            y+=-1
            X+=[y]
            Tsaut+=[tm]
    T=np.cumsum(Tsaut)
    return X,T
X,T=naiss_mort_immig(10,10000)
plt.plot(T,X)
