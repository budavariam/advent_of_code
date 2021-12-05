""" Advent of code 2021 day 05 / 1 """

import math
from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        print(self.lines)
        dim = {}
        cnt = 0
        xa, xb, ya, yb = -1, -1, -1, -1
        for line in self.lines:
            x1, y1, x2, y2 = line
            xa, xb = sorted([x1, x2])
            ya, yb = sorted([y1, y2])
            if x1 == x2:
                # onlyhor
                print("hor", x1, y1, x2, y2, xa, xb, ya, yb)
                for i in range(ya, yb+1):
                    pos = f"{i}-{x1}"
                    if dim.get(pos) is not None:
                            dim[pos] += 1
                            
                    else:
                        dim[pos] = 1
            elif y1 == y2:
                # onlyvert
                print("vert", x1, y1, x2, y2, xa, xb, ya, yb)
                for i in range(xa, xb+1):
                    pos = f"{y1}-{i}"
                    if dim.get(pos) is not None:
                            dim[pos] += 1

                    else:
                        dim[pos] = 1
            pass
        print(dim)
        for i in dim.values():
            if i > 1:
                cnt+=1
        return cnt

def preprocess(raw_data):
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = [int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))]
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
