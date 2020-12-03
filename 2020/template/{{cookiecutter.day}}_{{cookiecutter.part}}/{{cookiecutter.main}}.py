""" Advent of code 2020 day {{cookiecutter.day}}/{{cookiecutter.part}} """

import math
from os import path


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pass


def solution(data):
    """ Solution to the problem """
    lines = data.split("\n")
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), '{{cookiecutter.inputfilename}}.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
