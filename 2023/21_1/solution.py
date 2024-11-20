""" Advent of code 2023 day 21 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict, deque
from utils import log, profiler

OPP_DIRECTIONS = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W",
}
DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Code(object):
    def __init__(self, lines, remaining_steps):
        self.lines = lines
        self.remaining_steps = remaining_steps
        self.maxh = len(self.lines)
        self.maxw = len(self.lines[0])
        self.pos = (0, 0)
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if c == "S":
                    self.pos = (y, x)
                    break
            if self.pos != (0, 0):
                break

    def print_map(self, visited, lvl, start):
        display_map = []
        cnt = 0
        for y, line in enumerate(self.lines):
            new_line = []
            for x, c in enumerate(line):
                if c == "#":
                    new_line.append("#")
                elif ((y, x), lvl) in visited:
                    cnt += 1
                    if (y, x) == start:
                        new_line.append("s")
                    else:
                        new_line.append("o")
                elif (y, x) == start:
                    new_line.append("S")
                else:
                    new_line.append(".")
            display_map.append(new_line)
        log.debug(".... lvl: %d", lvl)
        for line in display_map:
            log.debug("".join(line))
        log.debug(".... cnt: %d", cnt)
        log.debug("....")

    def solve(self):
        # pprint(self.lines)
        # log.debug(self.pos)

        queue = deque([(self.pos, 0)])
        visited = set([])
        curr_level = 0
        while queue:
            curr, level = queue.popleft()
            if curr_level > self.remaining_steps + 1:
                break
            if (curr, level) in visited:
                # log.info("Already visited! %s %d", curr, level)
                continue
            if level > curr_level:
                # self.print_map(visited, curr_level, self.pos)
                curr_level = level
            visited.add((curr, level))
            for d in DIRECTIONS.values():
                new_y, new_x = add(d, curr)
                new_level = level + 1
                if (
                    (((new_y, new_x), new_level) not in visited)
                    and 0 <= new_y < self.maxh
                    and 0 <= new_x < self.maxw
                    and self.lines[new_y][new_x] in [".", "S"]
                ):
                    queue.append(((new_y, new_x), new_level))
        result = [0 for (_, lvl) in visited if lvl == self.remaining_steps].count(0)
        return result


@profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = list(line)
        processed_data.append(data)
    return processed_data


@profiler
def solution(data, remaining_steps):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines, remaining_steps)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read(), 64))
