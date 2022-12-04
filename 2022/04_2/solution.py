""" Advent of code 2022 day 04 / 2 """

from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        res = 0
        for a0, a1, b0, b1 in self.lines:
            rng1 = set(range(a0, a1 + 1))
            rng2 = set(range(b0, b1 + 1))
            ins = rng1.intersection(rng2)
            if len(ins) > 0:
                res += 1
        return res


def preprocess(raw_data):
    pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = [
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3)),
            int(match.group(4)),
        ]
        # data = line
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
