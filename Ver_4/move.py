from dataclasses import dataclass


@dataclass
class Move:
    """Data class used to represent pokémon moves"""
    move_name: str
    attack: int