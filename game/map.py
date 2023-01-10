
""" Importing """

from .         import Direction, Sequencer
from itertools import product

""" Packaging """

__all__ = ['Map', 'Cell']

class Map:

    def __init__(self, width, height):
        """ Create a new map 
        
        Parameters: TBC
        """

        self.width  = width
        self.height = height
        self.cells  = [[Cell() for y in range(height)] for x in range(width)]

        for (x, y) in product(range(width), range(height)):
            left  = self.cells[x-1][y] if x > 0 else None
            right = self.cells[x+1][y] if x < width - 1 else None
            up    = self.cells[x][y-1] if y > 0 else None
            down  = self.cells[x][y+1] if y < height - 1 else None
            self.cells[x][y].localize(x, y, left, right, up, down)

    def __iter__(self):
        """ Return an iterator over a map """

        return iter([cell for row in self.cells for cell in row])

    def at(self, x, y):
        """ Return the cell at a given position within a map 
        
        Parameters: TBC
        """

        if x < 0 or x >= self.width:
            raise IndexError(f'out of range')
        if y < 0 or y >= self.width:
            raise IndexError(f'out of range')

        return self.cells[x][y]

    def size(self):
        """ Return a map's size (W x H) """

        return self.width, self.height

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

    def setEntity(self, entity):
        """ Set a cell's entity """

        self.entity = entity

    def getEntity(self):
        """ Get a cell's entity """

        return self.entity

    def hasEntity(self):
        """ Return True / False based on whether a cell contains an entity """

        return self.entity is not None

    def clearEntity(self):
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



