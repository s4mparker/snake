
""" Importing """

import json
import yaml
from os.path import splitext

""" Packaging """

__all__ = ['Parameters']

class Parameters:

    ACCEPTS = [int, float, str, bool]

    def __init__(self, filename):
        """ Create a new Parameters object 
        
        Parameters:
            filename (str) : file containing parameters
        """

        extension = splitext(filename)[1]
        
        with open(filename, mode='r') as file:
            data = None
            match extension:
                case '.json' : data = json.load(file)
                case '.yaml' : data = yaml.load(file, Loader=yaml.SafeLoader)
                case _       : raise ValueError(f'unrecognized filetype - {extension}')
            self.add(**data)
            
    def __str__(self):
        """ Return a string representation of a Parameters object """

        parameter_str = ''
        for (name, value) in self.__dict__.items():
            parameter_str += f'{str(name):<10}: {str(value):<10} ({type(value).__name__})\n'
        return parameter_str

    def add(self, **parameters):
        """ Add a parameters to an existing Parameters object
        
        Parameters:
            **parameters: (name, value) pairs
        """

        for (name, value) in parameters.items():
            if type(value) not in self.ACCEPTS:
                raise TypeError(f'unexpected type - recieved a {type(value)}, only accepts {", ".join([t.__name__ for t in self.ACCEPTS])}')
            
            setattr(self, name, value)

    def export(self, filename):
        """ Export a Parameters object to an external file 
        
        Parameters:
            filename (str) : outputted filename
        """

        extension = splitext(filename)[1]

        with open(filename, mode='w') as file:
            data = self.__dict__
            match extension:
                case '.json' : json.dump(data, file, indent=2)
                case '.yaml' : yaml.dump(data, file, Dumper=yaml.SafeDumper)
                case _       : raise ValueError(f'unrecognized filetype - {extension}')
                