""" Advent of code 2020 day 1/1 """

import math
from os import path


def solution(data):
    """ Solution to the problem """
    lines = data.split("\n")
    precalculate = dict()
    for line_value_str in lines:
        precalculate[2020 - int(line_value_str)] = True

    for line_value_str in lines:
        current_value = int(line_value_str)
        inverse = 2020 - current_value
        if (precalculate.get(current_value) == True):
            return current_value * inverse
    return None


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
