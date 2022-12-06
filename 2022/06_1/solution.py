""" Advent of code 2022 day 06 / 1 """

import math
from os import path
import re
from collections import deque


class Code(object):
    def __init__(self, lines):
        self.lines = lines[0]

    def solve(self):
        print(self.lines)
        result = 0
        last4= deque(self.lines[0:4])
        for i, char in enumerate(self.lines[4:]):
            # print(last4, char, i, i+4)
            if len(set(last4)) == 4:
                return i+4
            else:
                last4.popleft()
                last4.append(char)
        return result


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append(data)
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
