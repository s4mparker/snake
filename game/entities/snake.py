
""" Importing """

from .  import Entity
from .. import Message

""" Packaging """

__all__ = ['Snake', 'SnakeHead', 'SnakeBody']

class Snake:

    def __init__(self, messages, cell):
        """ Create a new snake """

        self.messages = messages
        self.head     = SnakeHead(cell=cell)
        self.body     = []

    def update(self, direction):
        """ Perform a snake update """

        present = self.head.get()
        future  = present.neighbour(direction=direction)

        if future is None:
            self.messages.put(Message.GAMEOVER)
            return
        elif future.hasEntity() and future.getEntity().doesBlock():
            self.messages.put(Message.GAMEOVER)
            return
        else:
            self.head.move(future)

        for body in self.body:
            future  = present
            present = body.get()
            body.move(future)

        # if self.messages.has('snake'):
        #     body = SnakeBody()
        #     self.body.append(body)
        #     body.move(present)
        #     self.messages.get('snake')

class SnakeBody(Entity):

    blocks = True

class SnakeHead(Entity):

    blocks = True
