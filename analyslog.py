#!/bin/env python3
import re
import multiprocessing as mp


val=re.compile(r"bout de (.*) second")
unite,i=1,0   #Changer unite en 1 si on souhait prendre la seconde comme unité de temps ou 0 pour prendre la première valeur lue
q = mp.Queue()
indice=mp.Queue()

f=open("logtime.log","r")
for line in f: 
    if re.findall(val,line)!=[]:
        temps=float(re.findall(val,line)[0])
        if unite==0:
            unite=temps
            q.put(1)
            indice.put(i)
        else:
            n=int(temps/unite)
            if n==0: n+=1
            q.put(n)
            indice.put(i)
        i+=1
f.close()

# vidage
while q.qsize()>0:
  n = q.get(block=True)
  i=indice.get(block=True)
  obj=''
  for j in range(n): obj+='|'
  print(f"{i}: {obj}")
