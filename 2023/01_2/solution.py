""" Advent of code 2023 day 01 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numrev = [n[::-1] for n in num]

def findnum(txt, values, ptrn):
    # ptrn = f"({'|'.join(map(str,range(0,10)))}|{'|'.join(pattern)})"
    grp = re.search(ptrn, txt)
    print(grp)
    if grp is not None:
        raw = grp.group(1)
        if len(raw) == 1:
            return int(raw)
        else:
            return values.index(grp.group(1)) + 1
    print(f"ERROR IN PATTERN {txt} {ptrn}")
    return -1

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        result = 0
        for line in self.lines:
            n1 = findnum(line, num, r"(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)")
            n2 = findnum(line[::-1], numrev, r"(0|1|2|3|4|5|6|7|8|9|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)")

            result += int(f"{n1}{n2}")
        return result


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read()))
