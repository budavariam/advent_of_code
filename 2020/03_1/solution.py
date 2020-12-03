""" Advent of code 2020 day 03/1 """

import math
from os import path


class Trajectory(object):
    def __init__(self, lines, d_x, d_y):
        self.lines = lines
        self.x = 0
        self.pattern_size = len(lines[0])
        self.d_x = d_x
        self.d_y = d_y

    def solve(self):
        result = 0
        for line in self.lines:
            if line[self.x] == '#':
                result += 1
            self.x = (self.x + self.d_x) % self.pattern_size
        return result


def solution(data):
    """ Solution to the problem """
    lines = data.split("\n")
    solver = Trajectory(lines, 3, 1)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
