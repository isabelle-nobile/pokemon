import random
from math import floor
from type import Type
from dataclasses import fields


GLOBAL_DAMAGE_REDUCTION = 4  # damage reduction for fights because hp and damage is not balanced

def print_heading(heading):
    print(f"---------------------------{heading}---------------------------")


class Combat:
    def __init__(self):
        self.attack_order = []

    @staticmethod
    def fight(pokemon1, pokemon2, random_fight=True):
        turn = 1
        pokemon_type = Type()
        while pokemon1.hp > 0 and pokemon2.hp > 0:
            print_heading(f'TURN {turn}')
            print(f"{pokemon1.name} hp:{pokemon1.hp} ---> {pokemon2.name} hp:{pokemon2.hp}"
                  f" (type multiplier = {pokemon_type.get_multiplier(pokemon1.type, pokemon2.type)})")

            # choose move for pokemon1
            available_moves = Combat.check_available_moves(pokemon1)
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
                (selected_move['attack'] * pokemon_type.get_multiplier(pokemon1.type, pokemon2.type)) / GLOBAL_DAMAGE_REDUCTION)
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
        
        available_moves = []
        for idx, move in enumerate(fields(pokemon.moves)):
            if getattr(pokemon.moves, move.name) is not None:
                available_moves.append(idx + 1)
        return available_moves
