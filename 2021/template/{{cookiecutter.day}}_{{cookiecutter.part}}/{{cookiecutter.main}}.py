""" Advent of code 2021 day {{cookiecutter.day}}/{{cookiecutter.part}} """

import math
from os import path


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pass


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), '{{cookiecutter.inputfilename}}.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
