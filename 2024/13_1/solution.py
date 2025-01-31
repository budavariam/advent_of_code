""" Advent of code 2024 day 13 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, PULP_CBC_CMD

PRICE_A = 3
PRICE_B = 1

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        result = 0
        for i, data in enumerate(self.lines):
            problem_id = f"aoc2024_13_{i}"
            prob = LpProblem(problem_id, LpMinimize)
            a = LpVariable("a", lowBound=0, upBound=100, cat=LpInteger)
            b = LpVariable("b", lowBound=0, upBound=100, cat=LpInteger)

            x_a, y_a, x_b, y_b, x_prize, y_prize = data
            prob += x_a * a + x_b * b == x_prize
            prob += y_a * a + y_b * b == y_prize
            prob += PRICE_A * a + PRICE_B * b
            prob.solve(PULP_CBC_CMD(msg=0))
            if prob.status == 1 and a.varValue is not None and b.varValue is not None:
                result += int(3 * a.varValue + b.varValue)
                # print(f"Best solution: a={int(a.varValue)}, b={int(b.varValue)}, cost={int(3 * a.varValue + b.varValue)}")
            else:
                # print("No integer solution found inside the constrains.")
                continue
        return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r'^.*: X.(\d+), Y.(\d+)$')
    """Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400"""
    processed_data = []
    for lines in raw_data.split("\n\n"):
        data = []
        for line in lines.split("\n"):
            match = re.match(pattern, line)
            if match:
                data.extend([int(match.group(1)), int(match.group(2))])
        processed_data.append(tuple(data))
    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
