
""" Importing """

from .  import Entity
from .. import Tag

""" Packaging """

__all__ = ['Snake', 'SnakeHead', 'SnakeBody']

class Snake:

    def __init__(self, messages, direction, cell):
        """ Create a new snake """

        self.messages = messages

        self.head     = SnakeHead(direction=direction)
        self.body     = []

        self.head.move(cell=cell)

    def update(self, direction):
        """ Perform a snake update """

        self.head.setDirection(direction=direction)

        present = self.head.get()
        future  = present.neighbour(direction=direction)

        if future is None:
            self.messages.put(lambda x: setattr(x, 'gameover', True), 'snake')
            return
        elif future.has() and future.get().getTag() in [Tag.HEAD, Tag.BODY]:
            self.messages.put(lambda x: setattr(x, 'gameover', True), 'snake')
            return
        else:
            self.head.move(future)

        for body in self.body:
            future  = present
            present = body.get()
            body.move(future)

        if self.messages.has('snake'):
            body = SnakeBody()
            self.body.append(body)
            body.move(present)
            self.messages.get('snake')

class SnakeBody(Entity):

    pass

class SnakeHead(Entity):

    def __init__(self, direction):
        """ Create a new snake head entity 
        
        Parameters: TBC
        """

        super().__init__()
        self.direction = direction

    def setDirection(self, direction):
        """ Set a snake head's direction 
        
        Parameters: TBC
        """

        self.direction = direction

SnakeBody.setTag(Tag.BODY)
SnakeHead.setTag(Tag.HEAD)
