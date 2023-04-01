from dataclasses import dataclass


@dataclass
class Move:
    """
    Data class used to represent pokémon moves

    ...

    Attributes
    ----------
    move_name : str
        the name of the move
    attack : int
        the attack damage of the move
    """
    move_name: str
    attack: int