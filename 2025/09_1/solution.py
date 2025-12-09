"""Advent of code 2025 day 09 / 1"""

import math
from pprint import pprint
from os import path
from utils import log, profiler


class Code(object):
    def __init__(self, points):
        self.points = points

    def area(self, c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        # +1 because tiles are inclusive in both directions
        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

    def solve(self):
        largest = 0
        n = len(self.points)
        for i, c1 in enumerate(self.points):
            for j in range(i + 1, n):
                c2 = self.points[j]
                largest = max(largest, self.area(c1, c2))
        return largest


@profiler
def preprocess(raw_data):
    points = []
    for line in raw_data.splitlines():
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        points.append((x, y))
    return points


@profiler
def solution(data):
    points = preprocess(data)
    solver = Code(points)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
