
""" Importing """

from game import Parameters

if __name__ == '__main__':
    data = {
        'WIDTH': 20,
        'HEIGHT': 20,
        'STARTX': 10,
        'STARTY': 10,
        'DIRECTION': 'right',
        'PERIOD': 0.1
    }

    Parameters.export_file(data, 'parameters/game.yaml')

    data = {
        'WIDTH': 600,
        'HEIGHT': 600,
        'COLOURS' : [('SnakeHead', '0101BF'), ('SnakeEntity', '89CFF0'), ('Apple', 'EE0101'), ('GoldenApple', 'FFD700')]
    }

    Parameters.export_file(data, 'parameters/display.yaml')