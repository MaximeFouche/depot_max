#!/bin/env python3

import asyncio
import sys,time, datetime
import numpy as np
import logging

t0=time.time()
logging.basicConfig(level=logging.DEBUG,
                    filename="cocktail.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Accessoire():
    def __init__(self):
        self.contenu=[]

class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def embrocher(self,postit):
        print(type(self.contenu))
        self.contenu.append(postit)
        if verbo!=0:
            print(f"[{self.__class__.__name__}] post-it '{postit}' embroché")
            if verbo==2:
                print(f"[{self.__class__.__name__}] état={self.contenu}")
        logging.info(f"Le post-it {postit} fut embroché au bout de {time.time()-t0} secondes")
        return self.contenu
    def liberer(self):
        if len(self.contenu)==0:
            if verbo ==2: print(f"[{self.__class__.__name__}] état={self.contenu}")
            print(f"Pic est vide")
            logging.info(f"Le pic est vide au bout de {time.time()-t0} secondes")
        else:
            if verbo!=0:
                if verbo==2:
                    print(f"[{self.__class__.__name__}] état={self.contenu}")
                print(f"[{self.__class__.__name__}] post-it '{self.contenu[-1]}' libéré")
            postit=self.contenu.pop(-1)
            logging.info(f"Le post-it {postit} fut libéré au bout de {time.time()-t0} secondes")
            return postit


class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    def recevoir(self,plateau):
        self.contenu.append(plateau)
        if verbo!=0:
            print(f"[{self.__class__.__name__}]   '{plateau}' reçu")
            if verbo==2:
                print(f"[{self.__class__.__name__}] état={self.contenu}")
        logging.info(f"Le plateau {plateau} fut reçu par le bar au bout de {time.time()-t0} secondes")
        return self.contenu
    def evacuer(self):
        if len(self.contenu)==0:
            if verbo==2 : print(f"[{self.__class__.__name__}]   état={self.contenu}")
            logging.info(f"Le bar est vide au bout de {time.time()-t0} secondes")
            print(f"Bar est vide")
        else:
            if verbo!=0:
                if verbo==2:
                    print(f"[{self.__class__.__name__}] état={self.contenu}")
                print(f"[{self.__class__.__name__}] '{self.contenu[-1]}' évacué")
            plateau=self.contenu.pop(-1)
            logging.info(f"Le plateau {plateau} fut évacué du bar au bout de {time.time()-t0} secondes")
            return plateau

class Serveur:
    def __init__(self,pic,bar,commandes):
        self.plateau=[]
        print(f"[{self.__class__.__name__}]   prêt pour le service!")
        logging.info(f"Le serveur est prêt au bout de {time.time()-t0} secondes")
    async def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        while commandes!=[]:
            com=commandes.pop(-1)
            print(f"[{self.__class__.__name__}]   je prends commande de '{com}'" )
            logging.info(f"La commande {com} est prise par le serveur au bout de {time.time()-t0} secondes")
            pic.embrocher(com)
            await asyncio.sleep(2)
        if verbo!=0:
            if verbo==2:
               print(f"[{self.__class__.__name__}] il n'y a plus de commande à prendre ")
            logging.info(f"Le serveur n'a plus de commandes à prendre au bout de {time.time()-t0} secondes")
            print(f"plus de commande à prendre")
    async def servir(self):
        """ Prend un plateau sur le bar. """
        while commandes!=[] or pic.contenu!=[] or bar.contenu!=[]:
            if bar.contenu==[]:
                await asyncio.sleep(5)
            com=bar.evacuer()
            logging.info(f"La commande {com} fut servie par le serveur au bout de {time.time()-t0} secondes")
            print(f"[{self.__class__.__name__}]  je sers '{com}'")
            await asyncio.sleep(5)
        if verbo!=0: bar.evacuer()

class Barman:
    def __init__(self,pic,bar):
        self.pic=[]
        self.bar=[]
        self.actif=False
        logging.info(f"Le barman est prêt au bout de {time.time()-t0} secondes")
        print(f"[{self.__class__.__name__}] prêt pour le service!")
    async def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        while commandes!=[] or pic.contenu!=[]:
            com=pic.liberer()
            logging.info(f"La commande {com} est initiée au bout de {time.time()-t0} secondes")
            print(f"[{self.__class__.__name__}] je commence la fabrication de '{com}'")
            await asyncio.sleep(4)
            logging.info(f"La commande {com} est finie au bout de {time.time()-t0} secondes")
            print(f"[{self.__class__.__name__}] je termine la fabrication de '{com}'")
            bar.recevoir(com)
        if verbo!=0: pic.liberer()
        
#le degré de verbosité, s'il est entré, sera le 1er argument (1 ou 2, le niveau 0 est par défaut)

async def main(): 
    async with asyncio.TaskGroup() as tg:
      task1 = tg.create_task(Steve.prendre_commande())
      task2 = tg.create_task(Bob.preparer())
      task3 = tg.create_task(Steve.servir())

if __name__ == "__main__":
    if sys.argv[1]=='1' or sys.argv[1]=='2':
        verbo=int(sys.argv[1]) 
        commandes=sys.argv[2:]
    else:
        verbo=0
        commandes=sys.argv[1:]
    pic=Pic()
    bar=Bar()
    Bob=Barman(pic,bar)
    Steve=Serveur(pic,bar,commandes)
    asyncio.run(main())