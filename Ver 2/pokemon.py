import csv
import random
from pathlib import Path
from dataclasses import fields
from moveset import MoveSet



def print_heading(heading):
    print(f"---------------------------{heading}---------------------------")

class Pokemon(object):
    """
    A class used to represent a pokémon

    """

    all = {}  # dict so each pokemon can only exist ones

    def __init__(self, name, hp: int, moves: MoveSet, p_type, multiplicative_damage=None):
        """
        Parameters
        ----------
        name : str
            the name of the pokémon
        hp : int
            the hp of the pokémon
        moves : MoveSet
            the moveset of the pokémon
        p_type : str
            the type of the pokémon
        multiplicative_damage : dict
            the multiplicative damage received per pokémon type

        Raises
        ------
        Hit point error
            If hit point is not greater than 0"
        Move set error
            If move set does not have 1 move
        """
        assert hp > 0, f"Hit point {hp} is not greater than 0"
        assert sum(
            getattr(moves, move.name) is not None for move in fields(moves)), f"pokémon should at least have 1 move"

        self.name = name
        self.hp = hp
        self.moves = moves
        self.type = p_type
        self.multiplicative_damage = multiplicative_damage or {}
        Pokemon.all[name] = self

    def __repr__(self):
        """Custom string to print objects with the Pokemon class """

        return f"Pokemon('{self.name}', {self.hp}, {self.moves}, {self.type},{self.multiplicative_damage})"

    

    @staticmethod
    def print_all_pokemon():
        """Print all available pokemon"""

        print_heading('AVAILABLE POKEMON')
        for idx, pokemon in enumerate(list(Pokemon.all.values())):
            status = ""
            if pokemon.hp == 0:
                status = "---knocked out"
            print(f"{idx + 1} > {pokemon.name}, type: {pokemon.type}, hp: {pokemon.hp} {status}")

    def print_pokemon_specs(self):
        """Print specs of Pokemon"""

        print(f"Pokemon name: '{self.name}'")
        print(f"Pokemon hp: '{self.hp}'")
        print(f"Pokemon type: '{self.type}'")
        self.print_moves()
        self.print_multiplicative_damage()

    def print_moves(self):
        """Print moves of Pokemon"""

        print_heading('MOVES')
        for idx, move in enumerate(fields(self.moves)):
            if getattr(self.moves, move.name) is not None:
                move_name = getattr(self.moves, move.name)['move_name']
                attack = getattr(self.moves, move.name)['attack']
                print(f"{idx + 1} > {move_name}, dmg: {attack}")

    def print_multiplicative_damage(self):
        """Print multiplicative damage received per pokémon type of Pokemon"""

        print_heading('DAMAGE TAKEN MULTIPLIER PER TYPE')
        print(list(self.multiplicative_damage.keys()), list(self.multiplicative_damage.values()), sep='\n')

    @classmethod
    def instantiate_from_csv(cls, available_moves=4):
        """instantiate all pokémon in datafile and give each pokémon random moves

        ...

        Parameters
        ----------
        available_moves : int
            the amount of moves each instantiated Pokemon should have
        """

        base_path = Path(__file__).parent  # absolute path so its works when used in all locations' e.g. testing file

        # get moves
        with open(base_path / 'data/PokemonMoves.csv', 'r') as f:
            reader = csv.DictReader(f)
            moves_in_csv = list(reader)
            for move in moves_in_csv:
                move['attack'] = int(move['attack'] or 0)  # make attack an int value

        # get pokémon
        with open(base_path / 'data/FirstGenPokemon.csv', 'r') as f:
            reader = csv.DictReader(f)
            pokemons_in_csv = list(reader)

        # create all pokémon from dataset
        for pokemon in pokemons_in_csv:

            # select random moves for each pokémon
            moves = MoveSet()
            for idx, move in enumerate(fields(moves)):
                random_move = random.choice(moves_in_csv)
                setattr(moves, move.name, random_move)
                if idx == available_moves - 1:
                    break

            # multiplicative_damage to float
            multiplicative_damage = dict(list(pokemon.items())[3:])
            multiplicative_damage = dict(
                zip(multiplicative_damage.keys(), [float(value) for value in multiplicative_damage.values()]))

            # create pokémon
            Pokemon(
                name=pokemon.get('Name'),
                hp=int(pokemon.get('HP')),
                moves=moves,
                p_type=pokemon.get('Type'),
                multiplicative_damage=multiplicative_damage
            )

    @classmethod
    def create_via_terminal(cls):
        """Create a new Pokemon via user input in the terminal"""

        print_heading('CREATE A POKEMON')
        types = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fight', 'poison',
                 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon']
        multiplicative_damage_values = []
        p_type = ""
        hp = 0
        attack = 0
        available_moves = 0
        name = input("what is the name of the Pokemon: ")

        # ask pokemon type
        while True:
            try:
                print(f"Available types: {types}")
                p_type = input("what is the type of the Pokemon: ")
            except ValueError:
                print("Incorrect value")
                continue
            if p_type not in types:
                print("That pokemon type does not exist")
                continue
            else:
                break

        # ask hp
        while True:
            try:
                hp = int(input("what is the hp of the Pokemon: "))
            except ValueError:
                print("The hp value is not an integer")
                continue
            else:
                break

        # ask how many moves the pokemon should have
        while True:
            try:
                available_moves = int(input("how many moves does the Pokemon have (1 to 4): "))
            except ValueError:
                print("The nr of moves is not an integer")
                continue
            if available_moves < 1 or available_moves > 4:
                print("The pokemon can only have 1 to 4 moves")
                continue
            else:
                break

        # create moves
        moves = MoveSet()
        for idx, move in enumerate(fields(moves)):
            print_heading(f'MOVE {idx + 1}')
            move_name = input(f"The name of move {idx + 1}: ")
            while True:
                try:
                    attack = int(input("what is the attack of the move: "))
                except ValueError:
                    print("The attack value is not an integer")
                    continue
                if attack < 0:
                    print("the attack value is negative")
                    continue
                else:
                    break
            setattr(moves, move.name, {'move_name': move_name, 'attack': attack})
            if idx == available_moves - 1:
                break

        # ask multiplicative_damage_values
        while True:
            try:
                print("insert multiplicative damage taken per type as 15 float values seperated with a comma")
                print(f"types are in the following order {types}")

                multiplicative_damage_values = [float(multiplicative_damage)
                                                for multiplicative_damage in input("values: ").split(",")]
            except ValueError:
                print("one of the values is not an float")
                continue

            if len(multiplicative_damage_values) != 15:
                print(f"not the correct number of values {len(multiplicative_damage_values)} != 15")
                continue
            else:
                break

        multiplicative_damage = dict(zip(types, multiplicative_damage_values))

        # create pokémon
        Pokemon(
            name=name,
            hp=hp,
            moves=moves,
            p_type=p_type,
            multiplicative_damage=multiplicative_damage
        )

    def revive(self, revive_hp=100):
        """Revive the pokemon

        Pokemon can be given any amount of hp, base is 100

        ...

        Parameters
        ----------
        revive_hp : int
            the hp the Pokemon should revive with
        """

        self.hp = revive_hp
        
    def fight(self, opponent_pokemon, combat_instance, random_fight=None):
        ...
        # call the fight method of the Combat class
        combat_instance.fight(self, opponent_pokemon, random_fight=random_fight)
