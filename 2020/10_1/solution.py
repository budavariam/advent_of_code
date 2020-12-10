""" Advent of code 2020 day 10/1 """

import math
from os import path
from functools import reduce


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def calc_jolt_differences(self, acc, curr):
        diff = curr - acc["prev"]
        acc[diff] += 1
        acc["prev"] = curr
        return acc

    def solve(self):
        differences = reduce(self.calc_jolt_differences, self.lines, {"prev": 0, 1: 0, 2: 0, 3: 1})
        return differences[1] * differences[3]


def preprocess(raw_data):
    processed_data = sorted(map(int, raw_data.split("\n")))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
