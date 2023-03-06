#!/bin/env python3
import re
from monappli.models import Client, Page, Hit 

pattern=re.compile(r'^(.*?) .*? .*? (\[.*\]?) (\".*? (.*?) .*?\") .*? .*? (\".*?\") ') #regex à trouver
echecs=[]

with open("/.math_etu/users/2023/ds1/122000483/Documents/access.log","r", encoding="utf-8") as f:
  for line in f:
    print(line)
    found = pattern.search(line.strip())
    if found:
      print(found.groups())
      clienti = Client()
      clienti.client_ip = found.groups()[0]
      clienti.save()
      pagei = Page()
      pagei.page = found.groups()[3]
      pagei.save()
      hiti = Hit()
      hiti.timestamp = found.groups()[1]
      hiti.referer = found.groups()[4]
      hiti.client = clienti
      hiti.page = pagei

    else:
      echecs += [line]

print(f"\nlignes en échec de découpage : \n{echecs}")