
""" Importing """

from itertools import product

""" Packaging """

__all__ = ['Map', 'Cell']

class Map:

    def __init__(self, width, height):
        """ Create a new Map object 
        
        Parameters:
            width  (int) : map width
            height (int) : map height
        """

        self.width  = width
        self.height = height

        # Create the initial set of (unlocalized) cells
        self.cells = [[Cell() for x in range(width)] for y in range(height)]

        # Connect each cell to its respective neighbours
        for (x, y) in product(range(self.width), range(self.height)):
            cell = self.cells[y][x]
            cell.localize(
                x=x,
                y=y,
                left=self.at(x-1, y, default=None),
                right=self.at(x+1, y, default=None),
                up=self.at(x, y+1, default=None),
                down=self.at(x, y-1, default=None)
            )

    def __str__(self):
        """ Return a string representation of a Map object """

        return '\n'.join([''.join([str(cell) for cell in row]) for row in self.cells])

    def __contains__(self, cell):
        """ Determine whether a Map object contains a given Cell object 
        
        Parameters:
            cell (Cell) : The Cell object to check the existence for
        """

        return cell in iter(self)

    def __iter__(self):
        """ Return an iterator which iterates over a Map object's cells """

        flat_map = [cell for row in self.cells for cell in row]
        return iter(flat_map)

    def at(self, x, y, **kwargs):
        """ Retrieve a cell from a Map object at a given (x, y) position 
        
        Parameters:
            x (int)     : x co-ordinate
            y (int)     : y co-ordinate
            **kwargs    : keyword arguments
                default : return either a provided default value or raise a KeyError exception
        """

        default_flag  = 'default' in kwargs.keys()
        default_value = kwargs.pop('default', None)

        if len(kwargs) > 0:
            raise ValueError(f'unrecognised keyword argument/s ({", ".join([kwarg for kwarg in kwargs.keys()])})')
        
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return self.cells[y][x]
        elif default_flag:
            return default_value
        else:
            raise KeyError(f'no cell found at ({x}, {y}) position')

class Cell:

    def __init__(self):
        """ Create a new Cell object """

        self.contents   = None
        self.x = self.y = None
        self.left = self.right = self.up = self.down = None

    def __str__(self):
        """ Return a string representation of a Cell object """

        cell_str = f'Cell({self.x},{self.y})'
        return f'{cell_str:^10}'

    def set(self, item):
        """ Set the contents of a Cell object 
        
        Parameters:
            item (Object) : New contents of the Cell object
        """

        self.contents = item

    def localize(self, x, y, left, right, up, down):
        """ Localize a Cell object within a Map object 
        
        Parameters:
            x     (int)  : x co-ordinate
            y     (int)  : y co-ordinate
            left  (Cell) : left neighbour
            right (Cell) : right neighbour
            up    (Cell) : up neighbour
            down  (Cell) : down neighbour
        """

        self.x     = x
        self.y     = y
        self.left  = left
        self.right = right
        self.up    = up
        self.down  = down
        
    @property
    def isOccupied(self):
        """ Determine whether a Cell object is occupied """

        return self.contents is not None

    @property
    def isLocalized(self):
        """ Determine whether a Cell object has been localized within a Map object """

        return self.x is not None and self.y is not None

    @property
    def neighbours(self):
        """ Return a Cell object's neighbours as a list """

        return [self.left, self.right, self.up, self.down]

    @property
    def neighboursCount(self):
        """ Return the number of neighbours that a Cell object is connected to """

        return sum([int(neighbour is not None) for neighbour in self.neighbours])
