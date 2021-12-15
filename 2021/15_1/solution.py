""" Advent of code 2021 day 15 / 1 """

import math
from os import path
import re

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
        self.globalmin = 0 #self.height * 4 * 9 + self.width * 4 * 9

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

    def paths(self, s, e, visited):
        deq = deque([(s, visited, 0)])
        res = deque([])
        i = 0

        for u in range(self.height):
            for v in range(self.width):
                if u == v:
                    self.globalmin += self.lines[u][v]
                    self.globalmin += self.lines[u][v-1]
        print("heuristic",  self.globalmin)
        self.globalmin = 774
        while len(deq) > 0:
            i+=1
            if (i % 30000 == 0):
                print("chk", c_pos, c_risk, self.globalmin, len(c_visited), len(deq))
            [c_pos, c_visited, c_risk] = deq.pop()
            if c_pos in c_visited or c_risk > self.globalmin:
                continue
            if c_pos == e:
                # get last item
                print("finish with", c_risk, self.globalmin, len(c_visited), len(deq))
                self.globalmin = min(c_risk, self.globalmin)
                res.append(c_risk)
            y, x = c_pos
            next_pos = self.fillpos(y,x)
            heu = []
            for neighbour in next_pos:
                if neighbour not in c_visited:
                    n_vis = c_visited.copy().union(set([c_pos]))
                    newrisk = c_risk + self.lines[neighbour[0]][neighbour[1]]
                    if newrisk < self.globalmin:
                        heu.append((neighbour, n_vis, newrisk))
            heu = sorted(heu, key=lambda tup: tup[0][0] + tup[0][1])
            if len(heu) > 0:
                a = heu.pop()
                deq.append(a) # add most end near to the top
            heu2 = sorted(heu, key=lambda tup: tup[2], reverse=True)
            if len(heu2) > 0:
                deq.append(heu2[0]) # add smallest rank top to the start
            if len(heu2) > 1:
                for d in heu[1:]:
                    deq.appendleft(d) # add lowest top to the end
        return list(res)

    def solve(self):
        print(self.lines)
        
        risks = self.paths((0,0), (self.height-1, self.width-1), set())
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
