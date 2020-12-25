""" Advent of code 2020 day 24/1 """

import math
from os import path
import re

DIRECTION_RULES = re.compile(r'nw|sw|ne|se|w|e')


class HexGrid(object):
    """ Representation of the infinite grid """

    def __init__(self, data):
        """ Constructor of the grid """
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

    def solve(self, limit):
        for direction in self.data:
            location = self.get_location(direction)
            if self.grid.get(location):
                del(self.grid[location])
            else:
                self.grid[location] = True

        bound = max(max(abs(y), abs(x)) for y, x in self.grid.keys())
        turned_on, next_turn = set(self.grid.keys()), set()
        for turn in range(1, limit + 1):
            for y in range(-turn-bound, bound+turn+1):
                for x in range(-turn-bound, bound+turn+1):
                    neighbour_count = sum(
                        (y+dy, x+dx) in turned_on for dy, dx in self.direction.values()
                    )
                    if (y, x) in turned_on and 1 <= neighbour_count <= 2 or \
                       (y, x) not in turned_on and neighbour_count == 2:
                        next_turn.add((y, x))
            turned_on, next_turn = next_turn, set()
        return len(turned_on)


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    return processed_data


def solution(input_data):
    """ Solution to the problem """
    data = preprocess(input_data)
    solver = HexGrid(data)
    limit = 100
    return solver.solve(limit)


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
