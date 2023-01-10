
""" Importing """

pass

""" Packaging """

__all__ = ['Messages']

class Message:

    def __init__(self, text, func):
        """ Create a new message """

        self.text     = text
        self.func     = func

    def __str__(self):
        """ Return a string representation of a message """

        return str(self.text)

    def __call__(self, game):
        """ Execute a message """

        self.func(game)

class Messages:

    def __init__(self, *topics):
        """ Create a new Messages object """

        self.data = {k: [] for k in topics}

    def get(self, topic):
        """ Get a single message from a topic """

        if topic not in self.data.keys():
            raise KeyError(f'failed to find a {topic} topic')
        elif len(self.data[topic]) < 1:
            raise IndexError(f'{topic} topic contains no messages')
        else:
            return self.data[topic].pop(0)

    def has(self, topic):
        """ Check whether there is any outstanding messages in a topic """

        if topic not in self.data.keys():
            raise KeyError(f'failed to find a {topic} topic')
        else:
            return len(self.data[topic]) > 0

    def put(self, message, topic):
        """ Add a new message to a topic """

        if topic not in self.data.keys():
            raise KeyError(f'failed to find a {topic} topic')
        else:
            self.data[topic].append(message)
        


