""" Advent of code 2022 day 10 / 1 """

import math
from os import path
import re
from collections import defaultdict

NOOP = "NOOP"
ADDX = "ADDX"

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        print(self.lines)
        reg_x = 1
        cycle_number = 1
        timeline_x = []
        timeline_during = []
        timeline = []
        res_indices = [20, 60, 100, 140, 180, 220]
        signal_strength = 0
        for i, line_value in enumerate(self.lines):
            line = line_value[0]
            if line == NOOP:
                timeline_during.append(signal_strength)
                signal_strength = reg_x * cycle_number
                timeline.append(signal_strength)
                timeline_x.append(reg_x)
                print(cycle_number, NOOP, reg_x, signal_strength, line_value, i)
                cycle_number += 1
            if line == ADDX:
                x_val = line_value[1]
                signal_strength = reg_x * cycle_number
                print(cycle_number, ADDX, reg_x, signal_strength, line_value, i)
                timeline.append(signal_strength)
                timeline_x.append(reg_x)
                timeline_during.append(signal_strength)
                cycle_number += 1
                
                signal_strength = reg_x * cycle_number
                print(cycle_number, ADDX, reg_x, signal_strength, line_value, i)
                timeline_during.append(signal_strength)
                print(cycle_number, ADDX, reg_x, signal_strength, i)
                timeline.append(signal_strength)
                timeline_x.append(reg_x)
                cycle_number += 1
                reg_x += x_val
        print(len(timeline))
        print([timeline_x[x-1] for x in res_indices])
        print([timeline_during[x-1] for x in res_indices])
        res = sum([timeline_x[x-1] * x for x in res_indices])
        return res


def preprocess(raw_data):
    pattern = re.compile(r'addx (-?\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        if line == "noop":
            processed_data.append((NOOP, 1))
        else:
            match = re.match(pattern, line)
            processed_data.append((ADDX, int(match.group(1))))
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
