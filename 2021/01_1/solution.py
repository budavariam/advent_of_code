""" Advent of code 2021 day 01/1 """

import math
from os import path


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        res = list(zip(self.lines, self.lines[1:]))
        return [int(b) > int(a) for [a,b] in res].count(True)


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
