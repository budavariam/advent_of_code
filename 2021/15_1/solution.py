""" Advent of code 2021 day 15 / 1 """

import math
from os import path
import re
import heapq as hq

import sys
from collections import deque
sys.setrecursionlimit(500000000)

pos = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    # (-1, 1), (-1, -1), (1, -1), (1, 1)
]


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.height = len(lines)
        self.width = len(lines[0])

    def fillpos(self, y, x):
        pl = []
        for (dy, dx) in pos:
            ny = dy+y
            nx = dx + x
            np = (ny, nx)
            if ny >= 0 and ny < self.height and nx >= 0 and nx < self.width:
                pl.append(np)
        return pl

    def printlines(self, msg):
        pass
        # print(msg)
        # for line in self.lines:
        #     print("".join(map(str,['+' if x>9 else x for x in line])))

    def paths(self, s, e):
        deq = [(0, s)]
        res = []

        while deq:
            [c_risk, c_pos] = hq.heappop(deq)
            if c_pos == e:
                # get last item
                print("finish with", c_risk, len(deq))
                res.append(c_risk)
            y, x = c_pos
            next_pos = self.fillpos(y, x)
            for neighbour in next_pos:
                n_y, n_x = neighbour
                if self.lines[n_y][n_x] >= 0:
                    newrisk = (c_risk + self.lines[n_y][n_x] % 9) + 1
                    hq.heappush(deq, (newrisk, neighbour))
                    self.lines[n_y][n_x] = -1
        return res

    def solve(self):
        print(self.lines)

        risks = self.paths((0, 0), (self.height-1, self.width-1))
        print(risks)
        return min(risks)


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append([int(x)-1 for x in data])
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
