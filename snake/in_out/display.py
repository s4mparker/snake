
""" Importing """

from ..             import Parameters, Tag
from pygame         import get_init, init, Surface
from pygame.display import set_mode, flip
from pygame.draw    import polygon

""" Packaging """

__all__ = ['Display']

class Display:

    def __init__(self, display_parameters):
        """ Create a new display """

        if not get_init() : init()

        self.params     = Parameters(filename=display_parameters)
        self.screen     = set_mode((self.params.width, self.params.height))
        self.game       = None
        self.components = {}

    def initialize(self, game, width, height):
        """ Initialize a display """

        self.game = game

        cw     = int(self.params.width / width)
        ch     = int(self.params.height / height)

        bmin = self.params.border
        bmax = 1 - self.params.border

        points = [(bmin * cw, bmin * ch), (bmax * cw, bmin * ch), (bmax * cw, bmax * ch), (bmin * cw, bmax * ch)]

        base = Surface((cw, ch))
        base.fill(color=Display.hexToRGB('000000'))
        sub_base = polygon(surface=base, color=Display.hexToRGB('FFFFFF'), points=points)

        self.components.update({None: base})

        for tag in Tag:
            name       = tag.value
            colour_hex = getattr(self.params, name)
            colour_rgb = Display.hexToRGB(colour_hex)

            component = base.copy()
            component.fill(color=colour_rgb, rect=sub_base)
            self.components.update({tag: component})

    def update(self):
        """ Update a display """

        self.screen.fill(Display.hexToRGB('000000'))

        for cell in self.game:
            key = None
            
            if cell.has():
                key = cell.get().getTag()
            
            component      = self.components[key]
            w, h = component.get_width(), component.get_height()

            component_rect = component.get_rect()
            component_rect.update(cell.x * w, cell.y * h, w, h)

            self.screen.blit(component, component_rect)
            
        flip()

    @staticmethod
    def hexToRGB(colour):
        """ Convert a hex colour to RGB """

        r = int(colour[0:2],16)
        g = int(colour[2:4], 16)
        b = int(colour[4:], 16)

        return (r, g, b)
