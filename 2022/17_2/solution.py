""" Advent of code 2022 day 17 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

ROCKS = (
    (0, 1, 2, 3),
    (1, 0 + 1j, 2 + 1j, 1 + 2j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 0 + 1j, 0 + 2j, 0 + 3j),
    (0, 1, 0 + 1j, 1 + 1j),
)


def empty_slot(position, tower):
    return position.real in range(7) and position.imag > 0 and position not in tower


class Code(object):
    def __init__(self, lines):
        self.jetlist = lines[0]

    def solve(self):
        pprint(self.jetlist)
        height = 0
        i = 0
        j = 0
        tower = set([-1])
        cache = {}
        for falling_num in range(1000000000000 + 1):
            height = max(x.imag for x in tower)
            position = complex(2, height + 4)
            rock = ROCKS[i]
            i = (i + 1) % len(ROCKS)

            # check for cycle
            key = i, j
            if key in cache:
                N, H = cache[key]
                d, m = divmod(1000000000000 - falling_num, N - falling_num)
                if not m:
                    return int(height + (H - height) * d)
            else:
                cache[key] = falling_num, height

            while True:
                jet = +1 if self.jetlist[j] == ">" else -1
                j = (j + 1) % len(self.jetlist)
                if all(empty_slot(position + jet + shape, tower) for shape in rock):
                    # sideways
                    position += jet
                if all(empty_slot(position - 1j + shape, tower) for shape in rock):
                    # down
                    position -= 1j
                else:
                    break
            tower = tower.union([position + r for r in rock])
        return int(height)


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
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
