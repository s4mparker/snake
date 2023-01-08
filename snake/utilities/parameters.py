
""" Importing """

import json
import yaml
from os.path import splitext

""" Packaging """

__all__ = ['Parameters']

class Parameters:

    @staticmethod
    def import_file(filename):
        """ Import an external file 
        
        Parameters:
            filename (str) : external file
        """

        extension = splitext(filename)[1]

        with open(file=filename, mode='r') as file:
            match extension:
                case '.json' : return json.load(fp=file)
                case '.yaml' : return yaml.load(stream=file, Loader=yaml.SafeLoader)
                case _       : raise ValueError(f'unrecognized filetype ({extension})')

    @staticmethod
    def export_file(object, filename):
        """ Export an object to an external file 
        
        Parameters:
            object   (Object) : python object
            filename (str)    : external file
        """

        extension = splitext(filename)[1]

        with open(file=filename, mode='w') as file:
            match extension:
                case '.json' : json.dump(obj=object, fp=file, indent=4)
                case '.yaml' : yaml.dump(data=object, stream=file, Dumper=yaml.SafeDumper, sort_keys=False, canonical=True)
                case _       : raise ValueError(f'unrecognized filetype ({extension})')

if __name__ == '__main__':
    data = {
        'WIDTH': 40,
        'HEIGHT': 40,
        'STARTX': 20,
        'STARTY': 20,
        'DIRECTION': 'left',
        'PERIOD': 0.1
    }

    Parameters.export_file(data, '../../parameters/game.yaml')

    data = {
        'WIDTH': 280,
        'HEIGHT': 280,
        'COLOURS' : [('SnakeHead', '0101FF'), ('SnakeBody', '010188')]
    }

    Parameters.export_file(data, '../../parameters/display.yaml')