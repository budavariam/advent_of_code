""" Advent of code 2024 day 08 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
from itertools import combinations


def add(a, b):
    return tuple(map(sum, zip(a, b)))


def diff(a, b):
    return tuple(map(lambda p: p[1] - p[0], zip(a, b)))


class Code(object):
    def __init__(self, lines):
        self.antennas = lines["antennas"]
        self.maxh = lines["maxh"]
        self.maxw = lines["maxw"]

    def calculate_antennas(self, pointpairs):
        result = []
        for a, b in pointpairs:
            d_y, d_x = add(diff(a, b), b)
            d_a, d_b = add(diff(b, a), a)
            # print(a, b, ":", (d_y, d_x), (d_a, d_b))
            if (0 <= d_y < self.maxh) and (0 <= d_x < self.maxw):
                result.append((d_y, d_x))
            if (0 <= d_a < self.maxh) and (0 <= d_b < self.maxw):
                result.append((d_a, d_b))

        return result

    def solve(self):
        # pprint(self.lines)
        result = []
        for name, antennas in self.antennas.items():
            result.extend(self.calculate_antennas(list(combinations(antennas, 2))))
        return len(set(result))


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    d = raw_data.split("\n")
    processed_data = {
        "maxh": len(d),
        "maxw": len(d[0]),
        "antennas": defaultdict(set),
    }
    for y, line in enumerate(d):
        for x, c in enumerate(line):
            if c != ".":
                processed_data["antennas"][c].add((y, x))
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
