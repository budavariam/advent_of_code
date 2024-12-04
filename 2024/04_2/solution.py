""" Advent of code 2023 day 04 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


D = {  # Y, X
    "NE": (-1, 1),
    "SW": (1, -1),
    "NW": (-1, -1),
    "SE": (1, 1),
}


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.maxh = len(lines)
        self.maxw = len(lines[0])

    def search(self, pos: tuple[int, int]) -> int:
        y, x = pos
        center = (y, x)

        def c(direction):
            n_y, n_x = add(D[direction], center)
            return self.lines[n_y][n_x]

        diag_a = set([c("NE"), c("SW")])
        diag_b = set([c("NW"), c("SE")])
        check = set(["M", "S"])
        return 1 if (diag_a == check) and (diag_b == check) else 0

    def collect_start_points(self, start_letter):
        start = []
        for y, line in enumerate(self.lines):
            if y == 0 or y == self.maxh - 1:
                continue
            for x, c in enumerate(line):
                if x == 0 or x == self.maxw - 1:
                    continue
                if c == start_letter:
                    start.append((y, x))
        return start

    def solve(self, start_letter="A"):
        start = self.collect_start_points(start_letter)
        result = 0
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
