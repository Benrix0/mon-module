class Pile:
    def __init__(self, *args):
        self.__valeur = list(args)

    def __str__(self):
        return str(self.__valeur)

    def __repr__(self):
        return self.__str__()

    def empiler(self, valeur):
        self.__valeur.append(valeur)

    def depiler(self):
        return self.__valeur.pop()