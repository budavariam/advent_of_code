""" Advent of code 2020 day 15/2 """

import math
from os import path


class Code(object):
    def __init__(self, starting_numbers, stop):
        self.starting_numbers = starting_numbers
        self.memory = {}
        self.stop = stop

    def solve(self):
        self.memory[self.starting_numbers[0]] = 1
        prev_spoken = None
        for order_index, num in enumerate(self.starting_numbers):
            self.memory[prev_spoken] = order_index
            prev_spoken = num
        for index in range(1 + len(self.starting_numbers), self.stop + 1):
            prev_occurrance = self.memory.get(prev_spoken)
            # keep the info that it was spoken in the last turn
            self.memory[prev_spoken] = index - 1
            if prev_occurrance is None:
                prev_spoken = 0
            else:
                prev_turn_index = index - 1
                prev_spoken = prev_turn_index - prev_occurrance
            if index % 1000000 == 0:
                print(f"Turn {index}, Say: {prev_spoken}")
        return prev_spoken


def preprocess(raw_data):
    processed_data = list(map(int, raw_data.split(",")))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines, 30000000)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
