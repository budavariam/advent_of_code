""" Advent of code 2023 day 08 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import deque
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        steps = 0
        curr = "AAA"
        movement = deque(self.lines["movement"])
        while curr != "ZZZ":
            if len(movement) == 0:
                movement = deque(self.lines["movement"])
            direction = movement.popleft()
            curr = self.lines["nodes"][curr][0 if direction == "L" else 1]
            steps += 1
        return steps


@utils.profiler
def preprocess(raw_data):
    "AAA = (BBB, CCC)"
    pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    lines = raw_data.split("\n")
    movement = lines[0]
    nodes = {}
    processed_data = {"movement": movement, "nodes": nodes}
    for line in lines[2:]:
        match = re.match(pattern, line)
        processed_data["nodes"][match.group(1)] = (match.group(2), match.group(3))
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
