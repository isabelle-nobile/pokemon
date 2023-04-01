from dataclasses import dataclass
from move import Move

@dataclass
class MoveSet:
    """
    Data class used to represent the moveset pokémon

    ...

    Attributes
    ----------
    move1 : Move
        Move 1 of the pokémon
    move2 : Move
        Move 2 of the pokémon
    move3 : Move
        Move 3 of the pokémon
    move4 : Move
        Move 4 of the pokémon
    """
    move1: Move = None
    move2: Move = None
    move3: Move = None
    move4: Move = None