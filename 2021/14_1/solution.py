""" Advent of code 2021 day 14 / 1 """

import math
from os import path
import re
from collections import Counter, defaultdict


class Code(object):
    def __init__(self, lines):
        self.str = lines[0]
        self.curr = [a+b for [a, b] in zip(lines[0], lines[0][1:])]
        self.d = lines[1]
        self.rules = {k: v for [k, v] in lines[1]}
        self.c = {k: self.curr.count(k) for k in self.rules.keys()}
        pass

    def calcres(self):
        pfreq = defaultdict(int)
        for [k, v] in self.c.items():
            pfreq[k[0]] += v
        pfreq[self.str[-1]] += 1  # last stays the same

        leastf = min(pfreq.values())
        mostf = max(pfreq.values())

        return mostf - leastf

    def solve(self):
        print(self.str)
        for i in range(10):
            newf = defaultdict(int)
            for [k, res] in self.c.items():
                newf[self.rules[k][0]] += res
                newf[self.rules[k][1]] += res
            self.c = newf
        return self.calcres()


def preprocess(raw_data):
    pattern = re.compile(r'(\w)(\w) -> (\w+)')
    processed_data = ["", []]
    for i, line in enumerate(raw_data.split("\n")):
        if i == 0:
            processed_data[0] = line
            continue
        if line == "":
            continue
        match = re.match(pattern, line)
        a = match.group(1)
        b = match.group(2)
        c = match.group(3)

        data = [
            a+b,
            [a+c, c+b]
            # a,
            # b,
            # c
        ]
        processed_data[1].append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
