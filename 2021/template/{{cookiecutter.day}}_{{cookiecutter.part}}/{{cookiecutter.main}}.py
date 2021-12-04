""" Advent of code 2021 day {{cookiecutter.day}} / {{cookiecutter.part}} """

import math
from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        for line in self.lines:
            pass

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
    with(open(path.join(path.dirname(__file__), '{{cookiecutter.inputfilename}}.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
