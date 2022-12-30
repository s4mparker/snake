
""" Importing """

from enum import Enum

""" Packaging """

__all__ = ['Direction', 'CellStatus']

class Direction(Enum):
    LEFT  = 'left'
    RIGHT = 'right'
    UP    = 'up'
    DOWN  = 'down'

class CellStatus(Enum):
    FREE       = 'free'
    SNAKE_BODY = 'snake_body'
    SNAKE_HEAD = 'snake_head'


