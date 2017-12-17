""" Advent of code 2017 day 17/2 """
from argparse import ArgumentParser

class Spinlock(object):
    """ Spinlock implementation """
    def __init__(self, init):
        """Constructor for the twister """
        self.stepforward = int(init)
        self.data = -1

    def __repr__(self):
        """Representation of the spinlock """
        return "Spinlock({})".format(self.stepforward)

    def process(self, count):
        """ Store the number when the spin is at the first position """
        next_pos = 0
        for cycle in range(1, count + 1):
            next_pos = (next_pos + self.stepforward) % cycle + 1
            if next_pos == 1:
                self.data = cycle
        return self.data

def solution(data):
    """ Solution to the problem """
    lock = Spinlock(data)
    return lock.process(50000000)

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
        DEBUG = """3"""
        print(solution(DEBUG))
