""" Advent of code 2022 day 18 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

SIDES = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # pprint(self.lines)
        pair_cnt = 0
        for (x,y,z) in self.lines:
            for delta in SIDES:
                cnt = (x+delta[0], y+delta[1], z+delta[2])
                if cnt in self.lines:
                    pair_cnt += 1

        return 6*len(self.lines) - pair_cnt

@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = set()
    for line in raw_data.split("\n"):
        x,y,z = (int(a) for a in line.split(','))
        processed_data.add((x,y,z))
    return processed_data

@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
