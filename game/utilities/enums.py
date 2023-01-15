
""" Importing """

from enum import Enum

""" Packaging """

__all__ = ['Direction', 'Message']

class Direction(Enum):
    LEFT  = 'left'
    RIGHT = 'right'
    UP    = 'up'
    DOWN  = 'down'
