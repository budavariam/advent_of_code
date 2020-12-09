""" Advent of code 2020 day 09/2 """

import math
from os import path


class Code(object):
    def __init__(self, preamble, lines):
        self.lines = lines
        self.preamble = preamble

    def find_contiguous_range_minmax(self, desiredsum):
        for i, item in enumerate(self.lines):
            summary_from_i = item
            rangemin = item
            rangemax = item
            for other_item in self.lines[i+1:]:
                summary_from_i += other_item
                if other_item < rangemin:
                    rangemin = other_item
                elif other_item > rangemax:
                    rangemax = other_item

                if summary_from_i == desiredsum:
                    return (rangemin, rangemax)
                if summary_from_i > desiredsum:
                    continue

    def calc_combinations(self, items):
        return {items[i] + items[j]: True for i in range(len(items)) for j in range(i+1, len(items))}

    def find_error_num(self):
        index = self.preamble
        for item in self.lines[self.preamble:]:
            possible_values = self.calc_combinations(
                [x for x in self.lines[index - self.preamble:index]])
            index += 1
            if item not in possible_values:
                return item
        return None

    def solve(self):
        errnum = self.find_error_num()
        if errnum is None:
            return None
        rangemin, rangemax = self.find_contiguous_range_minmax(errnum)
        return rangemin + rangemax

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
