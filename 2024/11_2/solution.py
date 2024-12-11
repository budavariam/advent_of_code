""" Advent of code 2024 day 11 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from functools import cache
from utils import log, profiler


class Code(object):
    @cache
    def rule(self, num: int) -> tuple[int, ...]:
        if num == 0:
            return (1,)

        num_s = str(num)
        num_len = len(num_s)
        if num_len % 2 == 0:
            return (int(num_s[: num_len // 2]), int(num_s[num_len // 2 :]))
        return (num * 2024,)

    @cache
    def solve(self, numbers: tuple[int, ...], times: int) -> int:
        if times == 0:
            return len(numbers)

        return sum(self.solve(self.rule(n), times - 1) for n in numbers)


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = tuple(map(int, raw_data.split(" ")))
    return processed_data


@profiler
def solution(data, times=75):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code()
    return solver.solve(lines, times)


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
