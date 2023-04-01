import random
from typing import List, Tuple
from math import floor
from pokemon import Pokemon


class Combat:
    """
    A class used to represent a combat between two Pokémon.

    Attributes
    ----------
    pokemon1 : Pokemon
        the first Pokémon involved in the combat
    pokemon2 : Pokemon
        the second Pokémon involved in the combat
    random_fight : bool
        if True, the moves of each Pokémon will be selected at random during the combat
    turn : int
        the current turn number of the combat

    Methods
    -------
    fight() -> Tuple[str, Pokemon]
        Start the combat between pokemon1 and pokemon2 and return the winner of the combat and the remaining Pokémon.
    """

    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon, random_fight: bool = True):
        """
        Parameters
        ----------
        pokemon1 : Pokemon
            the first Pokémon involved in the combat
        pokemon2 : Pokemon
            the second Pokémon involved in the combat
        random_fight : bool
            if True, the moves of each Pokémon will be selected at random during the combat
        """

        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.random_fight = random_fight
        self.turn = 1

    def fight(self) -> Tuple[str, Pokemon]:
        """
        Start the combat between pokemon1 and pokemon2 and return the winner of the combat and the remaining Pokémon.

        Returns
        -------
        Tuple[str, Pokemon]
            A tuple containing the winner of the combat and the remaining Pokémon.
        """

        print(f"{self.pokemon1.name} vs {self.pokemon2.name} !")

        while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
            print(f"\nTURN {self.turn}")
            print(f"{self.pokemon1.name} ({self.pokemon1.hp} HP) vs {self.pokemon2.name} ({self.pokemon2.hp} HP)")

            # Determine the move of each Pokémon
            if self.random_fight:
                move1 = random.choice(self.pokemon1.check_available_moves())
                move2 = random.choice(self.pokemon2.check_available_moves())
            else:
                move1 = int(input(f"Which move should {self.pokemon1.name} use? ")) - 1
                move2 = int(input(f"Which move should {self.pokemon2.name} use? ")) - 1

            # Compute the damage dealt by each Pokémon
            damage1 = floor((self.pokemon1.moves[move1].attack / self.pokemon2.multiplicative_damage[self.pokemon1.type]) / GLOBAL_DAMAGE_REDUCTION)
            damage2 = floor((self.pokemon2.moves[move2].attack / self.pokemon1.multiplicative_damage[self.pokemon2.type]) / GLOBAL_DAMAGE_REDUCTION)

            # Apply the damage
            self.pokemon2.hp -= damage1
            print(f"{self.pokemon1.name} deals {damage1} damage to {self.pokemon2.name}!")
            if self.pokemon2.hp <= 0:
                break
            self.pokemon1.hp -= damage2
            print(f"{self.pokemon2.name} deals {damage2} damage to {self.pokemon1.name}!")

            # Increment the turn counter
            self.turn += 1

        if self.pokemon1.hp > 0:
            winner = self.pokemon1.name
            remaining_pokemon = self.pokemon1
        else:
            winner = self.pokemon
            winner = self.pokemon2.name
            remaining_pokemon = self.pokemon2

        print(f"\n{winner} wins the battle with {remaining_pokemon.hp} HP remaining!")
        return (winner, remaining_pokemon)

