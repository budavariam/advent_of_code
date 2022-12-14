""" Advent of code 2022 day 14 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


# NOTE: coords in (x,y)
START = (500, 0)


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def sand_fall(self, num, start_pos: tuple, occupied_blocks, max_depth):
        """
        A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.
        """
        n_x, n_y = start_pos
        finished = False
        is_rest = False
        while not is_rest:
            n_y += 1
            # if n_y == max_depth:
            #     print(f"Sand {num} reached max_depth ({n_y}, {max_depth})")
            #     finished = True
            #     break
            if (n_x, n_y) in occupied_blocks:
                if (n_x - 1, n_y) not in occupied_blocks:
                    n_x -= 1
                    # print(f"Sand {num} falling left: ({n_x}, {n_y})")
                elif (n_x + 1, n_y) not in occupied_blocks:
                    n_x += 1
                    # print(f"Sand {num} falling right: ({n_x}, {n_y})")
                else:
                    is_rest = True
                    n_y -= 1
                    # print(f"Sand {num} is at rest: ({n_x}, {n_y})")
            else:
                # print(f"Sand {num} falling down: ({n_x}, {n_y})")
                pass
        return (n_x, n_y), finished

    def solve(self):
        # pprint(self.lines)
        occupied, max_depth = self.lines
        num_sand = 0
        finished = False
        while not finished:
            sand_res_pos, finished = self.sand_fall(
                num_sand, START, occupied, max_depth
            )
            if sand_res_pos in occupied:
                finished = True
            occupied.add(sand_res_pos)
            num_sand += 1
        return num_sand - 1


def gen_coords(paths):
    res = []
    for ((a_x, a_y), (b_x, b_y)) in zip(paths, paths[1:]):
        # print((a_x, a_y), (b_x, b_y))
        if a_x != b_x and a_y != b_y:
            # diagonal
            d_x = b_x - a_x
            d_y = b_x - a_x
            for _ in range(abs(d_x)):
                res.append((a_x + d_x, a_y + d_y))
        else:
            for y in range(min(a_y, b_y), max(a_y, b_y) + 1):
                for x in range(min(a_x, b_x), max(a_x, b_x) + 1):
                    res.append((x, y))
    # print("coords: ------")
    # pprint(paths)
    # pprint(res)
    # print("------")
    return set(res)


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = set([])
    max_depth = math.inf

    for line in raw_data.split("\n"):
        data = [[int(c) for c in coord.split(",")] for coord in line.split(" -> ")]
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        processed_data = processed_data.union(gen_coords(data))

    min_depth_x = min([x for (x, y) in processed_data]) - 10000
    max_depth_x = max([x for (x, y) in processed_data]) + 10000
    max_depth_y = max([y for (x, y) in processed_data]) + 2
    processed_data = processed_data.union(gen_coords([[min_depth_x, max_depth_y], [max_depth_x, max_depth_y]]))
    return [processed_data, max_depth_y]


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
