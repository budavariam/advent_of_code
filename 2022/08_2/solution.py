""" Advent of code 2022 day 08 / 2 """

import math
from os import path
import re
from collections import defaultdict


def count_visible(DIR, sublst, original, oind):
    result = 0
    # print(f"checking {oind}.....{DIR}")
    (y, x) = oind
    maxi = original[y][x]
    for ind in sublst:
        (y, x) = ind
        value = original[y][x]
        # print(f"othertree: {value}, viewpoint: {maxi}")
        if value < maxi:
            result += 1
        if value >= maxi:
            result += 1
            # see the blocking one
            break
    # print("visible:", result)
    return result


DIR_LEFT = (0, -1)
DIR_RIGHT = (0, 1)
DIR_UP = (-1, 0)
DIR_DOWN = (1, 0)


def genlist(oind, length, direction):
    n_y, n_x = oind
    d_y, d_x = direction
    res = []
    for _ in range(length):
        n_y = n_y + d_y
        n_x = n_x + d_x
        if n_y >= 0 and n_x >= 0 and n_y < length and n_x < length:
            res.append((n_y, n_x))
        else:
            break
    return res


def calc_scenic_view_from(original, ind):
    length = len(original)

    righttoleft = genlist(ind, length, DIR_LEFT)
    lefttoright = genlist(ind, length, DIR_RIGHT)
    toptobottom = genlist(ind, length, DIR_DOWN)
    bottomtotop = genlist(ind, length, DIR_UP)

    # print(f"{ind} righttoleft", righttoleft)
    # print(f"{ind} lefttoright", lefttoright)
    # print(f"{ind} toptobottom", toptobottom)
    # print(f"{ind} bottomtotop", bottomtotop)

    a = count_visible(DIR_LEFT, righttoleft, original, ind)
    b = count_visible(DIR_RIGHT, lefttoright, original, ind)
    c = count_visible(DIR_DOWN, toptobottom, original, ind)
    d = count_visible(DIR_UP, bottomtotop, original, ind)
    result = a * b * c * d
    # print(f"result: {result} ({a},{b},{c},{d})")
    return result


def transpose(l1):
    l2 = []
    for i in range(len(l1[0])):
        row = []
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        maxi = 0

        # yy = calc_scenic_view_from(self.lines, (1,2)) # 4
        # yy = calc_scenic_view_from(self.lines, (3,2)) # 8

        for y in range(len(self.lines)):
            views = []
            for x in range(len(self.lines[0])):
                val = calc_scenic_view_from(self.lines, (y, x))
                views.append(val)
            maxi = max(maxi, max(views))
        return maxi


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = [int(x) for x in list(line)]
        processed_data.append(data)
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
