import sys
from os import system, name
from View.MenuView import MenuView
import Modele.combat as combat
# import Modele.pokemon as pokemon
from Modele.pokemon import Pokemon
from Modele.combat import Combat

import Modele.combat as combat
import random

class ApplicationCtrl:
    """La classe qui gère le menu principale"""

    def __init__(self):
        self.pokemons = Pokemon.POKEMONS

    def start(self):
        """Lance l'application pour demander une action sur le menu principal"""
        self.command = MenuView(self.pokemons)
        self.menu_starting = self.command.launch_command_menu()

        if self.menu_starting == "commencer":
            pokemon1_choice = MenuView(self.pokemons).launch_pokemon_choices()
            pokemon1 = Pokemon(pokemon1_choice['name'],pokemon1_choice['hp'], pokemon1_choice['defense'], pokemon1_choice['attack'], pokemon1_choice['type'])

            pokemon2_choice = random.choice(Pokemon.POKEMONS)
            pokemon2 = Pokemon(pokemon2_choice['name'],pokemon1_choice['hp'], pokemon2_choice['defense'], pokemon2_choice['attack'], pokemon2_choice['type'])

            self.start_combat(pokemon1, pokemon2)

        elif self.menu_starting == "supprimer":
            self.clear_terminal()
            self.start()

    def start_combat(self, pokemon1, pokemon2):
        combat_instance = Combat(pokemon1, pokemon2)
        combat_instance.launch_combat()


    def clear_terminal(self):
        """Supprimer le terminal"""
        # Pour windows
        if name == 'nt':
            _ = system('cls')
    
        # Pour mac et linux
        else:
            _ = system('clear')
