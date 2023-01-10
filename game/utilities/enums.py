
""" Importing """

from enum import Enum

""" Packaging """

__all__ = ['Direction', 'Message']

class Direction(Enum):
    LEFT  = 'left'
    RIGHT = 'right'
    UP    = 'up'
    DOWN  = 'down'

class Message(Enum):
    GAMEOVER = lambda o: setattr(o, 'game_active', False)
    LENGTHEN = 'lengthen'
    NEWAPPLE = 'new_apple'
    ADD10    = lambda o: setattr(o, 'score', o.score + 10)

    def __call__(self, *args):
        """ Execute a message 
        
        Parameters: TBC
        """

        if callable(self.value):
            self.value(*args)
        
    