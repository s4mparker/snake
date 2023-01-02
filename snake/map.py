
""" Importing """

from .         import Direction, Sequencer
from itertools import product

""" Packaging """

__all__ = ['Map', 'Cell']

class Map:

    @staticmethod
    def generate(width, height):
        """ Generate a map of cells """

        map = [[Cell() for y in range(height)] for x in range(width)]
        for (x, y) in product(range(width), range(height)):
            left  = map[x-1][y] if x > 0 else None
            right = map[x+1][y] if x < width - 1 else None
            up    = map[x][y-1] if y > 0 else None
            down  = map[x][y+1] if y < height - 1 else None
            map[x][y].localize(x, y, left, right, up, down)

        return map

class Cell:

    def __init__(self):
        """ Create a new cell """

        self.id         = Sequencer.generate()
        self.entity     = None
        self.x = self.y = None
        self.neighbours = {
            Direction.LEFT  : None,
            Direction.RIGHT : None,
            Direction.UP    : None,
            Direction.DOWN  : None
        }

    def __str__(self):
        """ Return a string representation of a cell """

        return f'{self.id:^4}'

    def __hash__(self):
        """ Return a hash of a cell """

        return hash(self.id)

    def set(self, entity):
        """ Set a cell's entity """

        self.entity = entity

    def get(self):
        """ Get a cell's entity """

        return self.entity

    def has(self):
        """ Return True / False based on whether a cell contains an entity """

        return self.entity is not None

    def clear(self):
        """ Clear a cell's entity """

        self.entity = None

    def localize(self, x, y, left, right, up, down):
        """ Localize a cell in order to connect it to its neighbours """

        self.x, self.y                   = x, y
        self.neighbours[Direction.LEFT]  = left
        self.neighbours[Direction.RIGHT] = right
        self.neighbours[Direction.UP]    = up
        self.neighbours[Direction.DOWN]  = down

    def neighbour(self, direction):
        """ Return a cell's neighbour in a particular direction """

        return self.neighbours[direction]



