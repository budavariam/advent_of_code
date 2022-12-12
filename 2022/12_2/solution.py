""" Advent of code 2022 day 12 / 2 """

import math
from os import path
import re
from collections import defaultdict, deque
import utils

FOUR_NEIGHBORS = set([(0, 1), (1, 0), (0, -1), (-1, 0)])


def search(grid, start_node_list, end_node, grid_height, grid_width):
    seen = set()
    q = deque([(start_node, 0) for start_node in start_node_list])
    while len(q) > 0:
        pos, dist = q.popleft()
        if pos == end_node:
            return dist

        if pos in seen:
            continue
        seen.add(pos)

        y, x = pos
        for dy, dx in FOUR_NEIGHBORS:
            n_y, n_x = y + dy, x + dx

            y_inside = 0 <= n_y < grid_height
            x_inside = 0 <= n_x < grid_width
            if (not y_inside) or (not x_inside):
                continue
            prev_c = grid[(n_y, n_x)]
            curr_c = grid[(y, x)]
            valid_move = ord(prev_c) - ord(curr_c) <= 1
            # print(prev_c, curr_c, valid_move)
            if valid_move:
                q.append(((n_y, n_x), dist + 1))
    return -1


class Code(object):
    def __init__(self, data):
        self.data = data

    def solve(self):
        # print(self.data)
        result = search(
            self.data["grid"],
            self.data["start_node_list"],
            self.data["end_node"],
            self.data["grid_height"],
            self.data["grid_width"],
        )
        return result


@utils.profiler
def preprocess(raw_data):
    processed_data = {
        "grid": {},
        "start_node_list": [],
        "end_node": (-1, -1),
        "grid_height": -1,
        "grid_width": -1,
    }
    grid = {}
    start_node_list = []
    split = raw_data.split("\n")
    for y, line in enumerate(split):
        for x, c in enumerate(line):
            if c == "S" or c == 'a':
                start_node_list.append((y, x))
                grid[(y, x)] = 'a'
            elif c == "E":
                processed_data["end_node"] = (y, x)
                grid[(y, x)] = 'z'
            else:
                grid[(y, x)] = c

    processed_data["grid"] = grid
    processed_data["grid_height"] = len(split)
    processed_data["grid_width"] = len(split[0])
    processed_data["start_node_list"] = start_node_list
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
