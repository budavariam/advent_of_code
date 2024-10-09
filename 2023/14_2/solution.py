""" Advent of code 2023 day 14 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

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

MAPPING = str.maketrans({".": "0", "#": "1", "O": "1"})


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def hash(self, data):
        return sum([int("".join(line).translate(MAPPING), 2) for line in data])

    def rotate(self, direction, raw, first):
        result = []
        if direction == "N":
            if first:
                return [list(row) for row in zip(*raw)][::-1]
            else:
                return [list(row) for row in zip(*raw[::-1])]
        elif direction == "S":
            if first:
                return [list(row) for row in zip(*raw[::-1])]
            else:
                return [list(row) for row in zip(*raw)][::-1]
        elif direction == "W":
            result = raw
        elif direction == "E":
            result = [row[::-1] for row in raw[::-1]]
        return result

    def tilt(self, direction, data):
        # pprint(data)
        new_data = self.rotate(direction, data, True)
        result = []
        for line in new_data:
            connected = "".join(line)
            tilted = "#".join(
                ["".join(sorted(list(x), reverse=True)) for x in connected.split("#")]
            )
            # print(line, tilted)
            result.append(tilted)
        result = self.rotate(direction, result, False)
        return result

    def calc_load(self, data):
        res = sum([(y + 1) * line.count("O") for y, line in enumerate(reversed(data))])
        return res

    def solve(self):
        data = self.lines
        i = 0
        visited = {}
        order = []
        iteration_num = 1000000000
        matching_interval = (-1, -1)
        while i < iteration_num:
            for d in "NWSE":
                data = self.tilt(d, data)
            i += 1
            hsh = self.hash(data)
            order.append(data)
            if hsh not in visited:
                visited[hsh] = i
            else:
                print(f"FOUND LOOP ON STEP {i} matches with step {visited[hsh]}")
                matching_interval = (visited[hsh], i)  # open ended
                break
        interval_width = matching_interval[1] - matching_interval[0]
        relevant_matrix = order[
            matching_interval[0]
            + ((iteration_num - matching_interval[0]) % interval_width)
            - 1 # array index start from 0
        ]

        result = self.calc_load(relevant_matrix)
        return result


@utils.profiler
def preprocess(raw_data):
    processed_data = []
    for data in raw_data.split("\n"):
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
