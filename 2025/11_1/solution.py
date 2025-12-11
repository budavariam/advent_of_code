""" Advent of code 2025 day 11 / 1 """

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
        pprint(self.lines)
        start = "you"
        end = "out"
        queue = [(start, [])]
        paths = []
        while queue:
            curr, pth = queue.pop()
            for nxt in self.lines[curr]:
                if nxt == end:
                    paths.append([x for x in pth] + [nxt])
                    continue
                next_item = (nxt, [x for x in pth] + [nxt])
                print(next_item)
                queue.append(next_item)
        return len(paths)


@profiler
def preprocess(raw_data):
    pattern = re.compile(r'(\w+): (.*)')
    processed_data = {}
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        if match is None:
            continue
        processed_data[match.group(1)] = match.group(2).split(" ")
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
