
""" Importing """

from enum import Enum

""" Packaging """

__all__ = ['Direction']

class Direction(Enum):
    LEFT  = 'left'
    RIGHT = 'right'
    UP    = 'up'
    DOWN  = 'down'

    def opposite(self):
        """ Get the opposite of a given direction """

        match self:
            case Direction.LEFT  : return Direction.RIGHT
            case Direction.RIGHT : return Direction.LEFT
            case Direction.UP    : return Direction.DOWN
            case Direction.DOWN  : return Direction.UP