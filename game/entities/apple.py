
""" Importing """

from .      import Entity
from random import choice, random

""" Packaging """

__all__ = ['Apple', 'AppleManager']

class Apple(Entity):

    value = 10

    def __init__(self):
        """ Create an apple """

        super().__init__()
        self.active = True

    def __bool__(self):
        """ Determine whether an apple is active or not """

        return self.active

    def consume(self):
        """ Consume an apple """

        self.active = False
        self.set(None)
        return self.value

class GoldenApple(Apple):

    value = 100

class AppleManager:

    @staticmethod
    def spawn(map):
        """ Spawn an apple on a provided map 
        
        Parameters:
            map (TileMap) : the map on which to spawn the apple
        """

        available = list(filter(lambda t: not t.has(), map))
        tile      = choice(available)

        apple     = Apple() if random() < 0.95 else GoldenApple()
        apple.set(tile)

        return apple
