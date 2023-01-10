
""" Importing """

from game import *

if __name__ == '__main__':
    game = Game(game_parameters='parameters/game.yaml', controller=Controller, display=True, display_parameters='parameters/display.yaml')
    game.begin()