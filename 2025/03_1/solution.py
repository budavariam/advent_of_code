"""Advent of code 2025 day 03 / 1"""

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
            num_a = -1
            num_b = -1
            for i, x in enumerate(line):
                curr_num = int(x)
                if i < len(line) - 1 and num_a == -1 and curr_num > num_a:
                    num_a = curr_num
                    num_b = -1
                elif i < len(line) - 1 and num_a != -1 and curr_num > num_a:
                    num_a = curr_num
                    num_b = -1
                elif num_a != -1 and curr_num > num_b:
                    num_b = curr_num
            num = num_a * 10 + num_b
            print(f"Selected number is: '{num}' ({num_a}, {num_b})")
            result += num
        return result


@profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
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
