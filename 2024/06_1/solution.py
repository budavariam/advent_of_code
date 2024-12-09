""" Advent of code 2024 day 06 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


DIRECTIONS = {  # Y, X
    "N": (-1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
}
TURN = {
    "N": "E",
    "E": "S",
    "W": "N",
    "S": "W",
}


class Guard(object):
    def __init__(self, matrix, pos, direction="N"):
        self.direction = direction
        self.pos = pos
        self.matrix = matrix
        self.maxh = len(self.matrix)
        self.maxw = len(self.matrix[0])
        self.inside_bounds = True
        self.guard_path = [pos]

    def check_pos(self, n_y, n_x):
        return 0 <= n_y < self.maxh and 0 <= n_x < self.maxw

    def move(self):
        if not self.inside_bounds:
            return False
        n_y, n_x = add(self.pos, DIRECTIONS[self.direction])
        self.inside_bounds = self.check_pos(n_y, n_x)
        if not self.inside_bounds:
            return False
        if self.matrix[n_y][n_x] == "#":
            self.direction = TURN[self.direction]
            # print(f"Guard turned at: ({n_y},{n_x})")
            n_y, n_x = add(self.pos, DIRECTIONS[self.direction])
        self.pos = (n_y, n_x)
        self.guard_path.append(self.pos)
        self.inside_bounds = self.check_pos(n_y, n_x)
        return self.inside_bounds


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def find_guard(self, matrix) -> tuple[tuple[int, int], str]:
        for y, line in enumerate(matrix):
            for x, c in enumerate(line):
                if c == "^":
                    return ((y, x), "N")
        print("GUARD NOT FOUND!!")
        return ((-1, -1), "N")

    def solve(self):
        # pprint(self.lines)
        result = 0
        pos, direction = self.find_guard(self.lines)
        g = Guard(matrix=self.lines, direction=direction, pos=pos)
        while g.inside_bounds:
            g.move()
        return len(set(g.guard_path))


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
