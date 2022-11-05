#!/bin/env python3

from random import randrange
import copy

#1
class Carte():
    valeurs = list(range(7,11)) + ['Valet','Dame','Roi','As']
    couleurs = ['Coeur','Carreau','Pique','Trèfle']
    def __init__(self,v=None,c=None):
        if v:
            self.v=v
            if not v in Carte.valeurs:
                raise ValueError(f"{v}: valeur incorrecte")
        else:
            v = Carte.valeurs[randrange(0,len(Carte.valeurs))]
        if c:
            if not c in Jeu.couleurs:
                raise ValueError(f"{c}: couleur incorrecte")
        else:
            c = Carte.couleurs[randrange(0,len(Carte.couleurs))]
        self.couleur = c
        self.valeur = v
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"
    def __eq__(self,carte):
        return self.valeur==carte.valeur and self.couleur==carte.couleur

#2
class Cartes():
    def __init__(self,autres=None):
        self.deck=[]
        if autres:
            self.deck=copy.copy(autres.deck)
        self.n=len(self.deck)
    def __repr__(self):
        return ", ".join([str(c) for c in self.deck])
    def ajoute(self,c):
        self.deck += [c]
        self.n+=1
    def pioche(self):
        p=randrange(self.n)
        self.deck.remove(self.deck[p])
        self.n-=1
        if self.n==0:
            raise ValueError("pioche vide!")
        return self.deck
    def __isub__(self,carte):
        self.deck.remove(carte)
        self.n-=1
        return self
#3
class Jeu(Cartes):
    valeurs = list(range(7,11)) + ['Valet','Dame','Roi','As']
    couleurs = ['Coeur','Carreau','Pique','Trèfle']
    def __init__(self):
        self.deck=[]
        self.n=32
        for i in Jeu.valeurs:
            for c in Jeu.couleurs:
                self.deck+=[Carte(i,c)]


#4
class Main(Cartes): 
    def __init__(self,jeu):
        Cartes.__init__(self)
        self.paquet=jeu
    def complete(self):
        if self.paquet.n!=0:
            p=randrange(self.paquet.n)
            self.ajoute(self.paquet.deck[p])
            self.paquet-=self.paquet.deck[p]
        else:
            raise ValueError(f"plus de place pour compléter la main {self.deck}")
    def __isub__(self,autmain):
        for i in range(autmain.n):
            self.deck.remove(autmain.deck[i])
            self.n-=1
        return self
#5
class Carre(Main):
    def __init__(self,main):
        Cartes.__init__(self)
        for i in Jeu.valeurs:
            c=0
            for k in range(main.n):
                if main.deck[k].v==i:
                    c+=1
            if c==4 and self.n==0:
                self.ajoute(Carte(i,'Coeur'))
                self.ajoute(Carte(i,'Carreau'))
                self.ajoute(Carte(i,'Pique'))
                self.ajoute(Carte(i,'Trèfle'))
        if self.n==0:
            raise RuntimeError(f"pas de carre dans {main.deck}")
    def __repr__(self):
        if self.n==4:
            return f"carré de {self.deck[0].v}"

#6
class Quinte(Main):
    def __init__(self,main):
        Cartes.__init__(self)
        for i in range(main.n):
            q=0
            v,c=main.deck[i].v,main.deck[i].couleur
            if type(v)==int:                   #On crée nos suites à partir de l'élément le plus peti qui est obligatoirement une carte numérotée
                for k in range(main.n):        #de valeur maximale 10 pour la suite (10,valet,dame,roi,as)
                    if main.deck[k]==Carte(Jeu.valeurs[v-6],c) or main.deck[k]==Carte(Jeu.valeurs[v-5],c) or main.deck[k]==Carte(Jeu.valeurs[v-4],c) or main.deck[k]==Carte(Jeu.valeurs[v-3],c):
                            q+=1                             #Le v-6,v-5,etc permet de choisir les valeurs suivantes correctement dans le tableau Jeu.valeurs
            if q==4 and self.n==0:                           #Les cartes sont numérotées de 7 à 10 tandis que la liste commence en 0, et faire v-7 nous ramène à la valeur actuelle de v située dans Jeu.valeurs
                self.ajoute(Carte(Jeu.valeurs[v-7],c))
                self.ajoute(Carte(Jeu.valeurs[v-6],c))
                self.ajoute(Carte(Jeu.valeurs[v-5],c))
                self.ajoute(Carte(Jeu.valeurs[v-4],c))
                self.ajoute(Carte(Jeu.valeurs[v-3],c))
        if self.n==0:
            raise RuntimeError(f"pas de quinte dans {main.deck}")
    def __repr__(self):
        return f"Quinte {self.deck}"


print(Carte())                      # -> Valet de Trèfle (par exemple)
print(Carte())                      # -> Dame de Coeur (par exemple)
print(Carte())                      # -> 8 de Carreau (par exemple)
carte1 = Carte(7,"Coeur")
print(carte1)                       # -> 7 de Coeur
#carte2 = Carte("Valet","pic")       # -> ValueError: pic: couleur incorrecte
carte3 = Carte("Valet","Pique")
print(carte3) 
    
# 3 cartes
carte1 = Carte("As","Trèfle")
carte2 = Carte(7,"Coeur")
carte3 = Carte("Valet","Pique")
# un ensemble de cartes (vide au départ)
des_cartes = Cartes()
# on y ajoute les 3 cartes
for une_carte in [carte1,carte2,carte3]:
  des_cartes.ajoute(une_carte)
print(f"{des_cartes=}")
# on le clone
les_memes = Cartes(des_cartes)
print(f"{les_memes=}")
# on pioche dedans tant que l'on peut
try:
  while True:
    print(f"{des_cartes.pioche()=}")
    print(f"{des_cartes=}")
    print(f"{les_memes=}")
except ValueError as e:
  # traceback.print_exc(file=sys.stdout)
  print(e)
print("fin de programme")
un_jeu = Jeu()
print(f"{un_jeu=}")
un_jeu -= Carte('Valet','Coeur')
un_jeu -= Carte('As','Pique')
un_jeu -= Carte(10,'Trèfle')
print(f"{un_jeu=}")

le_jeu = Jeu()

# on crée 2 mains vides
ma_main = Main(le_jeu)
ta_main = Main(le_jeu)
print(f"{ma_main=}")
print(f"{ta_main=}")

# on y ajoute 3 cartes
for i in range(3):
  ma_main.complete()
  print(f"{ma_main=}")
  ta_main.complete()
  print(f"{ta_main=}")
print(f"{le_jeu=}")

# on tente d'ajouter 25 cartes à la première
try:
  for i in range(25):
    ma_main.complete()
except ValueError as e:
  print(e)

# on tente dajouter 25 cartes à la seconde
try:
  for i in range(25):
    ta_main.complete()
except ValueError as e:
  # traceback.print_exc(file=sys.stdout)
  print(e)

print("fin de programme")


le_jeu = Jeu()

# une main de 25 cartes
une_main = Main(le_jeu)
for i in range(25):
  une_main.complete()
print(f"{une_main=}")

# recheche tous les carrés contenus dans la main
while True:
  try:
    un_carre = Carre(une_main)               # essai de créer un carré
    # si on est là, c'est qu'un carré a été créé
    print(f"{un_carre=}, {une_main=}")
    une_main -= un_carre                     # on l'enlève de la main
  except RuntimeError as e:
    # si on est là, c'est qu'un carré n'a pas pu être créé
    print(e)
    break

print("fin de programme")

#Recherche de quinte dans un jeu complet
le_jeu = Jeu()
# une main de 32 cartes, soit un jeu complet
une_main = Main(le_jeu)
for i in range(32):
  une_main.complete()
print(f"{une_main=}")

while True:
  try:
    une_quinte = Quinte(une_main)               # essai de créer une quinte
    # si on est là, c'est qu'une quinte a été créée
    print(f"{une_quinte=}, {une_main=}")
    une_main -= une_quinte                     # on l'enlève de la main
  except RuntimeError as e:
    # si on est là, c'est qu'une quinte n'a pas pu être créé
    print(e)
    break                   

print("fin de programme")

