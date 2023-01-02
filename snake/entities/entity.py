
""" Importing """

pass

""" Packaging """

__all__ = ['Entity']

class Entity:

    tag = None

    def __init__(self):
        """ Create a new entity
        
        Parameters: TBC
        """

        self.cell      = None

    def move(self, cell):
        """ Move an entity to a new cell 
        
        Parameters: TBC
        """

        if self.cell:
            self.cell.clear()
        self.cell = cell
        self.cell.set(self)

    def get(self):
        """ Retrieve the cell an entity belongs to """

        return self.cell

    @classmethod
    def setTag(cls, tag):
        """ Set an entity class' tag """

        cls.tag = tag

    def getTag(self):
        """ Get the tag associated with an entity """

        return self.tag