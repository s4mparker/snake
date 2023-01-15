
""" Importing """

pass

""" Packaging """

__all__ = ['Entity', 'ConsumeException']

class Entity:

    def __init__(self):
        """ Create a new entity """

        self.tile = None

    def set(self, tile):
        """ Set an entity's assigned tile
        
        Parameters:
            tile (Tile) : the tile to be occupied
        """

        if self.tile:
            self.tile.clear()
        if tile:
            tile.set(entity=self)
        self.tile = tile

    def get(self):
        """ Get an entity's assigned tile """

        return self.tile

    def consume(self):
        """ Consume an entity """

        raise NotImplementedError(f'consume() must be defined by a subclass class')

class ConsumeException(Exception):

    pass
