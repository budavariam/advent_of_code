""" Advent of code 2017 day 13/2 """
from argparse import ArgumentParser
import re
from functools import reduce

class Scanner(object):
    """ Scanner that moves in a straight line """
    def __init__(self, scan_depth, scan_range):
        """Constructor for the scanner """
        self.depth = scan_depth
        self.range = scan_range
        self.direction = -1
        self.position = 0

    def __repr__(self):
        """ Show the data of the scanners """
        return "{}:{}/{}({})".format(self.depth, self.position, self.range, self.direction)

    def move(self):
        """ Move the scanner and return its current position """
        if (self.position == 0 and self.direction == -1) or \
           (self.position == self.range-1 and self.direction == 1):
            self.direction *= -1
        self.position += self.direction
        return self.position

    def delay(self, time):
        """ Init the position of the scanners """
        modulo = self.range - 1
        cycle = (time - 1) / modulo
        new_position = time - (cycle * modulo)
        self.direction = 1 if cycle % 2 == 0 else -1
        self.position = new_position if self.direction > 0 else modulo - new_position
        return self

class Firewall(object):
    """ Representation of the network """
    def __init__(self, data):
        """ Constructor of the node """
        self.ranges = self.parse_input(data)
        self.largest_depth = max(self.ranges)
        self.caught = []
        self.reset()

    def __repr__(self):
        """ Show the data of the firewalls """
        return "Firewall({})".format(self.largest_depth)

    @staticmethod
    def parse_input(data):
        """ load the graph """
        pattern = re.compile(r'(\d+): (\d+)')
        return {int(match.group(1)): int(match.group(2)) for match in re.finditer(pattern, data)}

    def reset(self):
        """ Reset scanners """
        self.scanners = {elem[0]: Scanner(elem[0], elem[1]) for elem in self.ranges.items()}
        self.caught = []

    def move_scanners(self):
        """ Move all scanners 1 step """
        return {scanner.depth: scanner.move() for scanner in self.scanners.values()}

    def init_scanners(self, delay):
        """ Move all scanners any step """
        return {scanner.depth: scanner.delay(delay) for scanner in self.scanners.values()}

    def simulate(self, delay):
        """ Simulate a going through """
        self.init_scanners(delay)
        user_pos = 0
        while user_pos <= self.largest_depth:
            if user_pos in self.scanners and self.scanners[user_pos].position == 0:
                self.caught = True
                break
            self.move_scanners()
            user_pos += 1
        return self.caught

    def severity(self):
        """ Depth * range of the places where got caught """
        return reduce(lambda acc, elem: acc+elem, self.caught, 0)

def solution(input_data):
    """ Solution to the problem """
    firewall = Firewall(input_data)
    delay = 0
    caught = True
    while caught:
        if delay % 10000 == 0:
            print(delay)
        caught = firewall.simulate(delay)
        firewall.reset()
        delay += 1
    return delay - 1

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
        DEBUG = """0: 3
1: 2
4: 4
6: 4"""
        print(solution(DEBUG))
