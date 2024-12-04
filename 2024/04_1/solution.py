""" Advent of code 2023 day 04 / 1 """

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
        self.maxh = len(lines)
        self.maxw = len(lines[0])

    def search(self, param: tuple[tuple[int, int], int, int]) -> int:
        d, y, x = param
        text = self.lines[y][x]
        for _ in range(len("XMAS") - 1):
            y, x = add(d, (y, x))
            if not (0 <= y < self.maxh and 0 <= x < self.maxw):
                break
            text += self.lines[y][x]
        return 1 if text == "XMAS" else 0

    def solve(self, start_letter="X"):
        # pprint(self.lines)
        result = 0

        start = []
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if c == start_letter:
                    start.extend([(d, y, x) for d in DIRECTIONS.values()])
        for p in start:
            result += self.search(p)

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
