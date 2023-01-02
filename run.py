
""" Importing """

from snake import *
from time  import sleep

if __name__ == '__main__':
    game    = Game(game_parameters='parameters/game.yaml', controller=None, display=True, display_parameters='parameters/graphics.yaml')
    display = game.getDisplay()

    game.begin()