
""" Importing """

from . import Parameters, Messages, Map, Cell, Display, Snake, Direction
from random import choice
from time import sleep

""" Packaging """

__all__ = ['Game']

class Game:

    def __init__(self, game_parameters, controller, display=False, display_parameters=None):
        """ Create a new game 
        
        Parameters: TBC
        """

        params          = Parameters(filename=game_parameters)

        # Game components
        self.messages   = Messages('game', 'snake', 'apple')
        self.map        = Map.generate(params.width, params.height)
        self.snake      = Snake(self.messages, Direction.LEFT, self.map[20][20])

        # Game state
        self.score      = 0
        self.gameover   = False
        self.lengthen   = False

        # IO components
        self.controller = controller
        if display and not display_parameters : raise ValueError(f'no display parameters provided')
        self.display    = Display(display_parameters) if display else None
        if self.display : self.display.initialize(self, params.width, params.height)

    def __iter__(self):
        """ Return an iterator over the game's map """

        return iter([cell for row in self.map for cell in row])

    def getDisplay(self):
        """ Return a display for the game """

        return self.display

    def begin(self):
        """ Begin execution of the game """

        for i in range(30):
            move = choice([d for d in Direction])
            if i % 2 == 0:
                self.messages.put('test', 'snake')
            self.snake.update(move)
            if self.display: self.display.update()
            sleep(0.2)
