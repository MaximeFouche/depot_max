#!/bin/env python3

import asyncio
import numpy as np

class Accessoire():
    def __init__(self):
        self.contenu=[]

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def embrocher(self,postit):
        self.contenu.append(postit)
        return self.contenu
    def liberer(self):
        postit=self.contenu[-1]
        np.delete(self.contenu,-1)
        return postit

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    def recevoir(self,plateau):
        self.contenu.append(plateau)
        return self.contenu
    def evacuer(self):
        plateau=self.contenu[-1]
        np.delete(self.contenu,-1)
        return plateau

class Serveur:
    def __init__(self,pic,bar,commandes):
        self.plateau=[]
    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        postit=
        pic.embrocher(postit)
    def servir(self):
        """ Prend un plateau sur le bar. """
        

class Barman:
    def __init__(self,pic,bar):
        self.pic=[]
        self.bar=[]
    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        ...