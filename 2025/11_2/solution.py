"""Advent of code 2025 day 11 / 2"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
from functools import cache


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        start = "svr"
        end = "out"

        @cache
        def dfs(node: str, reached_dac: bool, reached_fft: bool) -> int:
            if node == end:
                return 1 if reached_dac and reached_fft else 0

            total = 0
            for nxt in self.lines[node]:
                total += dfs(
                    nxt, reached_dac or (nxt == "dac"), reached_fft or (nxt == "fft")
                )
            return total

        return dfs(start, False, False)


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\w+): (.*)")
    processed_data = {}
    for line in raw_data.split("\n"):
        line = line.strip()
        if not line:
            continue
        match = re.match(pattern, line)
        if match is None:
            continue
        processed_data[match.group(1)] = match.group(2).split(" ")
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
