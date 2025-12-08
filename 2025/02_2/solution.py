""" Advent of code 2025 day 02 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler

def is_invalid(s):
    i = (s+s).find(s, 1, -1)
    # return 1None if i == -1 else s[:i]
    return i != -1

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        result = 0
        for s,e in self.lines:
            for current_id in range(s, e+1):
                if is_invalid(str(current_id)):
                    result += current_id
                    print(f"Invalid ID found: {current_id}")
        return result


@profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split(","):
        data = tuple(map(int, line.split("-")))
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
