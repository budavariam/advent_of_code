"""Advent of code 2025 day 05 / 1"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, num):
        return self.start <= num <= self.end

    def __repr__(self) -> str:
        return f"{self.start}-{self.end}"


class Code(object):
    def __init__(self, data):
        self.data = data

    def solve(self):
        pprint(self.data)
        result = 0
        for ing in self.data["ingredients"]:
            for r in self.data["ranges"]:
                if r.contains(ing):
                    result += 1
                    break
        return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\d+)-(\d+)")
    processed_data = {"ranges": [], "ingredients": []}
    ranges, ingredients = raw_data.split("\n\n")

    for line in ranges.split("\n"):
        match = re.match(pattern, line)
        if match is not None:
            data = Interval(int(match.group(1)), int(match.group(2)))
            processed_data["ranges"].append(data)
    for line in ingredients.split("\n"):
        processed_data["ingredients"].append(int(line))
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
