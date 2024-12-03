""" Advent of code 2023 day 03 / 2 """

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
        result = 0
        for a, b in self.lines:
            result += a * b
        return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
    data = re.findall(pattern, raw_data)
    processed_data = []
    enabled = True
    for line in data:
        if line[0] == "":
            enabled = line[3] == ""
        elif enabled:
            x, y, _, _ = line
            processed_data.append((int(x), int(y)))
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
