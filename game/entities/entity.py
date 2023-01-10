
""" Importing """

pass

""" Packaging """

__all__ = ['Entity']

class Entity:

    blocks = False

    def __init__(self, cell=None):
        """ Create a new entity """

        self.cell = cell

    def move(self, cell):
        """ Move an entity to a new cell 
        
        Parameters:
            cell (Cell) : the new cell into which the move the entity
        """

        if self.cell : self.cell.clearEntity()
        self.cell = cell
        self.cell.setEntity(self)

    def get(self):
        """ Retrieve the cell an entity is in """

        return self.cell

    def doesBlock(self):
        """ Returns True / False depending on whether the entity blocks its current cell """

        return self.blocks
