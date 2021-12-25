""" Advent of code 2021 day 25 / 1 """

import math
from os import path
import re


class Code(object):
    def __init__(self, data):
        self.grid = data[0]
        self.height = data[1]
        self.width = data[2]

    def printmap(self, grid = None):
        if grid is None:
            print("Prev")
            grid = self.grid
        else:
            print("New")
        for y in range(0, self.height):
            line = ""
            for x in range(0, self.width):
                line += grid[(y, x)] if (y, x) in grid else "."
            print(line)

    def step(self):
        new_grid = {}
        can_step = False
        cnt = len(self.grid)
        for which in ['>', 'v']:
            for (y, x), what in self.grid.items():
                (d_y, d_x) = (1, 0) if what == 'v' else (0, 1)
                if which == what:
                    n_y = (d_y + y) % self.height
                    n_x = (d_x + x) % self.width
                    if which == '>':
                        can_move = not((n_y, n_x) in self.grid)
                    elif which == 'v':
                        # there's nobody yet in the new grid AND there was not any v in the original over there
                        can_move = not((n_y, n_x) in new_grid) and not(self.grid.get((n_y, n_x)) == 'v')

                    # print(y, x, can_move, n_y, n_x)
                    if can_move:
                        new_grid[(n_y, n_x)] = what
                    else:
                        new_grid[(y, x)] = what
                    can_step = can_step or can_move
                else:
                    continue
        # self.printmap()
        # self.printmap(new_grid)
        new_cnt = len(new_grid)
        if new_cnt != cnt:
            raise(Exception(f"Inconsistent state: {new_cnt} != {cnt}"))
        self.grid = new_grid
        return can_step

    def solve(self):
        can_step = True
        i = 0
        # self.printmap()
        while can_step:
            print(f"Step {i}")
            can_step = self.step()
            # self.printmap()
            i += 1
        return i


def preprocess(raw_data):
    processed_data = {}
    for y, line in enumerate(raw_data.split("\n")):
        for x, what in enumerate(line):
            if what != '.':
                processed_data[(y, x)] = what
    height = y + 1
    width = x + 1
    return (processed_data, height, width)


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
