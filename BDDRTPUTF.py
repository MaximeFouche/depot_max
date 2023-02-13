#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Données textuelles: Unicode

#ch3
a="&@àéα€"

"""

Carcatère   Code point hexadéc  Code point bin  Nb de bits du code point Nb d'octets du code UTF-8 Code UTF-8 bin  Code UTF-8 hexadéc     

&           U+0026              100110          6                        1
@           U+0040              1000000         7                        1 
à           U+00E0              11100000        8                        2                         11000011 10100000
€           U+20AC              10000010101100  14                       3 

"""

#ch4
import unicodedata
c1="\u0049"
c2="\u2160"
print(c1,c2)
print(unicodedata.name(c1),unicodedata.name(c2))
print(unicodedata.category(c1),unicodedata.category(c2))

c1="\u0041"
c2="\u0391"
print(c1,c2)
print(unicodedata.name(c1),unicodedata.name(c2))
print(unicodedata.category(c1),unicodedata.category(c2))

c1="\u004C"
c2="\u216C"
print(c1,c2)
print(unicodedata.name(c1),unicodedata.name(c2))
print(unicodedata.category(c1),unicodedata.category(c2))

c="\u039C"
print(unicodedata.name(c))
print(unicodedata.category(c))
print(c) #doit être la lettre grecque mu en majuscule 

