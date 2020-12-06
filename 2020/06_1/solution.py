""" Advent of code 2020 day 6/1 """

import math
from os import path
import re

whitespace_removal = re.compile(r'\s+')

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        return sum(map(len, self.lines))

def preprocess(raw_data):
    processed_data = [ set(whitespace_removal.sub('', group)) for group in raw_data.split("\n\n")]
    return processed_data

def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
