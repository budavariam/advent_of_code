""" Advent of code 2023 day 02 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        result = 0
        for line in self.lines:
            increasing = line[1] - line[0] > 0
            for a, b in zip(line, line[1:]):
                if increasing and not (1 <= (b - a) <= 3):
                    break
                if not increasing and not (-3 <= (b - a) <= -1):
                    break
            else:
                result += 1

        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        print("AAA", line)
        data = [int(x, 10) for x in line.split(" ")]
        processed_data.append(data)
    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
