""" Advent of code 2024 day 23 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
from itertools import combinations


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # pprint(self.lines)
        result = 0
        computer_names = self.lines.keys()
        computer_names_with_t = set([n for n in computer_names if n.startswith("t")])
        connections = self.lines

        all_combos = combinations(computer_names, r=3)
        # print(list(all_combos))
        for a, b, c in all_combos:
            has_a = b in connections[a] and c in connections[b]
            has_b = c in connections[b] and a in connections[b]
            has_c = a in connections[c] and b in connections[c]
            if (
                has_a
                and has_b
                and has_c
                and any([x in computer_names_with_t for x in [a, b, c]])
            ):
                result += 1
        return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\w+)-(\w+)")
    processed_data = defaultdict(set)
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        c1, c2 = [match.group(1), match.group(2)]
        # data = list(line)
        processed_data[c1].add(c2)
        processed_data[c2].add(c1)
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
