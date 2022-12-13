""" Advent of code 2022 day 13 / 1 """

import math
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def cmp(self, a,b):
        print(f"Comparing: {a} - {b}")
        if isinstance(a, int) and isinstance(b, int):
            """
            If both values are integers, the lower integer should come first.
            If the left integer is lower than the right integer, the inputs are in the right order.
            If the left integer is higher than the right integer, the inputs are not in the right order.
            Otherwise, the inputs are the same integer; continue checking the next part of the input.
            """
            val_a = a
            val_b = b
            # lower = min(val_a, val_b)
            if val_a < val_b:
                print(f"{val_a} < {val_b}")
                return True
                # continue # ???
                # return True # ???
            elif val_a > val_b:
                print(f"{val_b} < {val_a}")
                return False
            else:
                print(f"{val_a} == {val_b}")
                return None
        if isinstance(a, list) and isinstance(b, int):
            """
            If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
            """
            b = [b]
        if isinstance(a, int) and isinstance(b, list):
            a = [a]
        if isinstance(a, list) and isinstance(b, list):
            """
            If both values are lists, compare the first value of each list, then the second value, and so on.
            If the left list runs out of items first, the inputs are in the right order.
            If the right list runs out of items first, the inputs are not in the right order.
            If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
            """
            for a_part, b_part in zip(a,b):
                res = self.cmp(a_part,b_part)
                if res is not None:
                    return res
            if len(a) < len(b):
                return True
            if len(a) > len(b):
                return False
            if len(a) == len(b):
                return None
        return None

    def cnt(self, line):
        res = 0
        for x in line:
            if isinstance(x, list):
                return self.cnt(x)
            else:
                res += x
        return res

    def solve(self):
        print(self.lines)
        result = 0
        for i, (line_a, line_b) in enumerate(self.lines):
            print(f"{i}___")
            cmp_res = self.cmp(line_a,line_b)
            print(cmp_res)
            if cmp_res:
                # result += self.cnt(line_a)
                # result += self.cnt(line_b)
                result += i+1
        return result

@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append([eval(x) for x in data.split("\n")])
    return processed_data

@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
