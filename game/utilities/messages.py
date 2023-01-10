
""" Importing """

pass

""" Packaging """

__all__ = ['MessageHandler']

class MessageHandler:

    def __init__(self):
        """ Create a new message handler 
        
        Parameters: TBC
        """

        self.messages = []

    def put(self, message):
        """ Add a new message 
        
        Parameters: TBC
        """

        self.messages.append(message)

    def get(self, *values):
        """ Get all messages of a given type
        
        Parameters: TBC
        """

        matches       = list(filter(lambda m: m in values, self.messages))
        self.messages = list(filter(lambda m: m not in values, self.messages))
        return matches

    def purge(self, *values):
        """ Delete all messages of a given type
        
        Parameters: TBC
        """

        self.messages = list(filter(lambda m: m not in values, self.messages))
