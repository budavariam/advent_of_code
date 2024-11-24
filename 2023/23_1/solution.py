""" Advent of code 2023 day 23 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict, deque
from utils import log, profiler
import heapq

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

FOUR_NEIGHBOR = DIRECTIONS.values()


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.maxh = len(self.lines) - 1
        self.maxw = len(self.lines[0]) - 1
        self.start = (0, 1)
        self.final = (self.maxh, self.maxw - 1)

    def print_map(self, visited):
        result = []
        for y, line in enumerate(self.lines):
            new_line = []
            for x, c in enumerate(line):
                v = (y, x) in visited
                new_line.append("o" if v else c)
            result.append(new_line)
        print("....")
        for line in result:
            print("".join(line))
        print("....")

    def solve(self):
        pprint(self.lines)

        queue = [(0, self.start, set([]))]
        result = 0
        while queue:
            distance, (curr_y, curr_x), v = heapq.heappop(queue)
            visited = set(v)
            curr_pos = (curr_y, curr_x)
            if curr_pos in visited:
                continue
            visited.add(curr_pos)
            if curr_pos == self.final:
                result = max(result, distance)
                print(distance)
                continue

            new_distance = distance + 1
            curr_val = self.lines[curr_y][curr_x]
            if curr_val in ["^", ">", "v", "<"]:
                new_y, new_x = add(DIRECTIONS[curr_val], curr_pos)
                queue.append((new_distance, (new_y, new_x), visited))
            else:
                for d in FOUR_NEIGHBOR:
                    new_y, new_x = add(d, curr_pos)
                    new_pos = (new_y, new_x)

                    if (
                        0 <= new_y <= self.maxh
                        and 0 <= new_x <= self.maxw
                        and new_pos not in visited
                    ):
                        next_val = self.lines[new_y][new_x]

                        if next_val == "#":
                            continue
                        else:
                            queue.append((new_distance, (new_y, new_x), visited))
        # self.print_map(visited)

        return result


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
