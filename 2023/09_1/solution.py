""" Advent of code 2023 day 09 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def calc_next_extrapolated(self, original):
        curr_line = original
        finished = False
        lines = [original]

        while not finished:
            next_line = []
            all_zeroes = True
            for a, b in zip(curr_line, curr_line[1:]):
                diff = b - a
                if diff != 0:
                    all_zeroes = False
                next_line.append(diff)
            lines.append(next_line)
            curr_line = next_line
            if all_zeroes:
                finished = True
        print(original, lines)
        next_extrapolated = 0
        for x in range(len(lines)):
            next_extrapolated += lines[x][-1]
        return next_extrapolated

    def solve(self):
        pprint(self.lines)
        result = 0
        for line in self.lines:
            result += self.calc_next_extrapolated(line)
        return result


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        data = list(map(int, line.split(" ")))
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read()))
