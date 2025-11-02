"""Advent of code 2024 day 20 / 2"""

import math
from pprint import pprint
from os import path
import re
import copy
from collections import defaultdict, Counter
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


DIRECTIONS = {  # Y, X
    "N": (-1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
}


class Code(object):
    def __init__(self, processed_data):
        self.processed_data = processed_data

    def search(self, distance_grid, start, end):
        queue = [(start, 0)]
        visited = set()

        while queue:
            curr_pos, distance = queue.pop(0)

            if curr_pos in visited:
                continue

            visited.add(curr_pos)
            curr_y, curr_x = curr_pos
            distance_grid[curr_y][curr_x] = distance

            if curr_pos == end:
                continue

            for direction in DIRECTIONS.values():
                next_pos = add(direction, curr_pos)
                next_y, next_x = next_pos

                if (
                    next_pos in visited
                    or next_y < 0
                    or next_y >= self.processed_data["bounds"]["y"]
                    or next_x < 0
                    or next_x >= self.processed_data["bounds"]["x"]
                ):
                    continue

                if distance_grid[next_y][next_x] == "#":
                    continue

                queue.append((next_pos, distance + 1))

        return distance_grid

    def find_cheats(self, distance_grid, max_cheats=20):
        # NOTE: I do not have to keep track of each run if I calculate all distances in the grid with Manhattan distance
        results = []
        path_positions = []
        for y in range(self.processed_data["bounds"]["y"]):
            for x in range(self.processed_data["bounds"]["x"]):
                curr = distance_grid[y][x]
                if curr != "#" and curr >= 0:
                    path_positions.append(((y, x), curr))

        for start_pos, start_dist in path_positions:
            for end_pos, end_dist in path_positions:
                if start_pos == end_pos:
                    continue

                manhattan = abs(start_pos[0] - end_pos[0]) + abs(
                    start_pos[1] - end_pos[1]
                )

                if manhattan <= max_cheats:
                    time_saved = end_dist - start_dist - manhattan
                    if time_saved > 0:
                        results.append(time_saved)

        return results

    def solve(self, nr_over):
        grid = copy.deepcopy(self.processed_data["map"])
        distance_grid = self.search(
            grid,
            self.processed_data["start_pos"],
            self.processed_data["end_pos"],
        )

        results = self.find_cheats(distance_grid, max_cheats=20)

        cnt = Counter(results)

        if nr_over == 50:
            # for the test return the items
            return set([(v, k) for k, v in cnt.items() if k >= nr_over])
        else:
            # for the actual run return the summary
            result = 0
            for picosec_saved, count in cnt.items():
                if picosec_saved >= nr_over:
                    result += count
            return result


@profiler
def preprocess(raw_data):
    processed_data = {"map": [], "start_pos": (-1, -1), "end_pos": (-1, -1)}
    grid = raw_data.split("\n")
    for y, line in enumerate(grid):
        data = list(line)
        for x, char in enumerate(data):
            if char == "." or char == "#":
                continue
            elif char == "S":
                processed_data["start_pos"] = (y, x)
            elif char == "E":
                processed_data["end_pos"] = (y, x)
        processed_data["map"].append(data)
    processed_data["bounds"] = {
        "y": len(grid),
        "x": len(grid[0]),
    }
    return processed_data


@profiler
def solution(data, nr_over=None):
    """Solution to the problem"""
    processed_data = preprocess(data)
    solver = Code(processed_data)
    return solver.solve(nr_over)


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read(), 100))
