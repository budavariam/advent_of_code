""" Advent of code 2021 day 05 / 2 """

import math
from os import path
import re
from collections import Counter


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def printmap(self, dim, minx, miny, maxx, maxy):
        for i in range(miny, maxy + 1):
            ln = ""
            for j in range(minx, maxx+1):
                pos = f"{i}-{j}"
                ln += str(dim.get(pos)) if dim.get(pos) is not None else '.'
            print(ln)
        print(dim)

    def solve(self):
        # print(self.lines)
        minx, miny, maxx, maxy = 0, 0, 0, 0
        dim = {}
        cnt = 0
        xa, xb, ya, yb = -1, -1, -1, -1
        for line in self.lines:
            x1, y1, x2, y2 = line
            xa, xb = sorted([x1, x2])
            ya, yb = sorted([y1, y2])
            minx = min(minx, xa)
            miny = min(miny, ya)
            maxx = max(maxx, xb)
            maxy = max(maxy, yb)
            if x1 == x2:
                # print("hor", y1, x1, y2, x2, ya, xa, yb, xb)
                for i in range(ya, yb+1):
                    pos = f"{i}-{x1}"
                    if dim.get(pos) is not None:
                        dim[pos] += 1

                    else:
                        dim[pos] = 1
            elif y1 == y2:
                # print("vert", y1, x1, y2, x2, ya, xa, yb, xb)
                for i in range(xa, xb+1):
                    pos = f"{y1}-{i}"
                    if dim.get(pos) is not None:
                        dim[pos] += 1

                    else:
                        dim[pos] = 1
            else:
                # print("diag", y1, x1, y2, x2, ya, xa, yb, xb)
                if x1 < x2:
                    for i, x in enumerate(range(x1, x2+1)):
                        if y1 < y2:
                            pos = f"{y1+i}-{x}"
                        else:
                            pos = f"{y1-i}-{x}"
                        if dim.get(pos) is not None:
                            dim[pos] += 1
                        else:
                            dim[pos] = 1
                else:
                    for i, x in enumerate(range(x2, x1+1)):
                        if y1 < y2:
                            pos = f"{y2-i}-{x}"
                        else:
                            pos = f"{y2+i}-{x}"
                        if dim.get(pos) is not None:
                            dim[pos] += 1
                        else:
                            dim[pos] = 1
        # self.printmap(dim, minx, miny, maxx, maxy)
        
        for i in dim.values():
            if i > 1:
                cnt += 1
        return cnt


def preprocess(raw_data):
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = [int(match.group(1)), int(match.group(2)),
                int(match.group(3)), int(match.group(4))]
        # data = line
        processed_data.append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
