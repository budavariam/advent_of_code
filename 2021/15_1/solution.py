""" Advent of code 2021 day 15 / 1 """

import math
from os import path
import re

import sys
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
        self.globalmin = 99999999

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

    def paths(self, s, e, visited, risk):
        if s in visited or risk > self.globalmin:
            return
        if s == e:
            # get last item
            print("finish with", risk, self.globalmin, len(visited))
            self.globalmin = min(risk, self.globalmin)
            yield risk
        y, x = s
        next_pos = self.fillpos(y,x)
        # print(s, e,len(visited), next_pos)

        for neighbour in next_pos:
            if neighbour not in visited:
                n_vis = visited.copy().union(set([s]))
                newrisk = risk + self.lines[neighbour[0]][neighbour[1]]
                yield from self.paths(neighbour, e, n_vis, newrisk)
        return

    def solve(self):
        return self.paths('start', 'end', set(), False)

    def solve(self):
        print(self.lines)
        
        risks = [x for x in self.paths((0,0), (self.height-1, self.width-1), set(), 0)]
        print(risks)
        return min(risks)


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append([int(x) for x in data])
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
