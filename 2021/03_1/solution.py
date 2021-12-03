""" Advent of code 2021 day 03/1 """

import math
from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        print(self.lines)
        gamma = ""  # most common
        epsilon = ""  # least common
        bits = [[0, 0] for x in range(12)]
        for line in self.lines:
            for num, bit in enumerate(line):
                bits[num][int(bit)] += 1 
        for [zero, one] in bits:
            if zero > one:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        g = int(gamma, base=2)
        e = int(epsilon, base=2)
        pow = g * e
        return pow


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
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
