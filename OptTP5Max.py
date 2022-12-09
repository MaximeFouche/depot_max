# -*- coding: utf-8 -*-

import numpy as np


def f(x):
    return x[0]**2 +x[1]**2 -x[0]*x[1] +x[1]

def df(x):    
    return np.array([2*x[0]-x[1], 2*x[1]-x[0]+1])

def PK(x):
    return np.array([x[0]+(1/5)*(1-2*x[1]+4*x[0]),1/2-(1/5)*(1-2*x[1]+4*x[0])])


def GP(f,df,PK,x0,tol):
    pas=0.001
    x=np.copy(x0)
    Y=np.array([x])
    x=PK(x)
    X=np.array([x])
    diff=1
    compt=0
    while diff>tol:
        y=x-pas*df(x)
        xk=PK(y)
        X=np.append(X,[x],axis=0)
