from Modele.pokemon import Pokemon

class MenuCtrl:
    """La classe qui gère le menu principal"""

    def start_combat(self):
        """Lance un combat entre deux pokémons choisis par le joueur"""
        pokemon1_choice = ... # récupérer le choix du joueur pour le premier pokémon
        pokemon1 = Pokemon(pokemon1_choice['name'], pokemon1_choice['hp'], pokemon1_choice['defense'], pokemon1_choice['attack'])
        pokemon2_choice = ... # récupérer le choix du joueur pour le deuxième pokémon
        pokemon2 = Pokemon(pokemon2_choice['name'], pokemon2_choice['hp'], pokemon2_choice['defense'], pokemon2_choice['attack'])
        combat = Combat(pokemon1, pokemon2)
        combat.launch_combat()


