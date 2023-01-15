
""" Importing """

from . import Entity, ConsumeException

""" Packaging """

__all__ = ['Snake', 'SnakeHead', 'SnakeEntity']

class Snake:

    def __init__(self, state, tile):
        """ Create a new snake
        
        Parameters:
            state (State) : the associated game's state
            tile  (Tile)  : the snake's starting tile
        """

        self.state = state

        head = SnakeHead()
        head.set(tile=tile)
        self.components = [head]

    def apply(self, move):
        """ Apply a move to a snake
        
        Parameters:
            move (Direction) : the move to apply to the snake
        """

        current_tile = self.components[0].get()
        future_tile  = current_tile.neighbour(direction=move)

        if future_tile is None:
            self.state.active = False
            return

        bonus = 0
        if future_tile.has():
            try:
                bonus = future_tile.get().consume()
            except ConsumeException:
                self.state.active = False
                return
        self.state.score += bonus

        for component in self.components:
            current_tile = component.get()
            component.set(future_tile)
            future_tile = current_tile

        if bonus > 0:
            new = SnakeEntity()
            new.set(current_tile)
            self.components.append(new)

class SnakeEntity(Entity):

    def consume(self):
        """ Consume a snake entity object """

        raise ConsumeException(f'cannot consume a snake object -> game over!')

class SnakeHead(SnakeEntity):

    pass
