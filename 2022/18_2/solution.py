""" Advent of code 2022 day 18 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

SIDES = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

LOWER_BOUND, MIN_V = math.inf, math.inf
UPPER_BOUND, MAX_V = -math.inf, -math.inf

def get_neighbours(pos):
    x, y, z = pos
    neighbours = []
    for delta in SIDES:
        neighbour = (x + delta[0], y + delta[1], z + delta[2])
        for k in neighbour:
            if not (LOWER_BOUND <= k <= UPPER_BOUND):
                break
        else:
            neighbours.append(neighbour)
    return neighbours

def depth_first_search(start, cubes):
    """ https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/ """
    queue = [start]
    result = set()
    result.add(start)

    while len(queue) > 0:
        current = queue.pop()
        for nbr in get_neighbours(current):
            if nbr in result:
                continue
            if nbr in cubes:
                continue
            queue.append(nbr)
            result.add(nbr)

    return result

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        start = (LOWER_BOUND, LOWER_BOUND, LOWER_BOUND)
        steam_cells = depth_first_search(start, self.lines)

        result = 0
        for cube in self.lines:
            for nbr in get_neighbours(cube):
                if nbr in steam_cells:
                    result += 1

        return result

@utils.profiler
def preprocess(raw_data):
    global LOWER_BOUND, UPPER_BOUND, MIN_V, MAX_V
    processed_data = set()
    for line in raw_data.split("\n"):
        x,y,z = (int(a) for a in line.split(','))
        for k in (x, y, z):
            MIN_V = min(MIN_V, k)
            MAX_V = max(MAX_V, k)
        processed_data.add((x,y,z))

    LOWER_BOUND = MIN_V - 1
    UPPER_BOUND = MAX_V + 1
    
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
