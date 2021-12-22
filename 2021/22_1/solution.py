""" Advent of code 2021 day 22 / 1 """

import math
from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        res = set()
        for what, cuboids in self.lines:
            if what == 'on':
                res = res.union(cuboids)
            elif what == 'off':
                res = res - cuboids
        return len(res)

def preprocess(raw_data):
    pattern = re.compile(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    processed_data = []
    lines = raw_data.split("\n")
    i = 0
    for line in lines:
        print(f"Parse {i} / {len(lines)} {line}")
        i +=1
        match = re.match(pattern, line)
        cuboids = set()
        xmin = max(-50, int(match.group(2)))
        ymin = max(-50, int(match.group(4)))
        zmin = max(-50, int(match.group(6)))
        xmax = min(50, int(match.group(3)))
        ymax = min(50, int(match.group(5)))
        zmax = min(50, int(match.group(7)))
        for x in range(xmin, xmax +1):
            for y in range(ymin, ymax +1):
                for z in range(zmin, zmax +1):
                    cuboids.add((x,y,z))
        data = [
            match.group(1), 
            cuboids,
        ]
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
