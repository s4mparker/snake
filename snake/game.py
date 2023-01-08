
""" Importing """

from .      import Parameters, Messages, Map, Cell, Display, Snake, Direction
from random import choice
from time   import sleep

""" Packaging """

__all__ = ['Game']

class Game:

    """ TODO
    
    
    """

    def __init__(self, game_parameters, controller, display=False, display_parameters=None):
        """ Create a new game 
        
        Parameters: TBC
        """

        params          = Parameters.import_file(filename=game_parameters)

        # Game components
        self.messages   = Messages('game', 'snake', 'apple')
        self.map        = Map(params.get('WIDTH'), params.get('HEIGHT'))
        self.snake      = Snake(self.messages, self.map.at(x=params.get('STARTX'), y=params.get('STARTY')))

        # Game state
        self.score      = 0
        self.gameover   = False
        self.lengthen   = False

        # Game controller
        move = Direction(params.get('INITIAL'))
        self.controller = controller(period=params.get('PERIOD'), move=move)

        # Game display (if required)
        if display and not display_parameters:
            raise ValueError(f'no display parameters provided')
        elif not display and display_parameters:
            raise ValueError(f'display parameters provided but no display enabled')
        
        self.display = Display(display_parameters=display_parameters) if display else None
        if self.display : self.display.initialize(game=self)

    def begin(self):
        """ Begin execution of the game """

        i = 30

        while not self.gameover and i > 0:
            

            move = self.controller.poll()
            self.snake.update(move)
            if self.display : self.display.update()
            i -= 1
