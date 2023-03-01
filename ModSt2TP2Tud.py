#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy.random as npr
import numpy as np
import math as m
import copy
import matplotlib.pyplot as plt

#1)
def exp(l):
    return -np.log(npr.rand())/l

def N(l,n=50):
    i=0
    Ti=0
    Nti=0
    tempssaut=[Ti]
    valeurs=[Nti]
    temps=[]
    while i<n:
        i+=1
        Yi=exp(l)
        Ti+=Yi
        Nti+=1
        tempssaut+=[Ti]
        valeurs+=[Nti]
        temps+=[Yi]
    return tempssaut,valeurs

def Nt(l,t,n=50,Ndonne=None):
    if Ndonne:
        tx,Nx=Ndonne[0],Ndonne[1]
    else:
        tx,Nx=N(l,n)
    test=[[i<=u for u in tx]for i in t]
    iss=[(ti.index(True)) for ti in test]
    return [(Nx[j-1] if j!=0 else 0) for j in iss]

tis,Nis=N(0.08)
#plt.scatter(tis,Nis,marker='+')
ts=np.linspace(0,max(tis),1000)
Ns=Nt(0.08,ts,50,Ndonne=[tis,Nis])
plt.plot(ts,Ns)


#2)
def Xt(x,a,l,t):
    def Ntemps(l,t):
        i=0
        Ti=0
        Nti=0
        tempssaut=[Ti]
        valeurs=[Nti]
        temps=[]
        while Ti<t:
            i+=1
            Yi=exp(l)
            Ti+=Yi
            Nti+=1
            tempssaut+=[Ti]
            valeurs+=[Nti]
            temps+=[Yi]
        return tempssaut,valeurs
    def Ntmod(l,t,n=50,Ndonne=None):
        if Ndonne:
            tx,Nx=Ndonne[0],Ndonne[1]
        else:
            tx,Nx=N(l,n)
        test=[[i<=u for u in tx]for i in t]
        iss=[(ti.index(True)) for ti in test]
        N=np.array([(Nx[j-1] if j!=0 else 0)+x for j in iss])
        Fortune=N-a*t
        return Fortune
    tis,Nis=Ntemps(l,t)
    #plt.scatter(tis,Nis,marker='+')
    ts=np.linspace(0,t,1000)
    Ns=Ntmod(0.08,ts,50,Ndonne=[tis,Nis])
    plt.plot(ts,Ns)
    
Xt(6,0.1,0.1,100000)

#3)
def T(x,a,l):
    def Xtemps(x,a,l):
        i=0
        Ti=0
        Nti=x
        tempssaut=[Ti]
        valeurs=[Nti]
        temps=[]
        while i<=2000:
            i+=1
            Yi=exp(l)
            Nti1=Nti-Yi*a
            if Nti1<=0:
                T0=int(round(Ti+Nti/a,0))
                tempssaut+=[T0]
                valeurs+=[0]
                temps+=[T0-Ti]
                return tempssaut,valeurs,T0
                break
            Nti=Nti1
            Ti+=Yi
            Nti=Nti+1
            tempssaut+=[Ti]
            valeurs+=[Nti]
            temps+=[Yi]
        print("pas de ruine avant i=",{i})
        T0=Ti
        return tempssaut,valeurs,T0
    def Ntmod(l,t,n=50,Ndonne=None):
        if Ndonne:
            tx,Nx=Ndonne[0],Ndonne[1]
        else:
            tx,Nx=Xtemps(l,n)
        test=[[i>=u for u in tx]for i in t]
        Nss=[(sum(ti)-1) for ti in test]
        N=np.array([x+nss for nss in Nss])
        Fortune=N-a*t
        return Fortune
    tis,Nis,T0=Xtemps(x,a,l)
    print(f"T0={T0}")
    plt.scatter(tis,Nis,marker='+')
    ts=np.linspace(0,T0,1000)
    Ns=Ntmod(0.08,ts,50,Ndonne=[tis,Nis])
    plt.plot(ts,Ns)

T(6,0.1,0.1)

def simT(x,a,l,nT0=1000):
    def Xtemps(x,a,l):
        i=0
        Ti=0
        Nti=x
        tempssaut=[Ti]
        valeurs=[Nti]
        temps=[]
        while i<=2000:
            i+=1
            Yi=exp(l)
            Nti1=Nti-Yi*a
            if Nti1<=0:
                T0=T0=int(round(Ti+Nti/a,0))
                tempssaut+=[T0]
                valeurs+=[0]
                temps+=[T0-Ti]
                return T0
                break
            Nti=Nti1
            Ti+=Yi
            Nti=Nti+1
            tempssaut+=[Ti]
            valeurs+=[Nti]
            temps+=[Yi]
        print("pas de ruine avant i=",{i})
        T0=float('inf')
        return T0
    stock=[]
    k=0
    while k<=nT0:
        k+=1
        T0=Xtemps(x,a,l)
        stock+=[T0]
    return stock

#6)
Ts=simT(6,0.1,0.08,20000)
vals=sorted(list(set(Ts)))
occs=[Ts.count(v)/len(Ts) for v in vals]
plt.scatter(vals,occs,marker='+')
print(vals)
#print(occs)
print("proba 300 =",occs[vals.index(300)])
print("moyenne =",np.mean(Ts))
print("var =",np.var(Ts))

#Bonus
def Z():
    x=npr.rand()
    if x<=0.5: return 1
    elif x>0.5 and x<=0.75: return 2
    else: return 3

Zk=sorted([Z() for i in range(50)])


def Y(t):
    Y=0
    for i in range(t):
        Y+=Z()
    return Y 
#On remplace Nt par Yt dans Xt

def Xt2(x,a,l,t):
    def Ntemps(l,t):
        i=0
        Ti=0
        Nti=0
        tempssaut=[Ti]
        valeurs=[Nti]
        temps=[]
        while Ti<t:
            i+=1
            Yi=exp(l)
            Ti+=Yi
            Nti+=1
            tempssaut+=[Ti]
            valeurs+=[Nti]
            temps+=[Yi]
        return tempssaut,valeurs
    def Ntmod(l,t,n=50,Ndonne=None):
        if Ndonne:
            tx,Nx=Ndonne[0],Ndonne[1]
        else:
            tx,Nx=N(l,n)
        test=[[i<=u for u in tx]for i in t]
        iss=[(ti.index(True)) for ti in test]
        N=np.array([Y(j)+x for j in iss])
        Fortune=N-a*t
        return Fortune
    tis,Nis=Ntemps(l,t)
    #plt.scatter(tis,Nis,marker='+')
    ts=np.linspace(0,t,1000)
    Ns=Ntmod(0.08,ts,50,Ndonne=[tis,Nis])
    plt.plot(ts,Ns)
Xt2(6,0.1,0.1,100000)
