
""" Importing """

from game import Parameters

if __name__ == '__main__':
    data = {
        'WIDTH': 40,
        'HEIGHT': 40,
        'STARTX': 20,
        'STARTY': 20,
        'DIRECTION': 'left',
        'PERIOD': 0.1
    }

    Parameters.export_file(data, 'parameters/game.yaml')

    data = {
        'WIDTH': 280,
        'HEIGHT': 280,
        'COLOURS' : [('SnakeHead', '0101FF'), ('SnakeEntity', '010188'), ('Apple', 'EE0101')]
    }

    Parameters.export_file(data, 'parameters/display.yaml')