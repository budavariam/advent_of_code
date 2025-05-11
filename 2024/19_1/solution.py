"""Advent of code 2024 day 19 / 1"""

from os import path
import re
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        result = 0
        parts = "|".join(self.lines.get("parts"))
        regex_pattern = re.compile(f"^({parts})+$")
        for towel in self.lines.get("expected"):
            if regex_pattern.match(towel):
                result += 1
        return result


@profiler
def preprocess(raw_data):
    processed_data = {"parts": [], "expected": []}
    for i, line in enumerate(raw_data.split("\n")):
        if i == 0:
            processed_data["parts"].extend(line.split(", "))
        if i > 1:
            processed_data["expected"].append(line)
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
