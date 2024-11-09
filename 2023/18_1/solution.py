""" Advent of code 2023 day 18 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils
import sys

max_int = sys.maxsize
min_int = -sys.maxsize - 1
INTERIOR = "I"


DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


class Code(object):
    def __init__(self, lines):
        self.instructions = lines
        self.matrix = {(0, 0): "START"}
        self.bounds = (max_int, max_int, min_int, min_int)
        self.pos = (0, 0)

    def fill_interior(self, start):
        queue = [start]
        while queue:
            curr = queue.pop()
            for d in DIRECTIONS.values():
                d_y, d_x = d
                c_y, c_x = curr
                next_p = (c_y + d_y, c_x + d_x)
                if next_p in self.matrix:
                    # already visited
                    continue
                self.matrix[next_p] = INTERIOR
                queue.append(next_p)

    def draw_map(self, need_print=False):
        res = ""
        min_h, min_w, max_h, max_w = self.bounds
        # print(self.bounds)
        for y in range(min_h, max_h + 1):
            line = ""
            for x in range(min_w, max_w + 1):
                curr = (y, x)
                if x == 0 and y == 0:
                    line += "#"
                else:
                    line += "#" if curr in self.matrix else " "
            res += line + "\n"
            if need_print:
                print(line)
        return res

    def dig(self, instruction):
        next_d, count, color = instruction
        d = DIRECTIONS[next_d]
        for _ in range(count):
            d_y, d_x = d
            c_y, c_x = self.pos
            self.pos = (c_y + d_y, c_x + d_x)
            min_h, min_w, max_h, max_w = self.bounds
            self.bounds = (
                min(min_h, self.pos[0]),
                min(min_w, self.pos[1]),
                max(max_h, self.pos[0]),
                max(max_w, self.pos[1]),
            )
            self.matrix[self.pos] = color

    def solve(self):
        # pprint(self.instructions)
        result = 0
        for ins in self.instructions:
            self.dig(ins)
            # print("--------------")
        # pprint(self.matrix)
        self.fill_interior((1, 1))
        final_map = self.draw_map(need_print=False)
        # print(final_map)
        # return sum([len(x.strip(".")) for x in final_map.split("\n")])
        return final_map.count("#")


@utils.profiler
def preprocess(raw_data):
    pattern = re.compile(r"(U|D|L|R) (\d+) \(#(\w+)\)")
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = [match.group(1), int(match.group(2)), match.group(3)]
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read()))
