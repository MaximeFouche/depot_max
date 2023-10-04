#!/bin/env python3

import asyncio
import sys,time
import numpy as np

class Accessoire():
    def __init__(self,verbo):
        self.contenu=[]
        self.verbo=verbo

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def embrocher(self,postit):
        self.contenu.append(postit)
        if verbo==1 or verbo==2:
            print(f"[{self.__class__.__name__}] {postit} embroché")
            if self.verbo==2:
                print(f"[{self.__class__.__name__}] état= {self.contenu}")
        return self.contenu
    def liberer(self):
        postit=self.contenu[-1]
        if verbo==1 or verbo==2:
            if self.verbo==2:
                print(f"[{self.__class__.__name__}] état= {self.contenu}")
            print(f"[{self.__class__.__name__}] {postit} libéré")
        self.contenu=np.delete(self.contenu,-1)
        return postit

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    def recevoir(self,plateau):
        self.contenu.append(plateau)
        if self.verbo==1 or self.verbo==2:
            print(f"[{self.__class__.__name__}] {plateau} reçu")
            if verbo==2:
                print(f"[{self.__class__.__name__}] état= {self.contenu}")
        return self.contenu
    def evacuer(self):
        plateau=self.contenu[-1]
        if self.verbo==1 or self.verbo==2:
            if verbo==2:
                print(f"[{self.__class__.__name__}] état= {self.contenu}")
            print(f"[{self.__class__.__name__}] {plateau} évacué")
        self.contenu=np.delete(self.contenu,-1)
        return plateau

class Serveur:
    def __init__(self,pic,bar,commandes):
        self.plateau=[]
        print(f"[{self.__class__.__name__}] prêt pour le service!")
    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        for i in commandes:
            print(f"[{self.__class__.__name__}] je prends commande de {i}" )
            pic.embrocher(i)
        if verbo==1 or verbo==2:
            if verbo==2:
               print(f"[{self.__class__.__name__}] il n'y a plus de commande à prendre ")
            print(f"plus de commande à prendre")   
    def servir(self):
        """ Prend un plateau sur le bar. """
        for i in bar.contenu:
            com=bar.evacuer()
            print(f"[{self.__class__.__name__}] je sers {com}")

class Barman:
    def __init__(self,pic,bar):
        self.pic=[]
        self.bar=[]
        print(f"[{self.__class__.__name__}] prêt pour le service!")
    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        for i in pic.contenu:
            com=pic.liberer()
            print(f"[{self.__class__.__name__}] je commence la fabrication de {com}")
            time.sleep(0.4)
            print(f"[{self.__class__.__name__}] je termine la fabrication de {com}")
            bar.recevoir(com)

if __name__=="__main__":  #le degré de verbosité, s'il est entré, sera le 1er argument (1 ou 2, le niveau 0 est par défaut)
    if sys.argv[1]=='1' or sys.argv[1]=='2':
        verbo=int(sys.argv[1]) 
        commandes=reversed(sys.argv[2:])
    else:
        verbo=0
        commandes=reversed(sys.argv[1:])
    pic=Pic(0)
    bar=Bar(0)
    print(commandes)
    Bob=Barman(pic,bar)
    Steve=Serveur(pic,bar,commandes)
    Steve.prendre_commande()
    Bob.preparer()
    Steve.servir()

