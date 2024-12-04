""" Advent of code 2023 day {{cookiecutter.day}} / {{cookiecutter.part}} """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        result = 0
        for line in self.lines:
            pass
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = list(line)
        processed_data.append(data)
    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "{{cookiecutter.inputfilename}}.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
