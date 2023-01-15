
""" Importing """

from game import Game, Controller
from sys  import argv

if __name__ == '__main__':
    if len(argv) != 3:
        raise RuntimeError(f'expected two command line arguments\n\tpython3 run.py [game-parameters] [display-parameters]')
        
    game = Game(parameters=argv[1], controller=Controller, display=argv[2])
    score = game.play()
    print(f'Score: {score}')