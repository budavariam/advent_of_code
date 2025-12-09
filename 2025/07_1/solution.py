"""Advent of code 2025 day 07 / 1"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        d = self.lines
        result = 0
        visited = set()
        visited_splitter = set()
        splitters = set(d["splitters"])
        queue = [d["start"]]
        while queue:
            current = queue.pop()
            if current in visited:
                continue
            visited.add(current)
            if current[0] > d["max_y"]:
                continue
            if current in splitters:
                # split left and down
                queue.append(add(current, (1, -1)))
                # split right and down
                queue.append(add(current, (1, 1)))
                visited_splitter.add(current)
            else:
                # move down
                queue.append(add(current, (1, 0)))

        return len(visited_splitter)


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    splitted = raw_data.split("\n")
    processed_data = {
        "map": [],
        "start": (-1, -1),
        "splitters": [],
        "max_y": len(splitted),
    }
    for y, line in enumerate(splitted):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = list(line)
        for x, c in enumerate(line):
            if c == "S":
                processed_data["start"] = (y, x)
            if c == "^":
                processed_data["splitters"].append((y, x))
        processed_data["map"].append(data)
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
