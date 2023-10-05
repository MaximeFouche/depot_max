#!/bin/env python3

import asyncio
import sys,time, datetime
import numpy as np
import logging

t0=time.time()
logging.basicConfig(level=logging.DEBUG,
                    filename="cocktail.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %()s')

class Accessoire():
    def __init__(self):
        self.contenu=[]

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def embrocher(self,postit):
        self.contenu.append(postit)
        if verbo!=0:
            print(f"[{self.__class__.__name__}] ({time.time()-t0}) post-it '{postit}' embroché")
            if verbo==2:
                print(f"[{self.__class__.__name__}] ({time.time()-t0}) état={self.contenu}")
        logging.info(f"Le post-it {postit} fut embroché au bout de {time.time()-t0} secondes")
        return self.contenu
    def liberer(self):
        if len(self.contenu)==0:
            if verbo ==2: print(f"[{self.__class__.__name__}] ({time.time()-t0}) état={self.contenu}")
            print(f"({time.time()-t0}) Pic est vide")
            logging.info(f"Le pic est vide au bout de {time.time()-t0} secondes")
        else:
            postit=self.contenu[-1]
            if verbo!=0:
                if verbo==2:
                    print(f"[{self.__class__.__name__}] ({time.time()-t0}) état={self.contenu}")
                print(f"[{self.__class__.__name__}] ({time.time()-t0}) post-it '{postit}' libéré")
            self.contenu=np.delete(self.contenu,-1)
            logging.info(f"Le post-it {postit} fut libéré au bout de {time.time()-t0} secondes")
            return postit


class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    def recevoir(self,plateau):
        self.contenu.append(plateau)
        if verbo!=0:
            print(f"[{self.__class__.__name__}] ({time.time()-t0}) '{plateau}' reçu")
            if verbo==2:
                print(f"[{self.__class__.__name__}] ({time.time()-t0}) état={self.contenu}")
        logging.info(f"Le plateau {plateau} fut reçu par le bar au bout de {time.time()-t0} secondes")
        return self.contenu
    def evacuer(self):
        if len(self.contenu)==0:
            if verbo==2 : print(f"[{self.__class__.__name__}] ({time.time()-t0}) état={self.contenu}")
            logging.info(f"Le bar est vide au bout de {time.time()-t0} secondes")
            print(f" ({time.time()-t0}) Bar est vide")
        else:
            plateau=self.contenu[-1]
            if verbo!=0:
                if verbo==2:
                    print(f"[{self.__class__.__name__}] ({time.time()-t0}) état={self.contenu}")
                print(f"[{self.__class__.__name__}] ({time.time()-t0}) '{plateau}' évacué")
            self.contenu=np.delete(self.contenu,-1)
            logging.info(f"Le plateau {plateau} fut évacué du bar au bout de {time.time()-t0} secondes")
            return plateau

class Serveur:
    def __init__(self,pic,bar,commandes):
        self.plateau=[]
        print(f"[{self.__class__.__name__}] ({time.time()-t0}) prêt pour le service!")
        logging.info(f"Le serveur est prêt au bout de {time.time()-t0} secondes")
    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        for i in commandes:
            print(f"[{self.__class__.__name__}] ({time.time()-t0}) je prends commande de '{i}'" )
            logging.info(f"La commande {i} est prise par le serveur au bout de {time.time()-t0} secondes")
            pic.embrocher(i)
        if verbo!=0:
            if verbo==2:
               print(f"[{self.__class__.__name__}] ({time.time()-t0}) il n'y a plus de commande à prendre ")
            logging.info(f"Le serveur n'a plus de commandes à prendre au bout de {time.time()-t0} secondes")
            print(f" ({time.time()-t0}) plus de commande à prendre")
    def servir(self):
        """ Prend un plateau sur le bar. """
        for i in bar.contenu:
            com=bar.evacuer()
            logging.info(f"La commande {i} fut servie par le serveur au bout de {time.time()-t0} secondes")
            print(f"[{self.__class__.__name__}] ({time.time()-t0}) je sers '{com}'")
        if verbo!=0: bar.evacuer()

class Barman:
    def __init__(self,pic,bar):
        self.pic=[]
        self.bar=[]
        logging.info(f"Le barman est prêt au bout de {time.time()-t0} secondes")
        print(f"[{self.__class__.__name__}] prêt pour le service!")
    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        for i in pic.contenu:
            com=pic.liberer()
            logging.info(f"La comande {com} est initiée au bout de {time.time()-t0} secondes")
            print(f"[{self.__class__.__name__}] ({time.time()-t0}) je commence la fabrication de '{com}'")
            time.sleep(0.4)
            logging.info(f"La comande {com} est finie au bout de {time.time()-t0} secondes")
            print(f"[{self.__class__.__name__}] ({time.time()-t0}) je termine la fabrication de '{com}'")
            bar.recevoir(com)
        if verbo!=0: pic.liberer()
        
#le degré de verbosité, s'il est entré, sera le 1er argument (1 ou 2, le niveau 0 est par défaut)

if __name__=="__main__":  
    t0=time.time()
    if sys.argv[1]=='1' or sys.argv[1]=='2':
        verbo=int(sys.argv[1]) 
        commandes=reversed(sys.argv[2:])
    else:
        verbo=0
        commandes=reversed(sys.argv[1:])
    pic=Pic()
    bar=Bar()
    print(commandes)
    Bob=Barman(pic,bar)
    Steve=Serveur(pic,bar,commandes)
    Steve.prendre_commande()
    Bob.preparer()
    Steve.servir()

