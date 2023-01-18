#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
import matplotlib.pyplot as plt

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
