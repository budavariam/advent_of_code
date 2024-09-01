""" Advent of code 2023 day 10 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

OPP_DIRECTIONS = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W",
}
DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        for y, l in enumerate(lines):
            x = l.find("S")
            if x > -1:
                self.curr = (y, x)
                break
        self.start = self.curr
        self.maxw = len(lines[0])
        self.maxh = len(lines)

    def move(self, end_1, end_2, c_y, c_x, direction, symbol):
        y, x = c_y, c_x
        next_d = direction
        if direction == end_1:
            # y, x = add((c_y, c_x), DIRECTIONS[end_2])
            next_d = end_2
        elif direction == end_2:
            # y, x = add((c_y, c_x), DIRECTIONS[end_1])
            next_d = end_1
        else:
            raise ValueError(
                f"  NOT PASSABLE: '{symbol}' at {(c_y, c_x)} with direction: '{direction}' (only from '{end_1}' or '{end_2}')"
            )
        return y, x, next_d

    def step_on_matrix(
        self, curr: tuple[int, int], direction: str
    ) -> tuple[int, int, str]:
        c_y, c_x = curr
        y, x = c_y, c_x
        msg = "..."
        symbol = self.lines[c_y][c_x]
        d = direction
        match symbol:
            case "|":
                msg = "| is a vertical pipe connecting north and south."
                y, x, d = self.move("N", "S", c_y, c_x, direction, symbol)
            case "-":
                msg = "- is a horizontal pipe connecting east and west."
                y, x, d = self.move("E", "W", c_y, c_x, direction, symbol)
            case "L":
                msg = "L is a 90-degree bend connecting north and east."
                y, x, d = self.move("N", "E", c_y, c_x, direction, symbol)
            case "J":
                msg = "J is a 90-degree bend connecting north and west."
                y, x, d = self.move("N", "W", c_y, c_x, direction, symbol)
            case "7":
                msg = "7 is a 90-degree bend connecting south and west."
                y, x, d = self.move("S", "W", c_y, c_x, direction, symbol)
            case "F":
                msg = "F is a 90-degree bend connecting south and east."
                y, x, d = self.move("S", "E", c_y, c_x, direction, symbol)
            case ".":
                msg = ". is ground; there is no pipe in this tile."
                y, x, d = c_y, c_x, direction
            case "S":
                msg = "S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has."
                raise NameError(f" . START POSITION {self.curr}")
            case _:
                raise ValueError(f" . ERROR at {self.curr}")
        # print("  " + msg)

        return (y, x, d)

    def solve(self):
        queue = []
        result = []
        for d in DIRECTIONS.keys():
            queue.append((self.start, d, 0))
        while queue:
            curr, next_d, distance = queue.pop()
            try:
                next_y, next_x = add(curr, DIRECTIONS[next_d])
                direction = OPP_DIRECTIONS[next_d]
                # print(f"ENTERING ({next_y},{next_x}) from {direction} #{distance}")
                if (
                    next_y >= self.maxh
                    or next_y < 0
                    or next_x >= self.maxw
                    or next_x < 0
                ):
                    # print(f"  Over bounds!")
                    continue
                y, x, d = self.step_on_matrix((next_y, next_x), direction)
                queue.append(((y, x), d, distance + 1))
            except NameError:
                # print(f"  Back to start {n}, {curr}, {next_d}, {distance}")
                result.append(distance + 1)
            except ValueError:
                # print(v)
                pass
        # print(result)
        return max(result) // 2


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
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
