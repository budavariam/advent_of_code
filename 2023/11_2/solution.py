""" Advent of code 2023 day 11 / 2 """

import math
from pprint import pprint
import heapq
from os import path
import re
from collections import deque
from itertools import combinations
import utils
import math


FOUR_NEIGHBOR = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


class Code(object):
    def __init__(self, lines, expansion_rate):
        self.galaxy_locations = lines["galaxy_locations"]
        self.empty_rows = lines["empty_rows"]
        self.empty_cols = lines["empty_cols"]
        self.maxw = lines["maxw"]
        self.maxh = lines["maxh"]
        self.expansion_rate = expansion_rate

    def shortest_paths(self, start):
        queue = [(0, start[0], start[1])]
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
                # if we move up (d_y == -1) and go into an empty row (n_y in self.empty_row), then we need to expand the distance by 1
                if d_y == -1 and a_y in self.empty_rows:
                    expansion += self.expansion_rate - 1
                # if we move left (d_x == -1) and go into an empty col (n_x in self.empty_col), then we need to expand the distance by 1
                elif d_x == -1 and a_x in self.empty_cols:
                    expansion += self.expansion_rate - 1
                # ...
                elif d_y == 1 and a_y in self.empty_rows:
                    expansion += self.expansion_rate - 1
                # ...
                elif d_x == 1 and a_x in self.empty_cols:
                    expansion += self.expansion_rate - 1

                new_distance = c_len + 1 + expansion
                if (a_y, a_x) not in distances or new_distance < distances[(a_y, a_x)]:
                    distances[(a_y, a_x)] = new_distance
                    heapq.heappush(queue, (new_distance, a_y, a_x))
        # print(distances)
        return distances

    def solve(self):
        res = {}
        for i, g in enumerate(self.galaxy_locations):
            print(f"Calculating for: {i+1}/{len(self.galaxy_locations)}")
            distances_from_galaxy = self.shortest_paths(g)
            res[g] = {
                other: distances_from_galaxy.get(other, -1)
                for other in self.galaxy_locations
                if other != g
            }
        res = sum(
            [res[g1][g2] for g1, g2 in list(combinations(self.galaxy_locations, 2))]
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
    solver = Code(lines, expansion_rate)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read(), 1000000))
