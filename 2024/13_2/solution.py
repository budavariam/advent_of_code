""" Advent of code 2024 day 13 / 2 """

from os import path
import re
from utils import profiler

PRICE_A = 3
PRICE_B = 1
OFFSET = 10000000000000

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def mincost(self, x_a, y_a, x_b, y_b, x_prize, y_prize):
        # based on u/zniperr, we have to find the intersection of two lines
        b, b_remainder = divmod(y_a * x_prize - x_a * y_prize, y_a * x_b - x_a * y_b)
        a, a_remainder = divmod(x_prize - b * x_b, x_a)
        if a_remainder != 0 or b_remainder != 0:
            # non-integer solution is not valid in this case
            return 0
        return a * PRICE_A + b * PRICE_B

    def solve(self):
        result = 0
        for data in self.lines:
            x_a, y_a, x_b, y_b, x_prize, y_prize = data        
            result += self.mincost(x_a, y_a, x_b, y_b, OFFSET + x_prize, OFFSET + y_prize)
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
