from listeChainee import *

class File:
    def __init__(self, *args):
        self.__valeur = ListeChaine(*args)

    def __str__(self):
        return self.__valeur.__str__()

    def __repr__(self):
        return self.__valeur.__str__()

    def getPremier(self):
        return self.__valeur[0]

    def enfiler(self, valeur):
        self.__valeur.ajouter(valeur)

    def defiler(self):
        return self.__valeur.supprimer()
