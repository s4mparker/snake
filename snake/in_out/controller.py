
""" Importing """

from ..           import Direction
from threading    import Timer, Event
from pygame       import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d
from pygame.event import get

""" Packaging """

__all__ = ['Controller']

class Controller:

    def __init__(self, period, move):
        """ Create a new controller 
        
        Parameters:
            period (float)     : time available for the controller to provide a move
            move   (Direction) : the controller's initial move
        """

        self.period  = period
        self.move    = move
        self.mapping = {
            K_UP    : Direction.UP,
            K_w     : Direction.UP,
            K_DOWN  : Direction.DOWN,
            K_s     : Direction.DOWN,
            K_LEFT  : Direction.LEFT,
            K_a     : Direction.LEFT,
            K_RIGHT : Direction.RIGHT,
            K_d     : Direction.RIGHT
        }

        # Timing component
        self.flag    = Event()

    def poll(self):
        """ Poll a controller for an input """

        self.flag.clear()
        Timer(self.period, lambda: self.flag.set()).start()

        while not self.flag.is_set():
            for key in [event.key for event in get(eventtype=KEYDOWN)]:
                if key in self.mapping:
                    self.move = self.mapping.get(key)

        return self.move
