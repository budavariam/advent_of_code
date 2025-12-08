"""Advent of code 2025 day 03 / 2"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from functools import cache
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        result = 0
        for line in self.lines:
            if line.strip():
                result += self.max_joltage(line.strip())
        return result

    @cache
    def max_joltage(self, bank):
        n = len(bank)

        @cache
        def dp(i, used):
            if used == 12:
                return 0
            if i == n:
                return float("-inf")

            # skip this digit
            skip = dp(i + 1, used)

            # take this digit
            take = float("-inf")
            if used < 12:
                take = int(bank[i]) * (10 ** (11 - used)) + dp(i + 1, used + 1)

            return max(skip, take)

        return dp(0, 0)


@profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = line.strip()
        if data:  # skip empty lines
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
