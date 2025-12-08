"""Advent of code 2025 day 04 / 1"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


DIRECTIONS = {  # Y, X
    "N": (-1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
    "NE": (-1, 1),
    "NW": (-1, -1),
    "SE": (1, 1),
    "SW": (1, -1),
}


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # pprint(self.lines)
        result = 0
        max_y = len(self.lines)
        max_x = len(self.lines[0])

        for y, line in enumerate(self.lines):
            for x, curr in enumerate(line):
                if curr == "@":
                    rolls_around = 0
                    for d in DIRECTIONS.values():
                        pos_y, pos_x = add(d, (y, x))
                        if (0 <= pos_y < max_y) and (0 <= pos_x < max_x):
                            if self.lines[pos_y][pos_x] == "@":
                                rolls_around += 1
                    if rolls_around < 4:
                        result += 1
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = list(line)
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
