""" Advent of code 2023 day 02 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def safe(self, lines):
        return sorted(lines) in [lines, lines[::-1]] and all(
            1 <= abs(a - b) <= 3 for a, b in zip(lines, lines[1:])
        )

    def solve(self):
        result = 0
        for line in self.lines:
            if self.safe(line) or any(
                self.safe(line[:i] + line[i + 1 :]) for i in range(len(line))
            ):
                result += 1
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
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
