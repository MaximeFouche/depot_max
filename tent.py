# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 23:29:40 2022

@author: fouch
"""
import numpy as np
import scipy.linalg as sc


#Question 5
def remontee(A,b):
    x = np.copy(b)
    n = len(b)
    for i in range(n-1, -1, -1):
        x[i] = x[i] - A[i][i+1:n] @ x[i+1:n]
        x[i] = x[i] / A[i][i]
    return x


def descente(A,b):
    x = np.copy(b)
    n = len(b)
    for i in range(n):
        x[i] = x[i] - A[i][:i] @ x[:i]
        x[i] = x[i] / A[i][i]
    return x


def LU2(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    for j in range(n):
        for k in range(j,n):
            U[j][k] = A[j][k] - L[j,:j] @ U[:j,k]
        
        for k in range(j+1, n):
            L[k][j] = 1/U[j][j] * (A[k][j] -L[k,:j] @ U[:j,j])
    return L,U



def MatriceA(n,tau):
    t = np.arange(n)
    V = 1 / (1 + t**2 * tau**2)
    A = np.eye(n)
    for i in range(1,n):
        d = np.diagflat((n - i)*[V[i]], i)
        A += d + d.T
    return A

def makeP():    
    P=np.eye(20)
    for i in range(1,20):
        if i==6 or i==7 or i==14 or i==15 or i==16 or i==17:
            P[i,i]=0
    return P

A = MatriceA(20,1)
pi = np.ones(20)
P=makeP()
L,U = LU2(A)
y = descente(L, pi)
x1 = remontee(U,y)

print(x1,P@x1)
C=P@A.T
print(C.T@C)
xp=P@x1
print(P@A@xp,P@pi)



print(np.allclose(A@x1, pi)) # True
print(np.allclose(P@A@xp, P@pi))
print(np.allclose(P@x1, x1))


#Question 6

G=C.T@C
print(G)
L2,U2=LU2(G)
y2=descente(L2,C.T@pi)
x2=remontee(U2,y2)
print(x2)
print(np.allclose(G@x2, C.T@pi)) 
print(np.allclose(P@x2, x2))   #Le but est d'avoir True aux deux

#Test
B=MatriceA(4,1)
P2=np.eye(4)
P2[2,2]=0
print(P2)
C2=B@P2.T
print(C2)
G2=C2.T@C2
print(G2)
L3,U3=LU2(G2)
print(L3,U3)
