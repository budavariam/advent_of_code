""" Advent of code 2021 day 20 / 1 """

import math
from os import path
import re
from collections import defaultdict


class Code(object):
    def __init__(self, data):
        self.data = data

    def calcpos(self, y,x,algo, grid):
        num = ""
        for d_y in [-1,0,1]: 
            for d_x in [-1,0,1]:
                num += str(grid[(y+d_y,x+d_x)])
        if len(num) != 9:
            raise(Exception("offbyone"))
        pos = int(num, base=2)
        return algo[pos]

    def calclight(self, grid):
        return list(grid.values()).count(1)

    def solve(self):
        # print(self.data)
        algo, grid, dims = self.data
        print(dims, self.calclight(grid))
        for i in range(2):
            newg = defaultdict(lambda: i % 2) # blink adjust
            dims["miny"] -= 1 
            dims["minx"] -= 1 
            dims["maxy"] += 1 
            dims["maxx"] += 1 
            for y in range(dims["miny"], dims["maxy"]+1):
                line = ""
                for x in range(dims["minx"], dims["maxx"]+1):
                    n_v = self.calcpos(y,x, algo, grid)
                    newg[(y,x)] = n_v
                    line += "#" if n_v == 1 else "."

                print(line)
            grid = newg
            print(dims, self.calclight(grid))
        return self.calclight(grid)


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    algo = []
    grid = defaultdict(int)
    for y, line in enumerate(raw_data.split("\n")):
        if y == 0:
            algo = [1 if x == '#' else 0 for x in line]
        if y > 1:
            for x, c in enumerate(line):
                grid[(y-2, x)] = 1 if c == '#' else 0
    dims = {
        "minx": 0,
        "miny": 0,
        "maxx": x,
        "maxy": y-2,
    }

    return [algo, grid, dims]


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
