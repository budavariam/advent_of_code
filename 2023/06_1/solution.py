""" Advent of code 2023 day 06 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        result = []
        for record_time, record_distance in self.lines:
            win_times = 0
            for hold_time in range(1, record_time + 1):
                speed = hold_time
                distance = hold_time + (record_time - hold_time - 1) * speed
                # print(record_distance, distance)
                if distance > record_distance:
                    win_times += 1
            result.append(win_times)
        return math.prod(result)


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    raw_lines, raw_distances = raw_data.split("\n")
    print(raw_distances.split(": ")[1].split(" "))
    processed_data = list(
        zip(
            [int(x) for x in raw_lines.split(": ")[1].split(" ") if x != ""],
            [int(x) for x in raw_distances.split(": ")[1].split(" ") if x != ""],
        )
    )
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
