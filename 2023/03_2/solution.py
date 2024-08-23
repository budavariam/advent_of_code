""" Advent of code 2023 day 03 / 1 """

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
        pprint(self.lines)
        result = 0
        gears = self.lines["gears"]
        numbers = self.lines["numbers"]
        for gear_neighbours in gears.values():
            if len(gear_neighbours) == 2:
                result += math.prod([numbers[n] for n in gear_neighbours])
        return result


directions = [
    (0, -1),
    # (0,0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]


def is_special(chr: str):
    return (not chr.isdigit()) and (chr != ".")


@utils.profiler
def preprocess(raw_data):
    matrix = raw_data.split("\n")
    len_y = len(matrix)
    len_x = len(matrix[0])
    processed_data = {
        "gears": {},
        "numbers": {},
    }
    gears: dict[(int, int), set] = {}
    for y, line in enumerate(matrix):
        for x, c in enumerate(line):
            if c == "*":
                gears[(y, x)] = set([])

    curr_num_index = 1
    for y, line in enumerate(matrix):
        curr_num = 0
        num_started = False
        for x, c in enumerate(line):
            is_digit = c.isdigit()
            coords = [(y + d_y, x + d_x) for (d_y, d_x) in directions]
            coords = [
                (c_y, c_x)
                for (c_y, c_x) in coords
                if (0 <= c_y < len_y) and (0 <= c_x < len_x)
            ]
            # print(y, x, c, coords)
            if is_digit:
                neighbor_gear_coords = [c if c in gears else None for c in coords]
                neighbor_gear_coords = [
                    x for x in neighbor_gear_coords if x is not None
                ]
                # print(coords, neighbor_gear_coords)
                for g in neighbor_gear_coords:
                    gears[g].add(curr_num_index)
                if num_started:
                    curr_num *= 10
                curr_num += int(c)
                num_started = True
            else:
                if num_started:
                    # not a number anymore, save it
                    processed_data["numbers"][curr_num_index] = curr_num
                    curr_num_index += 1
                    # reset on blank
                    num_started = False
                    curr_num = 0
                elif not num_started:
                    # not a number at all
                    continue
        if num_started:
            # not a number at the end of line, save it
            processed_data["numbers"][curr_num_index] = curr_num
            curr_num_index += 1
    processed_data["gears"] = gears
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
