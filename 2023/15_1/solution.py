""" Advent of code 2023 day 15 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def hash_alg(self, text):
        """Determine the ASCII code for the current character of the string.
        Increase the current value by the ASCII code you just determined.
        Set the current value to itself multiplied by 17.
        Set the current value to the remainder of dividing itself by 256."""
        curr = 0
        for c in text:
            curr += ord(c)
            curr *= 17
            curr %= 256
        return curr

    def solve(self):
        pprint(self.lines)
        result = 0
        for line in self.lines:
            result += self.hash_alg(line)
        return result


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for data in raw_data.split(","):
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
