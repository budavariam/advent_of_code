"""Advent of code 2024 day 20 / 1"""

import math
from pprint import pprint
from os import path
import re
import copy
from collections import defaultdict, Counter
from utils import log, profiler

# IDEA: on the first run calculate the distance normally, mark the distnces in a grid. and then on the second pass check every path and modify the distances accordingly


def add(a, b):
    return tuple(map(sum, zip(a, b)))


DIRECTIONS = {  # Y, X
    "N": ((-1, 0), False),
    "E": ((0, 1), False),
    "W": ((0, -1), False),
    "S": ((1, 0), False),
}
CHEAT_DIRECTIONS = {  # Y, X
    "N": ((-1, 0), (-2, 0)),
    "E": ((0, 1), (0, 2)),
    "W": ((0, -1), (0, -2)),
    "S": ((1, 0), (2, 0)),
}


class Code(object):
    def __init__(self, processed_data):
        self.processed_data = processed_data

    def search(self, grid, directions, start, end, override_grid=False):
        queue = [(start, 0, None, set([]))]
        results = []
        og_distance = -1
        # # debug = print if not override_grid else lambda *x: x
        # debug = lambda *x: x
        while queue:
            curr = queue.pop()
            curr_pos, distance, cheat_location, visited = curr
            # debug(f"Visiting: {curr_pos}")
            # # debug(curr_pos, distance)
            curr_y, curr_x = curr_pos
            curr_visited = set(visited)
            curr_visited.add(curr_pos)
            if override_grid:
                grid[curr_y][curr_x] = distance
            if cheat_location:
                # short circuit
                # debug(f"  Found cheat @{curr} from {cheat_location}")
                prev_distance = grid[cheat_location[0]][cheat_location[1]]
                cheat_distance = grid[curr_y][curr_x]
                results.append(cheat_distance - prev_distance - 2)
                continue
            if curr_pos == end:
                # debug("  END FOUND", distance, cheat_location)
                if not cheat_location:
                    og_distance = distance
                continue
            for d, cheat_dir in directions.values():
                next_pos = add(d, curr_pos)
                next_y, next_x = next_pos
                if (
                    next_pos in curr_visited
                    or next_y < 0
                    or next_y >= self.processed_data["bounds"]["y"]
                    or next_x < 0
                    or next_x >= self.processed_data["bounds"]["x"]
                ):
                    continue
                next_is_wall = grid[next_y][next_x] == "#"
                if next_is_wall:
                    # debug(f"  Hit a wall @{next_pos}")
                    if cheat_dir:
                        nn_pos = add(cheat_dir, curr_pos)
                        nn_y, nn_x = nn_pos
                        if (
                            nn_pos in curr_visited
                            or nn_y < 0
                            or nn_y >= self.processed_data["bounds"]["y"]
                            or nn_x < 0
                            or nn_x >= self.processed_data["bounds"]["x"]
                        ):
                            continue
                        else:
                            nn_is_wall = grid[nn_y][nn_x] == "#"
                            if not nn_is_wall:
                                # debug(f"  Feasible cheat from {curr_pos} to {nn_pos}")
                                next_queue_item = (
                                    nn_pos,
                                    distance + 2,
                                    curr_pos,
                                    curr_visited,
                                )
                                queue.append(next_queue_item)
                    continue
                else:
                    next_queue_item = (
                        next_pos,
                        distance + 1,
                        cheat_location,
                        curr_visited,
                    )
                    # # debug("NQ:", distance, next_queue_item)
                    queue.append(next_queue_item)
        # debug("Search finished", results)
        return results, og_distance, grid

    def solve(self, nr_over):
        # pprint(self.processed_data)
        result = 0
        grid = copy.deepcopy(self.processed_data["map"])
        _, _, distance_grid = self.search(
            grid,
            DIRECTIONS,
            self.processed_data["start_pos"],
            self.processed_data["end_pos"],
            True,
        )
        results, _, _ = self.search(
            distance_grid,
            CHEAT_DIRECTIONS,
            self.processed_data["start_pos"],
            self.processed_data["end_pos"],
            False,
        )

        cheats = set()

        cnt = Counter(results)
        # print("CCC", results, cnt, cheats)

        if nr_over == 0:
            return set([(v, k) for k, v in cnt.items()])
        else:
            result = 0
            for picosec_saved, count in cnt.items():
                if picosec_saved >= nr_over:
                    result += count
            return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = {"map": [], "start_pos": (-1, -1), "end_pos": (-1, -1)}
    grid = raw_data.split("\n")
    for y, line in enumerate(grid):
        data = list(line)
        for x, char in enumerate(data):
            if char == "." or char == "#":
                continue
            elif char == "S":
                processed_data["start_pos"] = (y, x)
            elif char == "E":
                processed_data["end_pos"] = (y, x)
        processed_data["map"].append(data)
    processed_data["bounds"] = {
        "y": len(grid),
        "x": len(grid[0]),
    }
    return processed_data


@profiler
def solution(data, nr_over=None):
    """Solution to the problem"""
    processed_data = preprocess(data)
    solver = Code(processed_data)
    return solver.solve(nr_over)


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read(), 100))
