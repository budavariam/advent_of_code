""" Advent of code 2020 day 10/2 """

import math
from os import path
from functools import reduce


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def calc_jolt_connections(self, lines):
        result = {}
        for i, item in enumerate(lines):
            connections = []
            for nextitem in lines[i+1:i+1+3]: 
                # assume that the input is ordered, and there are no duplicates, the possible values are at most in the +3rd index
                diff = nextitem - item
                if diff <= 3: 
                    # data can be connected to the jolts up to +3 output, if it applies, add the current item to the possibilities
                    connections.append(nextitem)
            result[item] = connections
        return result

    def solve(self):
        start_jolt = 0
        lines_plus_jolt = [start_jolt, *self.lines]
        num_variations = self.calc_jolt_connections(lines_plus_jolt)
        
        cached_values = {}
        for item in reversed(lines_plus_jolt):
            # calculate possible combinations from the end
            next_items = num_variations[item]
            var_cnt = 1 if len(next_items) == 0 else sum([cached_values.get(x) for x in next_items])
            cached_values[item] = var_cnt
        return cached_values[start_jolt]


def preprocess(raw_data):
    processed_data = sorted(map(int, raw_data.split("\n")))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
