""" Advent of code 2020 day 24/1 """

import math
from os import path
from collections import Counter
import re

DIRECTION_RULES = re.compile(r'nw|sw|ne|se|w|e')


class HexGrid(object):
    def __init__(self, data):
        self.data = data
        self.grid = {}
        self.start = (0, 0)
        self.direction = {
            'nw': (-1, 0),
            'sw': (1, -1),
            'w': (0, -1),
            'ne': (-1, +1),
            'se': (+1, 0),
            'e': (0, 1)
        }

    def get_location(self, line):
        directions = [self.direction[step]
                      for step in DIRECTION_RULES.findall(line)]
        return tuple(map(sum, zip(self.start, *directions)))

    def solve(self):
        for direction in self.data:
            location = self.get_location(direction)
            self.grid[location] = False if self.grid.get(location) else True
        return Counter(self.grid.values())[True]


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    return processed_data


def solution(input_data):
    """ Solution to the problem """
    data = preprocess(input_data)
    solver = HexGrid(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
