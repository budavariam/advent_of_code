""" Advent of code 2021 day 02/2 """

import math
from os import path
import re


class Code(object):
    pattern = re.compile(r'(\w+) (\d+)')

    def __init__(self, lines):
        self.lines = []
        for line in lines:
            match = re.match(self.pattern, line)
            self.lines.append([match.group(1), int(match.group(2))])

    def solve(self):
        hor = 0
        dep = 0
        for [direct, num] in self.lines:
            if direct == 'forward':
                hor += num
            elif direct == 'down':
                dep += num
            elif direct == 'up':
                dep -= num
        print(self.lines)
        res = hor * dep
        return res


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
