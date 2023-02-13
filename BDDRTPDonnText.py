#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Données textuelles :Charsets et encoding

import encodings

#ch1

print(" ", end="   ")
for i in range(0,0x8):
    print(f"{i:1x}", end="   ")
print()

for i in range(0,0x10):
    print(f"{i:1x}: ", end=" ")
    for j in range(0,0x10):
        code = i+j*0x10
        car = chr(code)
        if not car.isprintable(): car = " "
        print(car, end="   ")
    print()

#ch3
c=b"\x41\x42\x43\xE9\xE8\xC5"
for i in range (1,8):
    print(c.decode(encoding=f"iso8859-{i}"))
for i in range (9,12):
    print(c.decode(encoding=f"iso8859-{i}"))
for i in range (13,16):
    print(c.decode(encoding=f"iso8859-{i}"))

#ch4
c=b"\xA4"
print(c.decode(encoding="iso8859-1"))
print(c.decode(encoding="iso8859-15"))

#ch5

def charset(codec):
  print(f"** {codec} **")

  # ligne d'en-tête
  print(" ", end="   ")
  for i in range(0,0x10):          # chaque colonne
      print(f"{i:1X}", end="   ")  # indice de colonne
  print()

  for i in range(0,0x10):           # chaque ligne
      print(f"{i:1X}: ", end=" ")   # indice de ligne
      for j in range(0,0x10):       # chaque case de la ligne
          code = i+j*0x10
          byte = bytes([code])
          car = byte.decode(encoding=codec, errors='replace')
          if not car.isprintable(): car = " "
          print(car, end="   ")
      print()

charset("iso8859-1")

#ch6
def diffcodepage(codec1,codec2):
  print(codec1," - ",codec2)

  print(" ", end="   ")
  for i in range(0,0x10):
      print(f"{i:1x}", end="   ")
  print()

  for i in range(0,0x10):
      print(f"{i:1x}: ", end=" ")
      for j in range(0,0x10):
          code = i+j*0x10
          byte = bytes([code])
          car1 = byte.decode(encoding=codec1, errors='replace')
          car2 = byte.decode(encoding=codec2, errors='replace')
          if not car1.isprintable() or car1==car2: car = " "
          print(car1, end="   ")
      print()
      
diffcodepage("iso8859-1", "iso8859-15")  

#ch7

fn = input("file name: ")
encod= input("encodage:")
with open(fn, "rb") as f:
    byte = f.read(1)
    while byte:
        print(byte.decode(encoding=encod),end="")
        byte = f.read(1)


