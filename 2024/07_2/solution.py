""" Advent of code 2024 day 07 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler

from itertools import product


class Code:
    def __init__(self, lines):
        self.lines = lines

    def evaluate_expression(self, nums, ops):
        result = nums[0]
        for i, op in enumerate(ops):
            if op == "*":
                result *= nums[i + 1]
            elif op == "+":
                result += nums[i + 1]
            elif op == "||":
                result = int(f"{result}{nums[i + 1]}")
        return result

    def find_solution(self, res, nums):
        operators = ["*", "+", "||"]
        for ops_config in product(operators, repeat=len(nums) - 1):
            if self.evaluate_expression(nums, ops_config) == res:
                return res

        return 0

    def solve(self):
        result = 0
        for res, nums in self.lines:
            result += self.find_solution(res, nums)
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line.split(": ")
        nums = data[1].split(" ")
        processed_data.append((int(data[0]), [int(x) for x in nums]))
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
