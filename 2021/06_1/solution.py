""" Advent of code 2021 day 06 / 1 """

import math
from os import path
import re

class LanternFish(object):
    def __init__(self, inittimer, isNew = False):
        self.i = inittimer
        self.curr = inittimer
        self.isNew = isNew
    def __repr__(self) -> str:
        return f"{self.curr} ({self.i})"
    def reset(self):
        self.isNew = False
        self.curr = 6

    def age(self):
        hasCreated = False
        if (self.isNew):
            self.isNew = False
            return (hasCreated, self.curr)
        self.curr -= 1
        if self.curr < 0:
            self.reset()
            hasCreated = True
        return (hasCreated, self.curr)

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        fishes = self.lines
        # print(fishes)
        for i in range(80):
            print(i)
            for f in fishes:
                a = f.age()
                if a[0]:
                    fishes.append(LanternFish(8, True))
            # print(fishes)

        return len(fishes)

def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        processed_data = list(map(LanternFish, map(int,line.split(","))))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
