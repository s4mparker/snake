
""" Importing """

pass

""" Packaging """

__all__ = ['Sequencer']

class Sequencer:

    value = 1

    @classmethod
    def generate(cls):
        """ Generate the next number in the sequence """

        number = cls.value
        cls.value += 1
        return number