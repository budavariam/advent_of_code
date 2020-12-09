""" Advent of code 2020 day 09/1 """

import math
from os import path


class Code(object):
    def __init__(self, preamble, lines):
        self.lines = lines
        self.preamble = preamble

    def calc_combinations(self, items):
        return {items[i] + items[j]: True for i in range(len(items)) for j in range(i+1, len(items))}

    def solve(self):
        index = self.preamble
        for item in self.lines[self.preamble:]:
            possible_values = self.calc_combinations(
                [x for x in self.lines[index - self.preamble:index]])
            index += 1
            if item not in possible_values:
                return item
        return None


def preprocess(raw_data):
    processed_data = list(map(int, raw_data.split("\n")))
    return processed_data


def solution(preamble, data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(preamble, lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(25, input_file.read()))
