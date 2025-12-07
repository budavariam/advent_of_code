""" Advent of code 2025 day 01 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        result = 0
        curr = 50
        size = 100

        for d, num in self.lines:
            direction = 1 if d == "R" else -1
            for _ in range(num):
                curr = (curr + direction) % size
                if curr == 0:
                    result += 1
        return result

    # def solve(self):
    #     pprint(self.lines)
    #     result = 0
    #     curr = 50
    #     size = 100
    #     for [d, num] in self.lines:
    #     #     direction = 1 if d == "R" else -1
    #     #     f
    #     #     step = direction * num
    #     #     mid = math.floor((curr + abs(step)) / size)
    #     #     curr = (curr + step) % size
    #     #     at_0 = curr == 0
    #     #     # print(result, direction, step, curr, mid, at_0)
    #         print(f"The dial is rotated {d}{num} to point at {curr}; during this rotation, it points at 0: {mid} times.")
    #         result += mid
    #         if at_0:
    #             result +=1
    #             if mid > 0:
    #                 result -= 1
    #     return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"([LR])(\d+)")
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        if match is None:
            continue
        data = [match.group(1), int(match.group(2))]
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
