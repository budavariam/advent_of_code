""" Advent of code 2022 day 15 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

FOUR_NEIGHBORS = set([(0, 1), (1, 0), (0, -1), (-1, 0)])

def mergeIntervals(intervals):
    """ https://www.geeksforgeeks.org/merging-intervals/ """
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval, if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    return stack
 
    # print("The Merged Intervals are :", end=" ")
    # for i in range(len(stack)):
    #     print(stack[i], end=" ")

def interval_in_x(line, y):
    dst = abs(y - line.get("s_y"))
    minx = line.get("s_min_x") + dst
    maxx = line.get("s_max_x") - dst
    if minx > line.get("s_x") and maxx < line.get("s_x"):
        return None
    return [minx, maxx]

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def find(self, find_y):
        result = []
        for line in self.lines:
            iv = interval_in_x(line, find_y)
            if iv is not None:
                result.append(iv)
        res = mergeIntervals(result)
        return res

    def solve(self, max_y):
        # pprint(self.lines)
        multiplier = 4000000
        for y in range(0, max_y + 1):
            res = self.find(y)
            if len(res) > 1:
                x = res[0][1] + 1
                print(y, res, max_y)
                break
        return x * multiplier + y

@utils.profiler
def preprocess(raw_data):
    # example: "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
    pattern = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        s_x = int(match.group(1))
        s_y = int(match.group(2))
        b_x = int(match.group(3))
        b_y = int(match.group(4))
        dist = abs(s_y - b_y) + abs(s_x - b_x)
        data = {
            # sensor
            "s_x": s_x,
            "s_min_x": s_x - dist,
            "s_max_x": s_x + dist,
            "s_y": s_y,
            "s_min_y": s_y - dist,
            "s_max_y": s_y + dist,
            # beacon
            "b_x": b_x,
            "b_min_x": b_x - dist,
            "b_max_x": b_x + dist,
            "b_y": b_y,
            "b_min_y": b_y - dist,
            "b_max_y": b_y + dist,
            "dist": dist,
        }
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data, y):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve(y)


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read(), 4000000))
