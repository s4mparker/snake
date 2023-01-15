
""" Importing """

from ..             import Parameters
from pygame         import get_init, init, Surface
from pygame.display import set_mode, flip

""" Packaging """

__all__ = ['Display']

class Display:

    def __init__(self, parameters):
        """ Create a new display 
        
        Parameters:
            parameters (str) : display parameters
        """

        # Display parameters
        params           = Parameters.import_file(filename=parameters)
        width, height    = params.get('WIDTH'), params.get('HEIGHT')
        colours          = params.get('COLOURS')
        
        if not get_init(): 
            init()

        self.screen      = set_mode((width, height))
        self.components  = []
        self.colours     = {name: Display.hexToRGB(colour=colour) for (name, colour) in colours}

    def initialize(self, game):
        """ Initialize a display 
        
        Parameters:
            game (Game) : the game that will be rendered by the display
        """

        w, h    = game.map.size()
        cw, ch  = self.screen.get_width() // w, self.screen.get_height() // h

        surface = Surface((cw, ch))

        for cell in game.map:
            cell_surface = surface.copy()
            cell_rect    = cell_surface.get_rect()
            cell_rect.update(cell.x * cw, cell.y * ch, cw, ch)
            self.components.append((cell, cell_surface, cell_rect))

    def update(self):
        """ Update a display """

        white = Display.hexToRGB('000000')
        black = Display.hexToRGB('FFFFFF')

        self.screen.fill(color=white)

        for (cell, surface, rect) in self.components:
            if not cell:
                surface.fill(color=black)
            else:
                entity = type(cell.get()).__name__
                colour = self.colours.get(entity, None)
                if colour:
                    surface.fill(color=colour)
                else:
                    raise KeyError(f'unrecognised colour ({entity})')

            self.screen.blit(surface, rect)

        flip()

    @staticmethod
    def hexToRGB(colour):
        """ Convert a hex colour to RGB """

        r = int(colour[0:2],16)
        g = int(colour[2:4], 16)
        b = int(colour[4:], 16)

        return (r, g, b)
