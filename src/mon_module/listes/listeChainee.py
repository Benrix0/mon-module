class Cellule:
    def __init__(self, valeur, suivante):
        self.__valeur = valeur
        self.suivante = suivante

    def __str__(self):
        return "({}, {})".format(self.__valeur, self.suivante)

    def __repr__(self):
        return self.__str__()

    def getSuivante(self):
        return self.suivante

    def setSuivante(self, suivante):
        self.suivante = suivante

    def getValeur(self):
        return self.__valeur

    def setValeur(self, valeur):
        self.__valeur = valeur


class ListeChaine:
    def __init__(self, *args) -> None:
        suivante = None
        for i in range(len(args), 0, - 1):
            cellule = Cellule(args[i - 1], suivante)
            suivante = cellule
        self.__valeur = cellule
        self.__length = len(args)
        self.__index = -1

    def __str__(self) -> str:
        cellule = self.__valeur
        res = "["
        for i in range(0, self.__length):
            if cellule:
                if i == 0:
                    res += str(cellule.getValeur())
                else:
                    res += ", " + str(cellule.getValeur())
                cellule = cellule.getSuivante()

        res += "]"
        return res

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, indice: int):
        if indice < self.__length:
            cellule = self.__valeur
            for i in range(indice + 1):
                if i == indice:
                    return cellule.getValeur()
                cellule = cellule.getSuivante()
        else:
            raise IndexError

    def __setitem__(self, indice: int, valeur: any):
        if indice < self.__length:
            cellule = self.__valeur
            for i in range(indice + 1):
                if i == indice:
                    return cellule.setValeur(valeur)
                cellule = cellule.getSuivante()
        else:
            return IndexError

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= self.__length:
            self.__index = -1
            raise StopIteration
        else:
            return self[self.__index]

    def __len__(self):
        return self.__length

    def ajouter(self, valeur: any, pos: int = -1) -> None:
        if pos == -1:
            pos = self.__length - 1
        if pos < self.__length:
            if pos == 0:
                self.__valeur = Cellule(valeur, self.__valeur)
                self.__length += 1
            elif pos == self.__length - 1:
                cellule = self.__valeur
                for i in range(self.__length):
                    if cellule.getSuivante() is None:
                        cellule.setSuivante(Cellule(valeur, None))
                    cellule = cellule.getSuivante()
                    self.__length += 1
            else:
                cellule = self.__valeur
                for i in range(pos):
                    cellule = cellule.getSuivante()
                    if i == pos - 2:
                        nvCellule = Cellule(valeur, cellule.getSuivante())
                        cellule.setSuivante(nvCellule)
                        self.__length += 1
        else:
            raise IndexError("index out of range")

    def supprimer(self, pos: int = 0) -> any:
        if pos < self.__length and pos >= 0:
            if pos == 0:
                res = self.__valeur.getValeur()
                self.__valeur = self.__valeur.getSuivante()
                self.__length -= 1
                return res
            elif pos == self.__length - 1:
                cellule = self.__valeur
                for i in range(1, self.__length):
                    if i == pos:
                        precCell = cellule
                    cellule = cellule.getSuivante()
                precCell.setSuivante(None)
                self.__length -= 1
                return cellule.getValeur()
            else:
                cellule = self.__valeur
                for i in range(1, pos + 1):
                    if i == pos:
                        precCell = cellule
                        cellule = cellule.getSuivante()
                    else:
                        cellule = cellule.getSuivante()
                precCell.setSuivante(cellule.getSuivante())
                self.__length -= 1
                return cellule.getValeur()
        else:
            raise IndexError

    def compte(self, valeur) -> int:
        res = 0
        cellule = self.__valeur
        for i in range(0, self.__length):
            if cellule.getValeur() == valeur:
                res += 1
            cellule = cellule.getSuivante()
        return res
