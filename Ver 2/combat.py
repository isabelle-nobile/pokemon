import random
from math import floor
# from pokemon import Pokemon
from dataclasses import fields


GLOBAL_DAMAGE_REDUCTION = 4  # damage reduction for fights because hp and damage is not balanced

def print_heading(heading):
    print(f"---------------------------{heading}---------------------------")


class Combat:

    @staticmethod
    def fight(pokemon1, pokemon2, random_fight=True):
        """
        Let two pokemons fight each other.

        While both pokemons are alive they keep fighting in a recursive loop of fight()
        Pokemons can choose their own moves at random or if random_fight is set to false a user can choose moves.

        ...

        Parameters
        ----------
        pokemon1 : Pokemon
            The first pokemon to fight.
        pokemon2 : Pokemon
            The second pokemon to fight.
        random_fight : boolean
            True: pokemons choose their own moves at random. False: Player chooses pokemons' moves.
        """
        turn = 1
        while pokemon1.hp > 0 and pokemon2.hp > 0:
            print_heading(f'TURN {turn}')
            print(f"{pokemon1.name} hp:{pokemon1.hp} ---> {pokemon2.name} hp:{pokemon2.hp}"
                  f" (type multiplier = {pokemon2.multiplicative_damage[pokemon1.type]})")

            # choose move for pokemon1
            available_moves = Combat.check_available_moves(pokemon1) # Modification ici
            input_nr = 0
            if random_fight:
                move_nr = "move" + str(random.choice(available_moves))
            else:
                pokemon1.print_moves()
                while True:
                    try:
                        input_nr = int(input(f"{pokemon1.name}, please enter the move you want to use: "))
                    except ValueError:
                        print("The input value is not an integer")
                        continue
                    if input_nr not in available_moves:
                        print("The input value is not a move the pokemon has")
                        continue
                    else:
                        break
                move_nr = "move" + str(input_nr)

            selected_move = getattr(pokemon1.moves, move_nr)
            move_name = selected_move['move_name']

            # attack damage is  (move_damage * enemy_dmg_taken_per_type) / GLOBAL_DAMAGE_REDUCTION
            attack_damage = floor(
                (selected_move['attack'] * pokemon2.multiplicative_damage[pokemon1.type]) / GLOBAL_DAMAGE_REDUCTION)
            pokemon2.hp -= attack_damage

            print(f"{pokemon1.name} did {move_name} for {attack_damage} Damage to {pokemon2.name}")
            print(f"{pokemon2.name} has {pokemon2.hp} HP left")

            # switch pokemon1 and pokemon2
            pokemon1, pokemon2 = pokemon2, pokemon1
            turn += 1

        # declare winner
        winner = pokemon1 if pokemon1.hp > 0 else pokemon2
        loser = pokemon2 if pokemon1.hp > 0 else pokemon1
        loser.hp = 0
        print_heading("WINNER: ")
        print(f"{winner.name} wins! ({winner.hp} HP left)")

    @staticmethod
    def check_available_moves(pokemon):
        """Check which moves the Pokemon has available

        Parameters
        ----------
        pokemon : Pokemon
            The active Pokemon in the combat.

        Returns
        -------
        list
            a list of of move numbers, e.g. all moves is [1,2,3,4]
        """
        available_moves = []
        for idx, move in enumerate(fields(pokemon.moves)):
            if getattr(pokemon.moves, move.name) is not None:
                available_moves.append(idx + 1)
        return available_moves

    # def check_available_moves(self):
    #     """Check which moves the Pokemon has available

    #     Returns
    #     -------
    #     list
    #     a list of of move numbers, e.g. all moves is [1,2,3,4]
    #     """
    #     available_moves = []
    #     for idx, move in enumerate(fields(self.moves)):
    #         if getattr(self.moves, move.name) is not None:
    #             available_moves.append(idx + 1)
    #     return available_moves


    # def fight(self, enemy, random_fight=True, turn=1):
    #     """
    #     Let a pokemon fight another pokemon

    #     While both pokemon are alive pokemon keep fighting in recursive loop of fight()
    #     Pokemon can choose their own moves at random or if random_fight is set to false a user can choose moves.

    #     ...

    #     Parameters
    #     ----------
    #     enemy : Pokemon
    #         the enemy pokémon
    #     random_fight : boolean
    #         True: pokemon choose their own moves at random. False: Player chooses pokemon moves
    #     turn : int
    #         shows in which turn the fight is.
    #     """
    #     if self.hp > 0:  #
    #         print_heading(f'TURN {turn}')
    #         print(f"{self.name} hp:{self.hp} ---> {enemy.name} hp:{enemy.hp}"
    #               f" (type multiplier = {enemy.multiplicative_damage[self.type]})")

    #         available_moves = self.check_available_moves()
    #         input_nr = 0
    #         if random_fight:
    #             move_nr = "move" + str(random.choice(available_moves))
    #         else:
    #             self.print_moves()
    #             while True:
    #                 try:
    #                     input_nr = int(input("Please enter the move you want to use: "))
    #                 except ValueError:
    #                     print("The input value is not an integer")
    #                     continue
    #                 if input_nr not in available_moves:
    #                     print("The input value is not an move the pokemon has")
    #                     continue
    #                 else:
    #                     break
    #             move_nr = "move" + str(input_nr)

    #         selected_move = getattr(self.moves, move_nr)
    #         move_name = selected_move['move_name']

    #         # attack damage is  (move_damage * enemy_dmg_taken_per_type) / GLOBAL_DAMAGE_REDUCTION
    #         attack_damage = floor(
    #             (selected_move['attack'] * enemy.multiplicative_damage[self.type]) / GLOBAL_DAMAGE_REDUCTION)
    #         enemy.hp -= attack_damage

    #         print(f"{self.name} did {move_name} for {attack_damage} Damage to {enemy.name}")
    #         print(f"{enemy.name} has {enemy.hp} HP left")

    #         return enemy.fight(self, random_fight, turn + 1)  # now the other pokemon attacks
    #     else:
    #         self.hp = 0  # leave pokemon with 0 health instead of a negative value
    #         print_heading("WINNER: ")
    #         print(f"{enemy.name} wins! ({enemy.hp} HP left)")