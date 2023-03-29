from View.menu import MenuView 

class Pokemon:
    def __init__(self, nom, niveau, puissance_attaque) -> None:
        self.__nom = nom
        self.__points_de_vie = 100
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = 0


    def choix_pokemon(self):
        MenuView.launch_pokemon_choices()

    def pikachu(self):
        pass


    