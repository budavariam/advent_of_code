"""Advent of code 2025 day 06 / 2"""

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
        read_order = list(zip(*self.lines))[::-1]

        numbers = []
        for x in read_order:
            line = list(x)
            op = line.pop().strip()
            num_str = "".join(line).strip()
            if num_str == "" and op == "":
                numbers = []
                continue
            num = int(num_str)
            numbers.append(num)
            if op == "+":
                result += sum(numbers)
            if op == "*":
                result += math.prod(numbers)
            
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        data = line
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
