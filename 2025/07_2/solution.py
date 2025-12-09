"""Advent of code 2025 day 07 / 2"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Code(object):
    def __init__(self, data):
        self.grid = data["map"]
        self.start = data["start"]
        self.max_y = data["max_y"]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows else 0

    def solve(self):
        # timelines[y][x] = number of timelines at cell (y, x)
        timelines = [[0] * self.cols for _ in range(self.rows)]
        sy, sx = self.start
        timelines[sy][sx] = 1

        # propagate from start row downwards
        for y in range(sy, self.rows - 1):
            for x in range(self.cols):
                k = timelines[y][x]
                if k == 0:
                    continue

                cell = self.grid[y][x]
                ny = y + 1
                if cell == "^":
                    # split: left-down and right-down
                    if x - 1 >= 0:
                        timelines[ny][x - 1] += k
                    if x + 1 < self.cols:
                        timelines[ny][x + 1] += k
                else:
                    # empty or S or whatever: straight down
                    timelines[ny][x] += k

        # answer: total timelines reaching any cell below the last splitter row
        bottom_y = self.rows - 1
        result = sum(timelines[bottom_y][x] for x in range(self.cols))
        return result


@profiler
def preprocess(raw_data):
    splitted = raw_data.split("\n")
    processed_data = {
        "map": [],
        "start": (-1, -1),
        "splitters": [],
        "max_y": len(splitted),
    }
    for y, line in enumerate(splitted):
        if not line:
            continue
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
