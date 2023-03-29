from pokemon import Pokemon


class Combat(Pokemon):
    def __init__(
            self, nom, niveau, puissance_attaque, pokemon1, pokemon2) -> None:
        super().__init__(nom, niveau, puissance_attaque)
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def verifie_pv(self, perdant):
        if self.__points_de_vie <= 0:
            return perdant

    def return_nom_perdant(self, perdant):
        return perdant

    def return_nom_vainqueur(self, vainqueur):
        return vainqueur


    def calculer_degats(self, type_attaquant, type_adversaire):
        tableau = {
            "Eau": {"Eau": 1, "Feu": 2, "Terre": 0.5, "Normal": 1},
            "Feu": {"Eau": 0.5, "Feu": 1, "Terre": 2, "Normal": 1},
            "Terre": {"Eau": 2, "Feu": 0.5, "Terre": 1, "Normal": 1},
            "Normal": {"Eau": 0.75, "Feu": 0.75, "Terre": 0.75, "Normal": 1}
        }

        indice = tableau[type_attaquant][type_adversaire]
        return indice
       
    # def switch_player(self):
    #     p1 = input(Pokemon())
    #     p2 = input(Pokemon())
    #     if self.pokemon1 == p1:
    #         self.pokemon1 = p1
    #     else:
    #         self.pokemon2 = p2

    def remove_pv_defence(self):
        indice = self.calculer_degats("Eau", "Normal")
        degats = (self.puissance_attaque * indice) - self.defense
        if degats < 0:
            degats = 0

        return degats
    


    def launch_combat(self):
        pass


c = Combat("T", 100, 20, "Toutuz", "Racou")
print(c.remove_pv_defence())
