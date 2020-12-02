""" Advent of code 2020 day 1/2 """

import math
from os import path


def solution(data):
    """ Solution to the problem """
    lines = list(map(int, data.split("\n")))
    precalculate = {}
    for a in lines:
        for b in lines:
            if (a != b) and (a+b <= 2020):
                # NOTE: I assume that all input numbers are unique
                precalculate[2020 - (a + b)] = a * b

    for value in lines:
        inverseMultiplied = precalculate.get(value)
        if inverseMultiplied is not None:
            return value * inverseMultiplied
    return None


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
