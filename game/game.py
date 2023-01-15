
""" Importing """

from .      import Parameters, Display, Direction
from .      import Snake, Apple, AppleManager
from .      import TileMap, GameState

""" Packaging """

__all__ = ['Game']

class Game:

    def __init__(self, parameters, controller, display=None):
        """ Create a new game 
        
        Parameters:
            parameters (str)        : game parameters
            controller (Controller) : a controller class with which to play the game
            display    (str)        : display parameters
        """

        # Game parameters
        params          = Parameters.import_file(filename=parameters)
        width, height   = params.get('WIDTH'), params.get('HEIGHT')
        x, y            = params.get('STARTX'), params.get('STARTY')
        move            = params.get('DIRECTION')
        period          = params.get('PERIOD')

        # Game components
        self.state      = GameState()
        self.map        = TileMap(width=width, height=height)
        start           = self.map.at(x=x, y=y)
        self.snake      = Snake(state=self.state, tile=start)
        self.apple      = AppleManager.spawn(map=self.map)

        # Game controller
        self.controller = controller(period=period, move=Direction(value=move))

        # Game display
        self.display = Display(parameters=display) if display else None
        if self.display:
            self.display.initialize(game=self)

    def play(self):
        """ Play a single game """

        while self.state:
            move = self.controller.poll()
            self.snake.apply(move=move)
            
            if not self.apple:
                self.apple = AppleManager.spawn(map=self.map)

            if self.display:
                self.display.update()

        return self.state.score
