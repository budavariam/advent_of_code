""" Advent of code 2024 day 10 / 1 """

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
}


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.starts = set([])
        self.ends = set([])
        self.maxh = len(lines)
        self.maxw = len(lines[0])

    def calculate_trail(self, pos):
        result = set([])
        queue = [(*pos, 0)]
        while queue:
            y, x, val = queue.pop()
            for d_y, d_x in DIRECTIONS.values():
                n_y, n_x = add((y, x), (d_y, d_x))
                if 0 <= n_y < self.maxh and 0 <= n_x < self.maxw:
                    if self.lines[n_y][n_x] == val + 1:
                        queue.append((n_y, n_x, val + 1))
                    if val == 8 and (n_y, n_x) in self.ends:
                        result.add((n_y, n_x))
        return len(result)

    def solve(self):
        # pprint(self.lines)
        result = 0
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if c == 0:
                    self.starts.add((y, x))
                elif c == 9:
                    self.ends.add((y, x))

        for p in self.starts:
            result += self.calculate_trail(p)
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        data = [int(x) if x.isnumeric() else "." for x in line]
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
