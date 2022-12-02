# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as rnd
import scipy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

#Exercice 1

def f(x):
    return (x[0] - 1)**2 + 10*(x[1] - x[0]**2)**2

def df(x):
    return np.array([40*x[0]*(x[0]**2-x[1]) + 2*(x[0]-1),20*(x[1]-x[0]**2)])
    
def d2f(x):
    return np.array(((2 - 4*10*x[1] + 12*10*x[0]**2, -4*x[0]*10),(-4*10*x[0],    2*10),))
def g(x):
    return x[0]**2 + 2*x[1]**2 +2*x[0]*x[1]
def dg(x):
    return np.array([2*x[0]+2*x[1],4*x[1]+2*x[0]])
def d2g(x):
    return np.array(((2,2),(2,4),))

def Newton(f,df,d2f,x0,tol):
    k=0
    x=x0
    X=[x]
    while np.linalg.norm(df(x))>tol:
        d=np.dot(-np.linalg.inv(d2f(x)),df(x))
        x+=d
        k+=1
        X=np.append(X,[x],axis=0)
    return X,k
"""
x0,tol=np.array([0.,0.]),0.01
X=np.linspace(-1,2,500)
Y=np.linspace(-1,2,500)
XX,YY= np.meshgrid(X,Y)
ZZ = f(np.array([XX,YY]))
plt.contour(XX,YY,ZZ,levels=np.logspace(-3,1,10,base=10),colors='grey')
plt.xlabel('x')
plt.ylabel('y')
X,k=Newton(f,df,d2f,x0,tol)
plt.plot(X[:,0],X[:,1],'-r')
plt.title(f'Méthode Newton et {k} itérations')
"""
"""
x0,tol=np.array([1.,1.]),0.01
X=np.linspace(-1,1,500)
Y=np.linspace(-1,1,500)
XX,YY= np.meshgrid(X,Y)
ZZ = g(np.array([XX,YY]))
plt.contour(XX,YY,ZZ,levels=np.logspace(-3,1,10,base=10),colors='grey')
plt.xlabel('x')
plt.ylabel('y')
X,k=Newton(g,dg,d2g,x0,tol)
plt.plot(X[:,0],X[:,1],'-r')
plt.title(f'Méthode Newton et {k} itérations')   #Marche en 1 itération car g quadratique
"""

#3,4
def wolfe(f,df,d,x,L=10,c1=0.1,c2=0.9,beta=0.5): #d_x est la direction de descente d_x . grad_x <= 0
    # test f(x_new) \leq f(x_0) + c alpha ps{d_x}{grad_x}
    gx=df(x)
    k=0
    m,M=0,np.inf
    h=-gx.dot(d)/(L*np.linalg.norm(d)**2)
    while f(x+h*d)>f(x)+c1*h*gx.dot(d) or  df(x+h*d).dot(d) < c2*df(x).dot(d):
        if f(x+h*d) > f(x)+c1*h*gx.dot(d):
            M=h
            h=(m+M)/2
        else:
            m=h
            if M==np.inf :
                h=10*h
            else :
                h=(m+M)/2
    return h       #pas vérifiant la condition de Wolfe

def Newton_wolfe(f,df,d2f,x0,tol):
    k=0
    x=x0
    T=[x]
    while np.linalg.norm(df(x))>tol:
        d=np.dot(-np.linalg.inv(d2f(x)),df(x))
        h=wolfe(f,df,d,x)
        x+=h*d
        k+=1
        T=np.append(T,[x],axis=0)
    return T,k
"""   
x0,tol=np.array([0.,0.]),0.01
X=np.linspace(-1,2,500)
Y=np.linspace(-1,2,500)
XX,YY= np.meshgrid(X,Y)
ZZ = f(np.array([XX,YY]))
plt.contour(XX,YY,ZZ,levels=np.logspace(-3,1,10,base=10),colors='grey')
plt.xlabel('x')
plt.ylabel('y')
X,k=Newton_wolfe(f,df,d2f,x0,tol)
plt.plot(X[:,0],X[:,1],'-r')
plt.title(f'Méthode Newton pas de Wolfe et {k} itérations')
"""
"""
x0,tol=np.array([1.,1.]),0.01
X=np.linspace(-1,1,500)
Y=np.linspace(-1,1,500)
XX,YY= np.meshgrid(X,Y)
ZZ = g(np.array([XX,YY]))
plt.contour(XX,YY,ZZ,levels=np.logspace(-3,1,10,base=10),colors='grey')
plt.xlabel('x')
plt.ylabel('y')
X,k=Newton_wolfe(g,dg,d2g,x0,tol)
plt.plot(X[:,0],X[:,1],'-r')
plt.title(f'Méthode Newton pas de Wolfe et {k} itérations')
"""
#Newton classique converge plus vite qu'avec le pas de Wolfe


#Exercice 2
"""
def BFGS(f,df,x0,tol):
    k,x=0,x0
    B=np.eye(len(x))
    X=[x]
    while np.linalg.norm(df(x))"""
    
#Exercice 3: Taper "wikipédia gauss newton sur internet"
#1

t = np.array([0.038,0.194,.425,.626,1.253,2.500,3.740])
y = np.array([0.050,0.127,0.094,0.2122,0.2729,0.2665,0.3317])
xopt=np.array((0.362,0.556))
x0=np.array((0.9,0.2))
def v(t,x):
    return x[0]*t/(x[1]+t)
plt.scatter(t,y)
plt.plot(np.linspace(0,4,50),v(np.linspace(0,4,50),xopt))
x=x0
x0,tol=np.array((0.9,0.2)),0.0001
#2
def r(x):  #résidu
    return y-v(t,x)
def J(x): #transposée du Jacobien de r
    return np.array((-t/(x[1]+t),x[0]*t/(x[1]+t)**2)).T
def GN(x0,tol): #algorithme Gauss Newton
    x,k=x0,0
    T=np.array([x])
    while np.linalg.norm(r(x).dot(J(x))) > tol and k <100:
        x= x-np.linalg.inv(np.transpose(J(x)).dot(J(x))).dot(np.transpose(J(x)).dot(r(x)))
        T,k=np.append(T,[x],axis=0),k+1
    return T , k
GN(x0,tol)  #rend les estimations de l'exemple wikipédia

#3
a,b,c=5,0.1,0.1
xopt=np.array((a,b,c))

def m(t,x):
    return x[0]*np.exp(-x[1]*t)*np.sin(x[2]*2*math.pi*t)

t2=np.arange(0,21,2)
y2=m(t,xopt)+0.1*np.random.randn(11)
plt.scatter(t,y2)
plt.plot(np.linspace(0,20,100),m(np.linspace(0,20,100),xopt))

def r2(x):  #résidu
    return y2-m(t,x)
print(r2(x0))

def J2(x): #transposée du Jacobien de r
    A=-np.exp(-x[1]*t2)*np.sin(x[2]*2*math.pi*t2)
    B=x[0]*t*np.exp(-x[1]*t2)*np.sin(x[2]*2*math.pi*t2)
    C=-2*math.pi*t2*x[0]*np.exp(-x[1]*t2)*np.cos(x[2]*2*math.pi*t2)
    return np.array((A,B,C)).T
print(J2(x0))

def GN2(x0,tol): #algorithme Gauss Newton
    x,k=x0,0
    T=np.array([x])
    while np.linalg.norm(r2(x).dot(J2(x))) > tol and k <100:
        x= x-np.linalg.inv(np.transpose(J2(x)).dot(J2(x))).dot(np.transpose(J2(x)).dot(r2(x)))
        T,k=np.append(T,[x],axis=0),k+1
    return T , k
x0=np.array((5.2,0.2,0.1))
tol=0.1
T2,k2=GN2(x0,tol)

plt.scatter(t2,y2)
plt.plot(np.linspace(0,20,500),m(np.linspace(0,20,500),T2[k2-1]))



