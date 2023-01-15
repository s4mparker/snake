
""" Importing """

pass

""" Packaging """

__all__ = ['GameState']

class GameState:

    def __init__(self):
        """ Create a new game state """

        self.active = True
        self.score  = 0

    def __str__(self):
        """ Return a string representation of a game state """

        return f'Active: {self.active}\nScore: {self.score}'

    def __bool__(self):
        """ Determine whether a game state is active or not """

        return self.active

    def __iadd__(self, value):
        """ Add a given value to a game state's score """

        self.score += value
        return self