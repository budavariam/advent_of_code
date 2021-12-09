""" Advent of code 2021 day 09 / 1 """

import math
from os import path
import re

pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        rl = 0
        height = len(self.lines)
        width = len(self.lines[0])
        for y, row in enumerate(self.lines):
            for x, c in enumerate(row):
                # print(c)
                shouldadd = []*len(pos)
                for (dy, dx) in pos:
                    ny = dy+y
                    nx = dx + x
                    if ny >= 0 and ny < height and nx >= 0 and nx < width:
                        shouldadd.append(self.lines[ny][nx] > c)
                if all(shouldadd):
                    print(c)
                    rl += c+1
        return rl


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append(list(map(int, data)))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
