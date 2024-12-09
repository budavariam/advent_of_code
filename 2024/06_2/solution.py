""" Advent of code 2024 day 06 / 2 """

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
    def __init__(self, matrix, pos, direction="N", stop_at=None, guard_path=None):
        self.direction = direction
        self.pos = pos
        self.matrix = matrix
        self.maxh = len(self.matrix)
        self.maxw = len(self.matrix[0])
        self.inside_bounds = True
        self.guard_path = guard_path
        self.stop_at = stop_at
        self.move_len = 0
        self.loop_checker = {}

    def check_pos(self, n_y, n_x):
        return 0 <= n_y < self.maxh and 0 <= n_x < self.maxw

    def print_matrix(self):
        for y, line in enumerate(self.matrix):
            pr = ""
            for x, c in enumerate(line):
                if (y, x) == (104, 112):
                    pr += "@"
                elif (y, x) in self.guard_path:
                    pr += "o"
                elif c == "#":
                    pr += "#"
                else:
                    pr += "."
            print(pr)
        print("---")
        print("---")

    def move(self):
        if not self.inside_bounds:
            return False
        n_y, n_x = add(self.pos, DIRECTIONS[self.direction])
        self.inside_bounds = self.check_pos(n_y, n_x)
        if not self.inside_bounds:
            return False
        can_move = False
        i = 0
        while not can_move and i < 3:
            if self.matrix[n_y][n_x] == "#" or self.stop_at == (n_y, n_x):
                self.direction = TURN[self.direction]
                n_y, n_x = add(self.pos, DIRECTIONS[self.direction])
            else:
                can_move = True
            i += 1
        if not can_move:
            return False
        self.pos = (n_y, n_x)
        self.guard_path.add(self.pos)

        self.inside_bounds = self.check_pos(n_y, n_x)
        self.move_len += 1
        # self.print_matrix()
        return self.inside_bounds

    def get_visited_paths(self):
        while self.inside_bounds:
            self.move()
        return set(self.guard_path)

    def find_loop(self):
        cond = True
        loop_found = False
        while cond and self.inside_bounds and not loop_found:
            prev_pos = self.pos
            cond = self.move()
            # save the step
            if (
                prev_pos in self.loop_checker
                and self.pos == self.loop_checker[prev_pos]
            ):
                ## loop is only found if it matches the prev state
                loop_found = True
            self.loop_checker[prev_pos] = self.pos
            # print(self.pos)
        # print(self.loop_found)
        return loop_found


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
        g = Guard(
            matrix=self.lines,
            direction=direction,
            pos=pos,
            stop_at=None,
            guard_path=set([pos]),
        )
        # print(f"Get visited paths...")
        paths = g.get_visited_paths()
        # print(f"Find loop...")
        looped = 0

        for i, check in enumerate(paths):
            print(f" {i}/{len(paths)-1}: {looped}", end="\r")
            g = Guard(
                matrix=self.lines,
                direction=direction,
                pos=pos,
                stop_at=check,
                guard_path=set(paths),
            )
            looped += 1 if g.find_loop() else 0
        return looped


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
