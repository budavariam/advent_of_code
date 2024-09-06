""" Advent of code 2023 day 11 / 2 """

import math
from pprint import pprint
import heapq
from os import path
import re
from collections import deque
from functools import total_ordering
from itertools import combinations
import utils
import cmath


FOUR_NEIGHBOR = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]
EXPANSION_RATE = 1
# LT = 0
# NEW = 0

# @total_ordering
class CustomComplex(complex):
    """Imaginary part is the huge distance, real part is a real number"""

    def __new__(cls, real, imag=0):
        # n_real = real
        # n_imag = imag
        # if real > EXPANSION_RATE:
        #     how_many_times = real // EXPANSION_RATE
        #     n_real = real % EXPANSION_RATE
        #     n_imag = imag + how_many_times
        # return super().__new__(cls, real=n_real, imag=n_imag)

        return super().__new__(cls, real=real % EXPANSION_RATE, imag=imag + (real // EXPANSION_RATE))

    def __eq__(self, other):
        # global NEW
        # NEW += 1
        return self.imag == other.imag and self.real == other.real

    def __lt__(self, other):
        # global LT
        # LT += 1
        if self.imag == other.imag:
            return self.real < other.real
        else:
            return self.imag < other.imag

    def __abs__(self) -> int:
        return int(self.imag) * int(EXPANSION_RATE) + int(self.real)


class Code(object):
    def __init__(self, lines):
        self.galaxy_locations = lines["galaxy_locations"]
        self.empty_rows = lines["empty_rows"]
        self.empty_cols = lines["empty_cols"]
        self.maxw = lines["maxw"]
        self.maxh = lines["maxh"]

    def shortest_paths(self, start):
        queue = [(CustomComplex(0), start[0], start[1])]
        visited = set()
        distances = {}
        while queue:
            c_len, c_y, c_x = heapq.heappop(queue)
            if (c_y, c_x) in visited:
                continue
            visited.add((c_y, c_x))
            for d_y, d_x in FOUR_NEIGHBOR:
                a_y = c_y + d_y
                a_x = c_x + d_x
                # print(f"{c_pos}+({d_y},{d_x}) -> ({a_y}, {a_x}): {c_len}")
                if not ((0 <= a_y <= self.maxh) and (0 <= a_x <= self.maxw)):
                    # do not explore out of bounds
                    continue

                expansion = 0
                # if we move up (d_y == -1) and go into an empty row (n_y in self.empty_row), then we need to expand the distance by 1 and so on...
                if (d_y != 0 and a_y in self.empty_rows) or (d_x != 0 and a_x in self.empty_cols):
                    expansion += 1
                new_distance = CustomComplex(c_len.real + 1, c_len.imag + expansion)
                if (a_y, a_x) not in distances or new_distance < distances[(a_y, a_x)]:
                    distances[(a_y, a_x)] = new_distance
                    heapq.heappush(queue, (new_distance, a_y, a_x))
        # print(distances)
        return distances

    def solve(self):
        res = {}
        # global LT, NEW
        for i, g in enumerate(self.galaxy_locations):
            print(f"Calculating for: {i+1}/{len(self.galaxy_locations)}")
            # print(f"Calculating for: {i+1}/{len(self.galaxy_locations)} {LT}, {NEW}")
            distances_from_galaxy = self.shortest_paths(g)
            res[g] = {
                other: distances_from_galaxy.get(other, -1)
                for other in self.galaxy_locations
                if other != g
            }
        res = sum(
            [
                abs(res[g1][g2])
                for g1, g2 in list(combinations(self.galaxy_locations, 2))
            ]
        )
        return res


@utils.profiler
def preprocess(raw_data):
    matrix = raw_data.split("\n")
    col_has_galaxy = set()
    processed_data = {
        "empty_rows": set(),
        "empty_cols": set(),
        "galaxy_locations": [],
        "maxw": len(matrix[0]),
        "maxh": len(matrix),
    }
    for y, line in enumerate(matrix):
        row_has_galaxy = False
        for x, c in enumerate(line):
            if c == "#":
                processed_data["galaxy_locations"].append((y, x))
                row_has_galaxy = True
                col_has_galaxy.add(x)
        if not row_has_galaxy:
            processed_data["empty_rows"].add(y)

    col_indices = set(range(0, len(matrix[0])))
    processed_data["empty_cols"] = col_indices.difference(col_has_galaxy)

    return processed_data


@utils.profiler
def solution(data, expansion_rate):
    """Solution to the problem"""
    lines = preprocess(data)
    global EXPANSION_RATE
    EXPANSION_RATE = expansion_rate - 1
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read(), 1000000))
