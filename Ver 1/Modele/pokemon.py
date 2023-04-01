import random
from Modele.type import Type

class Pokemon:
    POKEMONS = [
        {"name": "Evoli","hp": 100,  "defense": 50, "attack": 55, "type": "Normal"},
        {"name": "Charmander","hp": 100,  "defense": 43, "attack": 52, "type": "Feu"},
        {"name": "Squirtle","hp": 100,  "defense": 65, "attack": 48, "type": "Eau"},
        {"name": "Bulbasaur","hp": 100,  "defense": 49, "attack": 49, "type": "Terre"},
        {"name": "Jigglypuff","hp": 100,  "defense": 20, "attack": 45, "type": "Normal"},
        {"name": "Vaporeon", "hp": 100,  "defense": 60, "attack": 65, "type": "Eau"},
    ]

    VALID_TYPES = ["Normal", "Feu", "Eau", "Terre"]

    def __init__(self, name, hp, defense, attack, type):
        self.__name = name
        self.__hp = hp
        self.__defense = defense
        self.__attack = attack
        self.type = type

    def __str__(self):
        return f"{self.__name}, HP: {self.__hp}, Defense: {self.__defense}, Attack: {self.__attack}, Type: {self.type}"

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp

    def get_attack(self):
        return self.__attack
    
    def set_attack(self, attack):
        self.__attack = attack

    def get_defense(self):
        return self.__defense
    
    def set_defense(self, defense):
        self.__defense = defense

    def get_type(self):
        return self.type
    
    def set_type(self, type_):
        self.type = type_

    # def take_damage(self, damage, opponent):
    #     defense_multiplier = 1
    #     for valid_type in self.VALID_TYPES:
    #         if opponent.get_type() == valid_type:
    #             defense_multiplier = Type.get_defense_multiplier(Type(self.type), Type(valid_type))
    #             break
    #     damage_taken = damage * defense_multiplier
    #     self.set_hp(self.get_hp() - damage_taken)
    #     print(f"{self.get_name()} a perdu {damage_taken} HP")

    def take_damage(self, damage, opponent):
        attack_multiplier = Type.get_attack_multiplier(opponent.get_type(), self.type)
        defense_multiplier = Type.get_defense_multiplier(self.type, opponent.get_type())
        damage_taken = damage * attack_multiplier * defense_multiplier
        self.set_hp(self.get_hp() - damage_taken)
        print(f"{self.get_name()} a perdu {damage_taken} HP")


    @classmethod
    def get_random_opponent(cls):
        opponent = cls.POKEMONS[random.randint(0, len(cls.POKEMONS)-1)]
        return cls(
            opponent["name"],
            opponent["hp"],
            opponent["defense"],
            opponent["attack"],
            opponent["type"])
    
    def get_attack_multiplier(self, opponent_type):
        return Type.get_attack_multiplier(self.type, opponent_type)

    def get_defense_multiplier(self, opponent_type):
        return Type.get_defense_multiplier(self.type, opponent_type)
    
    def attack(self, opponent):
        damage = random.randint(1, 10)  # TODO: replace with actual damage calculation
        opponent.take_damage(damage, self)