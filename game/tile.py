
""" Importing """

from . import Direction, Sequencer

""" Packaging """

__all__ = ['Tile']

class Tile:

    def __init__(self, x, y):
        """ Create a new tile 
        
        Parameters:
            x (int) : tile's x co-ordinate
            y (int) : tile's y co-ordinate
        """

        self.id         = Sequencer.generate()
        self.entity     = None
        self.x, self.y  = x, y
        self.neighbours = {k: None for k in Direction}

    def __str__(self):
        """ Return a string representation of a tile """

        return f'{self.id:^4}'

    def __hash__(self):
        """ Return a hash of a tile """

        return hash(self.id)

    def has(self):
        """ Determine whether a tile has been assigned an entity """

        return self.entity is not None

    def set(self, entity):
        """ Assign a tile an entity
        
        Parameters:
            entity (Entity) : entity to be associated with the tile
        """

        self.entity = entity

    def get(self):
        """ Get a tile's assigned entity """

        return self.entity

    def clear(self):
        """ Clear a tile's assigned entity """

        self.entity = None

    def localize(self, left, right, up, down):
        """ Localize a tile in order to connect it to its neighbouring tiles
        
        Parameters:
            left  (Tile) : tile's 'left' neighbour
            right (Tile) : tile's 'right' neighbour
            up    (Tile) : tile's 'up' neighbour
            down  (Tile) : tile's 'down' neighbour
        """

        self.neighbours.update({Direction.LEFT: left, Direction.RIGHT: right, Direction.UP: up, Direction.DOWN: down})

    def neighbour(self, direction):
        """ Return a tile's neighbour in a particular direction 
        
        Parameters:
            direction (Direction) : the direction in which to get the neighbour
        """

        return self.neighbours[direction]
