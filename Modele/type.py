from pokemon import Pokemon

class Type(Pokemon):
    def __init__(self, nom, niveau, puissance_attaque, eau, terre, normal, feu) -> None:
        super().__init__(nom, niveau, puissance_attaque)
        self.eau = eau
        self.terre = terre
        self.normal = normal
        self.feu = feu 

    def __str__(self):
        return f'Nom: {self.__nom},\nPV: {self.__points_de_vie},\n Attaque: {self.puissance_attaque},\n Defense: {self.defense}'
