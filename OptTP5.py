# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:32:21 2021

@author: utilisateur
"""
import numpy as np
import matplotlib.pyplot as plt


def f(x) :
    return x[0]**2 + x[1]**2 - x[0]*x[1] + x[1]
def df(x) :
    return np.array((x[0]*2 - x[1], x[1]*2 - x[0] + 1))

def h(x) :
    return x[0]+2*x[1]-1
def dh(x) :
    return np.array(( 1,2))

def PK(x): 
    return np.array((x[0]+(1-x[0]-2*x[1])/5,x[1]+2*(1-x[0]-2*x[1])/5))

PK(np.array([0,0]))


def GC(f,df,PK,x0):
    epsilon = 0.001
    rho =  0.01 #pas fixe
    Y=np.array([x0])
    x0=PK(x0)
    X=np.array([x0])
    Y=np.append(Y,[x0],axis=0) 
    diff = 1
    iter = 0
    while diff > epsilon :
        y=x0-rho*df(x0) # descente gradient à pas fixe
        x = PK(y) # projection sur le convexe
        X=np.append(X,[x],axis=0)
        Y=np.append(Y,[y],axis=0) 
        Y=np.append(Y,[x],axis=0)
        iter += 1
        diff = ((x[0]-x0[0])**2+(x[1]-x0[1])**2)**0.5
        x0 = x        
        if iter % 100 == 0 :
            print (iter,diff, f,x0)
    return iter,X,Y 

x0=np.array((1,1))
GC(f,df,PK,x0)


x=np.linspace(-2,1,500)
y=np.linspace(-2,1,500)
X,Y= np.meshgrid(x,y)
Z = f(np.array((X,Y)))
np.min(Z)
np.max(Z)
plt.contour(X,Y,Z,colors='grey')
t=np.linspace(-2,1)
plt.plot(t,(1-t)/2,'-b')
k,X,Y=GC(f,df,PK,x0)    
plt.plot(Y[:,0],Y[:,1])
plt.axis('equal')




def AH(f,df,h,dh):
    x  = np.random.rand(2)
    p  = np.random.rand()
    X=np.array([x])
    epsilon = 1e-10
    rho1,rho2=  0.1,0.1
    diff = 1
    iter = 0
    while diff > epsilon :
        x    = x - rho1*(df(x)+ p*dh(x))
        X=np.append(X,[x],axis=0)
        p = p + rho2 * h(x)
        iter += 1
        diff = np.abs(h(x))
    return x,p,iter,X 



x=np.linspace(-2,1,500)
y=np.linspace(-2,1,500)
X,Y= np.meshgrid(x,y)

Z = f(np.array((X,Y)))
np.min(Z)
np.max(Z)
plt.contour(X,Y,Z,colors='grey')
#plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
x,p,k,X=AH(f,df,h,dh)
plt.plot(X[:,0],X[:,1],'-r')
t=np.linspace(-2,1)
plt.plot(t,(1-t)/2,'-b')
plt.title('Algorithme d Arrow-Hurwitz')





