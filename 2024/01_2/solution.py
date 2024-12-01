""" Advent of code 2023 day 01 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict, Counter
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        result = 0
        a = sorted([x[0] for x in self.lines])
        b = Counter([x[1] for x in self.lines])
        for i, _ in enumerate(self.lines):
            result += abs(b[a[i]] * a[i])
        return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\d+)\s+(\d+)")
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = [int(match.group(1)), int(match.group(2))]
        # data = line
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
