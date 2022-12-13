""" Advent of code 2022 day 13 / 2 """

import math
from os import path
import re
from collections import defaultdict
import utils


PACKET_A = [[2]]
PACKET_B = [[6]]


class Sortable:
    def __init__(self,data):
        self.data = data

    def cmp(self, a, b):
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
            for a_part, b_part in zip(a, b):
                res = self.cmp(a_part, b_part)
                if res is not None:
                    return res
            if len(a) < len(b):
                return True
            if len(a) > len(b):
                return False
            if len(a) == len(b):
                return None
        return None

    def __lt__(self,other):
        return self.cmp(self.data, other.data)
    def __eq__(self,other):
        return self.cmp(self.data, other) is None

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    # def comparator(self, a, b):
    #     res = self.cmp(a, b)
    #     if res == True:
    #         return 1
    #     elif res == False:
    #         return -1
    #     return 0

    def solve(self):
        print(self.lines)
        data = [Sortable(x) for x in self.lines]
        result = sorted(data)
        return (result.index(PACKET_A) + 1) * (result.index(PACKET_B) + 1)


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = [
        PACKET_A,
        PACKET_B,
    ]
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        if line == "":
            continue
        processed_data.append(eval(line))
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
