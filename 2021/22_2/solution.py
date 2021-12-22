""" Advent of code 2021 day 22 / 2 """

import math
from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def count(self, states):
        res = 0
        for flip, ((xmin, xmax), (ymin, ymax), (zmin, zmax)) in states:
            res += math.prod([
                flip,
                abs(xmax-xmin+1),
                abs(ymax-ymin+1),
                abs(zmax-zmin+1)
            ])
        return res

    def solve(self):
        # print(self.lines)
        res = []
        for what, (xmin, xmax), (ymin, ymax), (zmin, zmax) in self.lines:
            new_cuboids = []
            for flip, ((x_prev_min, x_prev_max), (y_prev_min, y_prev_max), (z_prev_min, z_prev_max)) in res:
                # find the common parts
                if (not any([
                    x_prev_max < xmin,
                    xmax < x_prev_min,
                    y_prev_max < ymin,
                    ymax < y_prev_min,
                    z_prev_max < zmin,
                    zmax < z_prev_min
                ])):
                    # extract the common parts
                    common_xmin = max(xmin, x_prev_min)
                    common_xmax = min(xmax, x_prev_max)
                    common_ymin = max(ymin, y_prev_min)
                    common_ymax = min(ymax, y_prev_max)
                    common_zmin = max(zmin, z_prev_min)
                    common_zmax = min(zmax, z_prev_max)
                    # flip common parts
                    new_cuboids.append((-1*flip, (
                        (common_xmin, common_xmax),
                        (common_ymin, common_ymax),
                        (common_zmin, common_zmax),
                    )))
            if what == 'on':
                res.append((1, ((xmin, xmax), (ymin, ymax), (zmin, zmax))))
            for cb in new_cuboids:
                res.append(cb)
        return self.count(res)


def preprocess(raw_data):
    pattern = re.compile(
        r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    processed_data = []
    lines = raw_data.split("\n")
    i = 0
    for line in lines:
        i += 1
        print(f"Parse {i} / {len(lines)} {line}")
        match = re.match(pattern, line)
        xmin = int(match.group(2))
        xmax = int(match.group(3))
        ymin = int(match.group(4))
        ymax = int(match.group(5))
        zmin = int(match.group(6))
        zmax = int(match.group(7))
        data = [
            match.group(1),
            (xmin, xmax),
            (ymin, ymax),
            (zmin, zmax),
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
