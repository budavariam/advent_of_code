""" Advent of code 2017 day 16/1 """
from argparse import ArgumentParser
import re

def char_range(char_a, char_b):
    """Generates the characters from `char_a` to `char_b`, inclusive."""
    for char in range(ord(char_a), ord(char_b)+1):
        yield chr(char)

def find_indexes(data, prog_a, prog_b):
    """ Return the index of the elements in the proper order """
    pos_a, pos_b = -1, -1
    for index, elem in enumerate(data):
        if elem == prog_a:
            pos_a = index
        elif elem == prog_b:
            pos_b = index
        elif pos_a > 0 and pos_b > 0:
            break
    return pos_a, pos_b

class Dance(object):
    """ Dance moves coordinator """
    def __init__(self, data, start, end):
        """Constructor for moves """
        self.data = data.split(',')
        self.progs = list(char_range(start, end))
        self.rspin = re.compile(r's(\d+)')
        self.rexchange = re.compile(r'x(\w+)\/(\w+)')
        self.rpartner = re.compile(r'p(\w)\/(\w)')

    def __repr__(self):
        return ''.join(self.progs)

    def process(self):
        """ Play the dance moves """
        for elem in self.data:
            if elem[0] == 's':
                match = re.match(self.rspin, elem)
                self.progs = self.spin(self.progs, int(match.group(1)))
            if elem[0] == 'x':
                match = re.match(self.rexchange, elem)
                self.progs = self.exchange(self.progs, int(match.group(1)), int(match.group(2)))
            if elem[0] == 'p':
                match = re.match(self.rpartner, elem)
                self.progs = self.partner(self.progs, match.group(1), match.group(2))

    @staticmethod
    def spin(data, count):
        """ Get the last n programs to the front """
        return data[-count:] + data[:-count]

    @classmethod
    def exchange(cls, data, pos_a, pos_b):
        """ Swap position A with position B """
        data[pos_b], data[pos_a] = data[pos_a], data[pos_b]
        return data

    @staticmethod
    def partner(data, prog_a, prog_b):
        """ Swap places of the programs """
        pos_a, pos_b = find_indexes(data, prog_a, prog_b)
        return Dance.exchange(data, pos_a, pos_b)

def solution(data):
    """ Solution to the problem """
    dance = Dance(data, 'a', 'p')
    for index in range(1000000000):
        if (index % 1000000) == 0:
            print(index)
            dance.process()
    return ''.join(dance.progs)

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(input_file.read()))
    elif ARGS.test:
        print(solution(str(ARGS.test)))
    else:
        DEBUG = """s1,x3/4,pe/b"""
        print(solution(DEBUG))
