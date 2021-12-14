""" Advent of code 2021 day 14 / 2 """

from os import path
import re
from collections import defaultdict


class Code(object):
    def __init__(self, lines):
        self.str = lines[0]
        self._curr = [a+b for [a, b] in zip(lines[0], lines[0][1:])]
        self.rules = {k: v for [k, v] in lines[1]}
        self.current = {k: self._curr.count(k) for k in self.rules.keys()}

    def step(self, c):
        newf = defaultdict(int)
        for [combo, occurrancenum] in c.items():
            newf[self.rules[combo][0]] += occurrancenum
            newf[self.rules[combo][1]] += occurrancenum
        return newf

    def result(self):
        pfreq = defaultdict(int)
        for [k, v] in self.current.items():
            pfreq[k[0]] += v
        pfreq[self.str[-1]] += 1  # last stays the same

        leastf = min(pfreq.values())
        mostf = max(pfreq.values())

        return mostf - leastf

    def solve(self):
        print(self.str)
        for _ in range(40):
            self.current = self.step(self.current)
        return self.result()


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
