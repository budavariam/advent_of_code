""" Advent of code 2022 day 08 / 1 """

import math
from os import path
import re
from collections import defaultdict


def count_visible(lst, original):
    # result = 0
    print(".....")
    indices = set()
    maxi = 0
    for num, ind in enumerate(lst):
        (y,x) = ind
        value = original[y][x]
        # edge is visible!
        print(value, maxi, indices)
        if num == 0:
            indices.add(ind)
            maxi = value
            continue
        if value < maxi:
            pass
        if value > maxi:
            maxi = value
            indices.add(ind)
            # result += 1
    return indices


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
        print(self.lines)
        left = [[(y, x) for x in range(len(self.lines))] for y in range(len(self.lines))]
        right = [x[::-1] for x in left]
        bottom = transpose(left)
        top = [x[::-1] for x in bottom]
        # print(left)
        # print(right)
        # print(bottom)
        # print(top)
        count_all = set()
        for line in left:
            l = count_visible(line, self.lines)
            count_all = count_all.union(l)
        for line in right:
            l = count_visible(line, self.lines)
            count_all = count_all.union(l)
        for line in bottom:
            l = count_visible(line, self.lines)
            count_all = count_all.union(l)
        for line in top:
            l = count_visible(line, self.lines)
            count_all = count_all.union(l)
        print(count_all)
        return len(count_all)


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
