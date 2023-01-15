
""" Importing """

from .         import Tile
from itertools import product

""" Packaging """

__all__ = ['Map']

class TileMap:

    def __init__(self, width, height):
        """ Create a new tile map
        
        Parameters:
            width  (int) : map width (x)
            height (int) : map height (y)
        """

        self.width  = width
        self.height = height

        self.tiles  = [[Tile(x=x, y=y) for y in range(height)] for x in range(width)]
        for (x, y) in product(range(width), range(height)):
            self.tiles[x][y].localize(left=self.at(x-1, y), right=self.at(x+1, y), up=self.at(x, y-1), down=self.at(x, y+1))

    def __iter__(self):
        """ Return an iterator over a map's cells """

        return iter([cell for row in self.cells for cell in row])

    def at(self, x, y, **kwargs):
        """ Return the cell at a given position within a map 
        
        Parameters:
            x (int)     : pass
            y (int)     : pass
            kwargs      : keyword arguments
                default : default value to return if no tile is found at the given position
        """

        use_default = 'default' in kwargs
        val_default = kwargs.pop('default', None)
        
        if len(kwargs) > 0:
            raise KeyError(f'unrecognised keyword argument/s ({kwargs.keys()})')

        if x < 0 or x >= self.width or y < 0 or y >= self.width:
            if use_default:
                return val_default
            else:
                raise IndexError(f'out of range')
        else:
            return self.cells[x][y]

    def size(self):
        """ Return a map's size (W x H) """

        return self.width, self.height
