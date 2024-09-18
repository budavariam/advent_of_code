""" Advent of code 2023 day 12 / 2 """

from pprint import pprint
from os import path
import utils
import re
from functools import lru_cache

island_pattern = re.compile(r"#+\.")


@lru_cache(maxsize=10000)
def calculate_str(current_slice, hints):
    if "?" not in current_slice:
        # no variable components, check the validity
        if tuple([len(x) for x in current_slice.split(".") if len(x) > 0]) == hints:
            return 1
        else:
            return 0
    first_error_index = current_slice.index("?")
    island_borders = [
        (found_island.start(), found_island.end())
        for found_island in island_pattern.finditer(
            current_slice[: first_error_index + 1]
        )
    ]
    island_lengths = [end - start - 1 for start, end in island_borders]
    if len(hints) < len(island_lengths) or any(
        curr_l != expc_l for curr_l, expc_l in zip(island_lengths, hints)
    ):
        # the tuple lengths do not match
        # or there is at least one item that is not matching the expected length
        return 0

    last_end_before_error = 0
    if len(island_borders) > 0:
        _, last_end_before_error = island_borders.pop()
    new_hints = hints[len(island_lengths) :]
    result = 0
    for possible_value in ".#":
        result += calculate_str(
            (
                current_slice[last_end_before_error:first_error_index]
                + possible_value
                + current_slice[first_error_index + 1 :]
            ).strip("."),
            new_hints,
        )
    return result


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        result = 0
        for i, (code, solver_key) in enumerate(self.lines):
            print(f"{i+1}/{len(self.lines)}: {code}-{solver_key}")
            result += calculate_str(code, solver_key)
        return result


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        data = line.split(" ")
        processed_data.append(
            ["?".join([data[0]] * 5), tuple(map(int, data[1].split(",") * 5))]
        )
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
