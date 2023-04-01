from dataclasses import dataclass
from move import Move

@dataclass
class MoveSet:
    """Data class used to represent the moveset pokémon"""
    move1: Move = None
    move2: Move = None
    move3: Move = None
    move4: Move = None