
""" Importing """

from ..             import Parameters
from pygame         import get_init, init, Surface
from pygame.display import set_mode, flip

""" Packaging """

__all__ = ['Display']

class Display:

    def __init__(self, display_parameters):
        """ Create a new display 
        
        Parameters: TBC
        """

        params           = Parameters.import_file(filename=display_parameters)
        
        if not get_init() : init()
        self.screen      = set_mode((params.get('WIDTH'), params.get('HEIGHT')))

        self.components  = []
        self.colours     = {name: Display.hexToRGB(colour=colour) for (name, colour) in params.get('COLOURS')}

    def initialize(self, game):
        """ Initialize a display """

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

        self.screen.fill(color=Display.hexToRGB('000000'))

        for (cell, surface, rect) in self.components:
            entity      = cell.getEntity()

            if entity is None:
                surface.fill(color=Display.hexToRGB('FFFFFF'))
            else:
                entity_type = type(entity).__name__
                if entity_type in self.colours:
                    surface.fill(color=self.colours.get(entity_type))
                else:
                    raise KeyError(f'unrecognised colour provided ({entity_type})')

            self.screen.blit(surface, rect)

        flip()

    @staticmethod
    def hexToRGB(colour):
        """ Convert a hex colour to RGB """

        r = int(colour[0:2],16)
        g = int(colour[2:4], 16)
        b = int(colour[4:], 16)

        return (r, g, b)
