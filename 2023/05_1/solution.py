""" Advent of code 2023 day 05 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils
import json
from functools import total_ordering


class Code(object):
    def __init__(self, lines):
        self.pd: ProcessedData = lines

    def solve(self):
        result = 9999999999999999
        for seed in self.pd.seeds:
            mappings = self.pd.get_mapping(seed)
            result = min(mappings["location"], result)
        return result


@total_ordering
class Range:
    source_start: int
    source_end: int
    dest_start: int
    dest_end: int
    range_len: int

    def __repr__(self):
        return f"({self.range_len}):{self.source_start}-{self.source_end}:{self.dest_start}-{self.dest_end}"

    def __init__(self, dest_start, src_start, range_len):
        self.source_start = src_start
        self.source_end = src_start + range_len
        self.dest_start = dest_start
        self.dest_end = dest_start + range_len
        self.range_len = range_len

    def __le__(self, o):
        return self.source_start <= o.source_start

    def get_mapping(self, num: int):
        if self.source_start <= num < self.source_end:
            diff = num - self.source_start
            return self.dest_start + diff
        return None


class ProcessedData:
    seeds: list[int] = []
    maps: list[list[Range]] = []

    def __repr__(self):

        names = [
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ]

        res = f"Seeds: {self.seeds}"
        for i, curr_mapping in enumerate(self.maps):
            res += f"\n\n{names[i]}:\n"
            res += ",\n".join([str(rng) for rng in curr_mapping])
            res += "\n"
        return res

    def get_mapping(self, seed: int):
        curr = seed
        result = [curr]
        for level_ranges in self.maps:
            for x in level_ranges:
                mp = x.get_mapping(curr)
                if mp is not None:
                    curr = mp
                    break
            result.append(curr)
        return {
            "seed": result[0],
            "soil": result[1],
            "fertilizer": result[2],
            "water": result[3],
            "light": result[4],
            "temperature": result[5],
            "humidity": result[6],
            "location": result[7],
        }


@utils.profiler
def preprocess(raw_data: str):
    processed_data: ProcessedData = ProcessedData()
    blocks = raw_data.split("\n\n")
    seeds = [int(s) for s in blocks[0].split(": ")[1].split(" ")]
    processed_data.seeds = seeds
    for blk in blocks[1:]:
        block_data = []
        for i, line in enumerate(blk.split("\n")):
            if i == 0:
                continue
            r = Range(*[int(x) for x in line.split(" ")])
            block_data.append(r)
        processed_data.maps.append(sorted(block_data))
    print(processed_data)
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
