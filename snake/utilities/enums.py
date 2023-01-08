
""" Importing """

from enum import Enum

""" Packaging """

__all__ = ['Direction']

class Direction(Enum):
    LEFT  = 'left'
    RIGHT = 'right'
    UP    = 'up'
    DOWN  = 'down'
