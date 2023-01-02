
""" Importing """

from threading import Timer, Event
from pygame import KEYDOWN
from pygame.event import get

""" Packaging """

__all__ = ['Controller', 'ControllerMapping']

class ControllerMapping:

    def __init__(self):
        """ Create a new ControllerMapping object """

        self.mapping = {}

    def addMapping(self, key, action):
        """ Add a new mapping to a ControllerMapping object """

        if key in self.mapping.keys():
            raise ValueError(f'invalid key mapping - there already exists a {str(key)} key mapping')
        self.mapping[key] = action
        
    def hasMapping(self, key):
        """ Determine whether a ControllerMapping object has a mapping for a given key """

        return key in self.mapping.keys()
    
    def getMapping(self, key):
        """ Get the mapping for a given key from a ControllerMapping object """

        return self.mapping.get(key, None)

class Controller:

    def __init__(self, time, mapping, initial_move, verbose=False):
        """ Create a new Controller object 
        
        Parameters:
            time         (int)               : time available for the controller to provide a move
            mapping      (ControllerMapping) : key mapping
            initial_move (Direction)         : controller's initial / default move
            verbose      (bool)              : verbose option
        """

        self.time    = time
        self.mapping = mapping
        self.move    = initial_move
        self.verbose = verbose

        # Timing components
        self.flag  = Event()

    def poll(self):
        """ Poll a controller for an input """

        # Reset the event flag and start the timer
        self.flag.clear()
        Timer(self.time, lambda: self.flag.set()).start()

        # Process any incoming keydown events
        while not self.flag.is_set():
            for key in [event.key for event in get(eventtype=KEYDOWN)]:
                if self.mapping.hasMapping(key):
                    self.move = self.mapping.getMapping(key)

        if self.verbose:
            print(f'move: {self.move.value}')
