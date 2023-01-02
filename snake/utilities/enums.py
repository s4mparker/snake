
""" Importing """

from enum import Enum

""" Packaging """

__all__ = ['Direction', 'Tag']

class Direction(Enum):
    LEFT  = 'left'
    RIGHT = 'right'
    UP    = 'up'
    DOWN  = 'down'

class Tag(Enum):
    HEAD  = 'head'
    BODY  = 'body'
    APPLE = 'apple'

