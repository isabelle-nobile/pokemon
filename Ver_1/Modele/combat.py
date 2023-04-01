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

    # def apply_damage(self, attacker_index, defender_index):
    #     attacker = [self.__pokemon1, self.__pokemon2][attacker_index - 1]

    #     defender = [self.__pokemon1, self.__pokemon2][defender_index - 1]
        
    #     attack_multiplier = attacker.get_attack_multiplier(defender.get_type())
    #     defense_multiplier = defender.get_defense_multiplier(
    #         attacker.get_type())
    #     damage = int(
    #         (attacker.get_attack() * attack_multiplier - defender.get_defense() *
    #          defense_multiplier) / 10)
    #     defender.set_hp(max(0, defender.get_hp() - damage))
    #     print(damage)
        # print(f"{attacker.get_name()} attaque {defender.get_name()} !")
        # print(f"Multiplicateur d'attaque : {attack_multiplier}")
        # print(f"Multiplicateur de défense : {defense_multiplier}")
        # print(f"{defender.get_name()} perd {damage} PV !")


        # return damage
    
    def apply_damage(self, attacker_index, defender_index):
        attacker = [self.__pokemon1, self.__pokemon2][attacker_index - 1]
        defender = [self.__pokemon1, self.__pokemon2][defender_index - 1]
        
        attack_multiplier = attacker.get_attack_multiplier(defender.get_type())
        defense_multiplier = defender.get_defense_multiplier(attacker.get_type())
        
        damage = self.calculate_damage(attacker, defender, attack_multiplier, defense_multiplier)
        
        defender.set_hp(max(0, defender.get_hp() - damage))
        
        return damage



    def calculate_damage(
            self, attacker, defender, attack_multiplier, defense_multiplier):
        damage = 2 * attacker.level / 5 + 2
        damage = int(damage * attacker.attack / defender.defense)
        damage = int(damage / 50) + 2
        damage = int(damage * attack_multiplier)
        damage = int(damage * defense_multiplier)
        return damage

    def get_loser(self):
        if self.__pokemon1.get_hp() <= 0:
            return self.__pokemon1.get_name()
        elif self.__pokemon2.get_hp() <= 0:
            return self.__pokemon2.get_name()
        else:
            return None

    # def launch_combat(self):
    #     # pokemon2_choice = random.choice(Pokemon.POKEMONS)
    #     # pokemon2 = Pokemon(pokemon2_choice['name'], pokemon2_choice['hp'], pokemon2_choice['defense'], pokemon2_choice['attack'], pokemon2_choice['type'])
    #     print(f"{self.__pokemon1.get_name()} VS {self.__pokemon2.get_name()} !")
    #     while not self.is_over():
    #         print(f"{self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV - {self.__pokemon2.get_name()} : {self.__pokemon2.get_hp()} PV")
    #         self.apply_damage(1, 2)
    #         # print(self.apply_damage(1, 2))
    #         if self.is_over():
    #             break
    #         print(f"{self.__pokemon2.get_name()} : {self.__pokemon2.get_hp()} PV - {self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV")
    #         self.apply_damage(2, 1)
    #         # print(self.apply_damage(1, 2))

    #     print("Le combat est terminé !")
    #     winner = self.get_winner()
    #     if winner is not None:
    #         print(f"{winner} a gagné !")
    #     else:
    #         print("Le combat s'est terminé en égalité !")
    # def launch_combat(self):
    #     print(f"{self.__pokemon1.get_name()} VS {self.__pokemon2.get_name()} !")
    #     while not self.is_over():
    #         print(f"{self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV - {self.__pokemon2.get_name()} : {self.__pokemon2.get_hp()} PV")
    #         print("-----")
    #         self.apply_damage(1, 2)
    #         print(f"{self.__pokemon2.get_name()} : {self.__pokemon2.get_hp()} PV - {self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV")
    #         print("-----")
    #         self.apply_damage(2, 1)

    #     print("Le combat est terminé !")
    #     winner = self.get_winner()
    #     if winner is not None:
    #         print(f"{winner} a gagné !")
    #     else:
    #         print("Le combat s'est terminé en égalité !")
    def launch_combat(self):
        print(f"{self.__pokemon1.get_name()} VS {self.__pokemon2.get_name()} !")
        while not self.is_over():
            print(f"{self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV - {self.__pokemon2.get_name()} : {self.__pokemon2.get_hp()} PV")
            print("-----")
            damage = self.calculate_damage(1, 2)
            self.__pokemon2.take_damage(damage, self.__pokemon1)
            print(f"{self.__pokemon2.get_name()} : {self.__pokemon2.get_hp()} PV - {self.__pokemon1.get_name()} : {self.__pokemon1.get_hp()} PV")
            print("-----")
            damage = self.calculate_damage(2, 1)
            self.__pokemon1.take_damage(damage, self.__pokemon2)

        print("Le combat est terminé !")
        winner = self.get_winner()
        if winner is not None:
            print(f"{winner.get_name()} a gagné !")
        else:
            print("Le combat s'est terminé en égalité !")

