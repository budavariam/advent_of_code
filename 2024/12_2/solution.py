""" Advent of code 2024 day 12 / 2 """

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

MOVE_DIRS = { 
    "N": ["E", "W"],
    "E": ["N", "S"],
    "W": ["N", "S"],
    "S": ["E", "W"],
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
                        neighbors.append(((n_y, n_x), d, neighbor == c))
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
                regions.append(
                    (n, set([(n, pos, og_region[pos]) for pos in current_region]))
                )
        # pprint(regions)
        return regions

    def extend_line(self, start, direction, points, visited):
        dy, dx = DIRECTIONS[direction]
        current = start
        line = []
        current = add(current, (dy, dx))
        while current in points and current not in visited:
            line.append(current)
            visited.add(current)
            current = add(current, (dy, dx))
        return line
    def count_lines(self, points_by_direction):

        lines_count = {}

        for direction, points in points_by_direction.items():
            points = set(points)  # Ensure points is a set for fast lookup
            visited = set()
            relevant_dirs = MOVE_DIRS[direction]
            lines = []

            for point in points:
                if point not in visited:
                    # Extend the line in both relevant directions
                    full_line = set()
                    for move_dir in relevant_dirs:
                        extended = self.extend_line(point, move_dir, points, visited)
                        extended.append(point)
                        full_line.update(extended)

                    lines.append(full_line)
                    visited.add(point)
            # print(direction)
            # pprint(full_line)
            # pprint(visited)
            # pprint(lines)
            # Add the total number of distinct lines for this direction
            lines_count[direction] = len(lines)

        return lines_count

    def calc_fence(self, region):
        border_positions = set([])
        borders = set([])
        border_quick_access = defaultdict(set)
        for nm, pos, neighbors in region:
            for n in neighbors:
                n_pos, n_dir, n_is_inside = n
                if not n_is_inside:
                    borders.add((n_dir, n_pos))
                    border_quick_access[n_dir].add(n_pos)

        # print(border_quick_access)
        # self.print_map(borders)

        fences = self.count_lines(border_quick_access)
        result = sum(fences.values())
        # print(fences, result)
        return result

    def print_map(self, borders):
        items = set([])
        for _, n_pos in borders:
            items.add(n_pos)
        for y in range(-1, self.maxh + 1):
            line = ""
            for x in range(-1, self.maxw + 1):
                if (y, x) in items:
                    line += "x"
                else:
                    line += "."
            print(line)
        print("-----")

    def calculate_region(self, region) -> tuple[int, int]:
        area = len(region)
        fences = self.calc_fence(region)

        return (area, fences)

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
