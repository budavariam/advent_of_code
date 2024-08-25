""" Advent of code 2023 day 04 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # pprint(self.lines)
        result = 0
        for line in self.lines:
            cnt_winning_numbers = len(line["w"].intersection(line["c"]))
            if cnt_winning_numbers > 0:
                # print(cnt_winning_numbers)
                result += 2**(cnt_winning_numbers - 1)
        return result


def parse_numbers(lst):
    return [int(x) for x in lst.split(" ") if x != ""]


@utils.profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        strip_1 = line.split(":")
        cid = strip_1[0].strip("Card ")
        winning, cards = map(parse_numbers, strip_1[1].split("|"))
        data = {"id": cid, "w": set(winning), "c": set(cards)}
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
