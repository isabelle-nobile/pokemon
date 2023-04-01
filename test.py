import random


class Pokemon:
    POKEMONS = [
        {"name": "Pikachu", "hp": 35, "defense": 30, "attack": 55},
        {"name": "Evoli", "hp": 55, "defense": 50, "attack": 55},
        {"name": "Mew", "hp": 100, "defense": 100, "attack": 100},
    ]

    def __init__(self, name, hp, defense, attack, type_p):
        self.__name = name
        self.__hp = hp
        self.__defense = defense
        self.__attack = attack
        self.type_p = type_p

    def __str__(self):
        return f"{self.__name}, HP: {self.__hp}, Defense: {self.__defense}, Attack: {self.__attack}, Type: {self.type}"

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp

    def take_damage(self, damage):
        defense_multiplier = self.type_p.get_defense_multiplier(
            self.type_p, self.type_p.get_opponent_type())
        damage_taken = damage * defense_multiplier
        self.set_hp(self.get_hp() - damage_taken)
        print(f"{self.get_name()} a perdu {damage_taken} HP")

    @classmethod
    def get_random_opponent(cls):
        opponent = cls.POKEMONS[random.randint(0, len(cls.POKEMONS)-1)]
        return cls(
            opponent["name"],
            opponent["hp"],
            opponent["defense"],
            opponent["attack"])


import sys
from os import system, name
from View.MenuView import MenuView
import Modele.combat as combat
import Modele.pokemon as pokemon
import Modele.combat as combat

class ApplicationCtrl:
    """La classe qui gère le menu principale"""

    def __init__(self):
        self.pokemons = pokemon.Pokemon.POKEMONS

    def start(self):
        """Lance l'application pour demander une action sur le menu principal"""
        self.command = MenuView(self.pokemons)
        self.menu_starting = self.command.launch_command_menu()

        if self.menu_starting == "commencer":
            pokemon1_type = input("Choisissez le type de Pokemon 1 (eau/feu/herbe/normal): ")
            pokemon1_choice = MenuView(self.pokemons).launch_pokemon_choices(pokemon1_type)
            pokemon1 = pokemon.Pokemon(pokemon1_choice['name'], pokemon1_choice['hp'], pokemon1_choice['defense'], pokemon1_choice['attack'], pokemon1_choice['type_p'])

            combat_instance = combat.Combat(pokemon1, None)
            combat_instance.launch_combat()

        elif self.menu_starting == "supprimer":
            self.clear_terminal()
            self.start()

    def clear_terminal(self):
        """Supprimer le terminal"""
        # Pour windows
        if name == 'nt':
            _ = system('cls')
    
        # Pour mac et linux
        else:
            _ = system('clear')

import random
from Modele.pokemon import Pokemon

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2
    
    def is_over(self):
        return self.__pokemon1.get_hp() <= 0 or self.__pokemon2.get_hp() <= 0
    
    def get_winner(self):
        if self.__pokemon1.get_hp() > 0 and self.__pokemon2.get_hp() <= 0:
            return self.__pokemon1.get_name()
        elif self.__pokemon2.get_hp() > 0 and self.__pokemon1.get_hp() <= 0:
            return self.__pokemon2.get_name()
        else:
            return None
        
    def get_attack_multiplier(self, attacker_type, defender_type):
        return attacker_type.get_attack_multiplier(defender_type)
    
    def apply_damage(self, attacker, defender):
        damage = attacker.get_attack()
        defender_type = defender.type
        attack_multiplier = self.get_attack_multiplier(attacker.type, defender_type)
        damage *= attack_multiplier
        defender.take_damage(damage)
        
    def get_loser(self):
        if self.__pokemon1.get_hp() <= 0:
            return self.__pokemon1.get_name()
        elif self.__pokemon2.get_hp() <= 0:
            return self.__pokemon2.get_name()
        else:
            return None
    
    def launch_combat(self):
        pokemon2_choice = random.choice(Pokemon.POKEMONS)
        pokemon2 = Pokemon(pokemon2_choice['name'], pokemon2_choice['hp'], pokemon2_choice['defense'], pokemon2_choice['attack'])
        print(f"{self.__pokemon1.get_name()} VS {pokemon2.get_name()} !")
        while not self.is_over():
            print(f"{self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV - {pokemon2.get_name()} : {pokemon2.get_hp()} PV")
            self.apply_damage(self.__pokemon1, pokemon2)
            if self.is_over():
                break
            print(f"{pokemon2.get_name()} : {pokemon2.get_hp()} PV - {self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV")
            self.apply_damage(pokemon2, self.__pokemon1)
        print("Le combat est terminé !")
        winner = self.get_winner()
        if winner is not None:
            print(f"{winner} a gagné !")
        else:
            print("Le combat s'est terminé en égalité !")

from Modele.pokemon import Pokemon


class Type(Pokemon):
    def __init__(self, name, hp, attack, defense, type):
        super().__init__(name, hp, defense, attack, type)
        if type == "Feu":
            self.set_hp(hp * 0.8)
            self.__attack *= 1.2
            self.__defense *= 0.9
        elif type == "Eau":
            self.set_hp(hp * 1.2)
            self.__attack *= 0.9
            self.__defense *= 1.1
        elif type == "Terre":
            self.set_hp(hp * 1.1)
            self.__attack *= 1.1
            self.__defense *= 1.2
        elif type == "Normal":
            self.set_hp(hp)
            self.__attack *= 1.0
            self.__defense *= 1.0
    
    def get_attack_multiplier(self, opponent_type):
        return self.type.get_attack_multiplier(self.type, opponent_type)

    def get_defense_multiplier(self, opponent_type):
        return self.type.get_defense_multiplier(self.type, opponent_type)
