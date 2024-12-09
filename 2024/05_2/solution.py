""" Advent of code 2024 day 05 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
from functools import cmp_to_key


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # pprint(self.lines)
        rules = self.lines["rules"]
        updates = self.lines["updates"]
        key = cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))
        result = 0
        for line in updates:
            s = sorted(line, key=key)
            if line != s:
                result += s[len(s) // 2]
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    d = raw_data.split("\n\n")
    processed_data = {
        "rules": set([]),
        "updates": [],
    }
    for line in d[0].split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        before, after = line.split("|")
        processed_data["rules"].add((int(before), int(after)))
    for line in d[1].split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = list(map(int, line.split(",")))
        processed_data["updates"].append(data)
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
