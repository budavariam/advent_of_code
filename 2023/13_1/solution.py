""" Advent of code 2023 day 13 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def process_v1(self, index, d):
        data = d[index]
        height = data.get("height")
        found = False
        found_i = 0
        res = 0
        for i in range(1, height):
            if data["matrix"][i] == data["matrix"][i - 1]:
                print(f"{index}: Found match between {i-1}-{i} out of {height}")
                found = True

                lower_dist = i - 1
                upper_dist = height - i - 1
                found_i = i

                if lower_dist > upper_dist:
                    # midpoint is over the half
                    if data["matrix"][-1] == data["matrix"][i - 1 - upper_dist]:
                        continue
                    else:
                        return 0
                elif lower_dist < upper_dist:
                    # midpoint is before the half
                    if data["matrix"][0] == data["matrix"][i + lower_dist]:
                        continue
                    else:
                        return 0
                else:
                    if data["matrix"][0] == data["matrix"][-1]:
                        continue
                    else:
                        return 0

        if found:
            if index == 0:
                res = found_i * 100
            else:
                res = found_i
        return res

    def process(self, index, d):
        data = d[index]
        height = data.get("height")
        found_index = -1
        for i in range(1, height):
            low = i - 1
            high = i
            interval = (low, high)
            is_reflecting = False
            while low >= 0 and high < height:
                if data["matrix"][low] == data["matrix"][high]:
                    is_reflecting = True
                    interval = (low, high)
                    low -= 1
                    high += 1
                else:
                    is_reflecting = False
                    break
            if is_reflecting:
                found_index = i
                # print(f"{found_index} at {interval[0]}-{interval[1]} in {0}-{height-1}")
        if found_index >= 0:
            return found_index * 100 if index == 0 else found_index
        return 0

    def solve(self):
        # pprint(self.lines)
        result = 0
        for i, line in enumerate(self.lines):
            # print(i)
            # print("processing... A")
            result += self.process(0, line)
            # print("processing... B")
            result += self.process(1, line)
        return result


@utils.profiler
def preprocess(raw_data):
    processed_data = []
    for matrix in raw_data.split("\n\n"):
        raw = matrix.rstrip("\n").split("\n")
        vertical = [tuple(line) for line in raw]
        horizontal = list(zip(*(raw)))
        data = [
            {"matrix": vertical, "width": len(vertical[0]), "height": len(vertical)},
            {
                "matrix": horizontal,
                "width": len(horizontal[0]),
                "height": len(horizontal),
            },
        ]
        # pprint(vertical)
        # pprint(horizontal)

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
