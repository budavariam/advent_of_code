""" Advent of code 2024 day 07 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def find_solution(self, res, nums):
        operators = ["*", "+"]
        queue = [(nums[0], o, 0) for o in operators]
        while queue:
            curr_result, op, i = queue.pop()
            next_result = 0
            if op == "*":
                next_result = curr_result * nums[i + 1]
            elif op == "+":
                next_result = curr_result + nums[i + 1]
            else:
                print("ERROR", op)

            if next_result > res:
                continue
            elif next_result == res:
                return res
            else:
                if i + 2 >= len(nums):
                    continue

                for o in operators:
                    queue.append((next_result, o, i + 1))
        return 0

    def solve(self):
        # pprint(self.lines)
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
