#!/bin/env python3
import time
import random


dp=0.05
class Torche:
    def __init__(self):
        self.A="Off"
        self.B="Vert"
        self.d=abs(random.uniform(-dp,+dp))
    def pushA(self):
        if self.A=="Off":
            self.A="On"
        else: 
            self.A="Off"
        return self
    def pushB(self):
        if self.B=="Vert":
            self.B="Orange"
        elif self.B=="Orange":
            self.B="Rouge"
        elif self.B=="Rouge":
            self.B="Auto"
            self.temps=time.time()
        else:
            self.B="Vert"
        
    def __str__(self):
        if self.A=="Off":
            print(1)
            return self.A
        else:
            if self.B=="Auto":
                fin=(time.time()-self.temps)*(1+self.d)+random.uniform(-self.d,self.d)
                if((fin)%3<=1):
                    return("Vert")
                elif((fin)%3<=2):
                    return("Orange")
                elif((fin)%3<=3):
                    return("Rouge")         
            else:
                return self.B 

"""Question 1
t = Torche() ; print(t)       # Off
t.pushA() ; print(t)          # Vert
t.pushB() ; print(t)          # Orange
t.pushB() ; print(t)          # Rouge
t.pushA() ; print(t)          # Off
t.pushB() ; print(t)          # Off
t.pushB() ; print(t)          # Off
t.pushA() ; print(t)          # Orange
t.pushB() ; print(t)          # Rouge
t.pushB() ; print(t)          # Vert
t.pushB() ; print(t)          # Orange
t.pushB() ; print(t)          # Rouge"""

"""Question 2
t = Torche()
t.pushA()
t.pushB()
t.pushB()
t.pushB()
while True:
  print(t)"""

# création des 3 torches
t1 = Torche()
t2 = Torche()
t3 = Torche()

# allumage et mise en position 4
for t in [t1, t2, t3]:
    t.pushA()
    for i in range(3):
        t.pushB()

# observation de la dérive des horloges
while True:
    print(f"{t1} {t2} {t3}")
