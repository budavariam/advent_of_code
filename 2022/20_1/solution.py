""" Advent of code 2022 day 20 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

# import sys
# sys.setrecursionlimit(100000)

P_INDEX = 0
P_VAL = 1


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)

        zero_index = 0
        mixer = [(i, e) for (i, e) in enumerate(self.lines)]

        for i in range(len(self.lines)):
            for j in range(len(self.lines)):
                if mixer[j][P_INDEX] == i:
                    curr = mixer.pop(j)
                    new_index = (j + curr[P_VAL]) % len(mixer)
                    mixer.insert(new_index, (i, curr[P_VAL]))
                    break

        for (itx, (_, val)) in enumerate(mixer):
            if val == 0:
                zero_index = itx
                break

        return (
            mixer[(zero_index + 1000) % len(mixer)][P_VAL]
            + mixer[(zero_index + 2000) % len(mixer)][P_VAL]
            + mixer[(zero_index + 3000) % len(mixer)][P_VAL]
        )


@utils.profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        processed_data.append(int(line))
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
