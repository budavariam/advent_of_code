""" Advent of code 2021 day 08 / 1 """

import math
from os import path
import re

seg_nums = {
    # 0:
    1: sum([0, 0, 1, 0, 0, 1, 0]),
    # 2:
    # 3:
    4: sum([0, 1, 1, 1, 0, 1, 0]),
    # 5:
    # 6:
    7: sum([1, 0, 1, 0, 0, 1, 0]),
    8: sum([1, 1, 1, 1, 1, 1, 1]),
     # 9:
}
chars= 'abcdefg'


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        print(self.lines, seg_nums)
        s = 0
        for [line, a] in self.lines:
            lens = [len(x) for x in a.split(" ")]
            a = [x for x in lens if x in [2,4,3,7]]
            s += len(a)
        return s
            # for x in 



def preprocess(raw_data):
    # pattern = re.compile(r'([a-z ]+) ([a-z ]+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = [x.strip() for x in line.split("|") if x != '']
        # print(data)
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
