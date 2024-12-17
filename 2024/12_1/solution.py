""" Advent of code 2024 day 12 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


def add(a, b):
    return tuple(map(sum, zip(a, b)))


DIRECTIONS = {  # Y, X
    "N": (-1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
}


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.maxh = len(lines)
        self.maxw = len(lines[0])

    def get_regions(self):
        named_regions = defaultdict(dict)
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                neighbors = []
                for d, diff in DIRECTIONS.items():
                    n_y, n_x = add((y, x), diff)
                    if (0 <= n_y < self.maxh) and (0 <= n_x < self.maxw):
                        neighbor = self.lines[n_y][n_x]
                        neighbors.append(((n_y,n_x), d, neighbor == c))
                    else:
                        neighbors.append(((n_y, n_x), d, None))
                named_regions[c][(y, x)] = tuple(neighbors)
        regions = []
        for n, og_region in named_regions.items():
            visited = set()
            region = set(og_region.keys())
            while region:
                current_region = set()
                region_start = region.pop()
                if region_start in visited:
                    continue
                queue = [region_start]

                while queue:
                    curr_pos = queue.pop()
                    if curr_pos in visited:
                        continue
                    visited.add(curr_pos)
                    current_region.add(curr_pos)
                    for n_pos, _, n_type in og_region.get(curr_pos, []):
                        if n_type == True:
                            queue.append(n_pos)
                regions.append((n, set([(n, pos, og_region[pos]) for pos in current_region])))
        # pprint(regions)
        return regions

    def calculate_region(self, region) -> tuple[int, int]:
        area = len(region)
        # perimeter = sum([1 if n_type else 0 for _, neighbors in region for n_dir, n_type in neighbors])
        perimeter = 0
        for pos, _direction, neighbors in region:
            # print(pos, neighbors)
            for _, _, n_type in neighbors:
                if n_type == False or n_type == None:
                    perimeter += 1
        return (area, perimeter)

    def solve(self):
        regions = self.get_regions()
        result = 0
        for region_name, region in regions:
            area, perimeter = self.calculate_region(region)
            res = area * perimeter
            # print(f"{region_name}: Area: {area} Perimeter: {perimeter}")
            result += res

        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = list(line)
        processed_data.append(data)
    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
