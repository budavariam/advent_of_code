"""Advent of code 2024 day 18 / 2"""

import math
from pprint import pprint
from os import path
from utils import log, profiler
import heapq


def add(a, b):
    return tuple(map(sum, zip(a, b)))


DIRECTIONS = {  # X, Y
    "N": (-1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
}


class Code(object):
    def __init__(self, lines, grid_max):
        self.lines = lines
        self.grid_max = grid_max
        self.max_nodes = grid_max * grid_max

    def print_map(self, lines=None, visited=None):
        if visited is None:
            visited = set()
        if lines is None:
            lines = []
        else:
            lines = set(lines)
        for y in range(0, self.grid_max + 1):
            for x in range(0, self.grid_max + 1):
                c = "#" if (x, y) in lines else "."
                if (x, y) in visited:
                    c = "v"
                print(c, end="")
            print("\n", end="")

    def find_min_path(self, d):
        queue = [(0, 0, 0)]
        end = (self.grid_max, self.grid_max)
        curr = None
        min_dist = float("inf")
        visited = set()
        lines = set(d)
        while len(queue) > 0:
            data = heapq.heappop(queue)
            dist, x, y = data
            min_dist = min(dist, min_dist)
            curr = (x, y)
            if curr in visited:
                continue
            # self.print_map(lines, visited)
            # print(f"Visiting ({x},{y})")
            # print(f"{len(visited)}/{self.max_nodes} {(len(queue))}")
            visited.add(curr)
            if curr == end:
                return dist

            for d in DIRECTIONS.values():
                new_x, new_y = add(curr, d)
                new_dist = dist + 1
                if new_dist > (min_dist * 1.1):
                    pass
                    # print(f"WAAAA {new_dist} {min_dist}")
                if (new_x, new_y) in lines:
                    # print(f"  Corrupted ({new_x},{new_y})")
                    pass
                elif (new_x, new_y) in visited:
                    # print(f"  Visited ({new_x},{new_y})")
                    pass
                elif 0 <= new_x <= self.grid_max and 0 <= new_y <= self.grid_max:
                    heapq.heappush(queue, (new_dist, new_x, new_y))
                    # print(f"  Pushed ({new_x},{new_y}) with dist:{new_dist}")
                    pass
                else:
                    # print(f"  OOB ({new_x},{new_y})")
                    pass
        return None

    def bisect(self, list_of_values, cb):
        final_index = None
        low = 0
        high = len(list_of_values)
        while low <= high:
            mid = (low + high) // 2
            calc_result = cb(list_of_values[:mid])
            print(f"Calc result for {mid} is {calc_result} ({low},{high})")
            if calc_result is None:
                final_index = mid
                high = mid - 1
            else:
                low = mid + 1
        return list_of_values[final_index-1]

    def solve(self):
        pprint(self.lines)
        x,y = self.bisect(self.lines, self.find_min_path)
        return f"{x},{y}"


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    # Coord = namedtuple("Coord", ["x", "y"])
    for i, line in enumerate(raw_data.split("\n")):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = tuple([int(n, 10) for n in line.split(",")])
        # processed_data.append(Coord(*data))
        processed_data.append(data)
    return processed_data


@profiler
def solution(data, grid_max=70):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines, grid_max)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
