""" Advent of code 2023 day 05 / 2 """

import math
from os import path
import utils
from functools import total_ordering

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


LEVELS = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


class Code(object):
    def __init__(self, lines):
        self.pd: ProcessedData = lines

    def solve(self):
        # transform the ranges instead of calculating the seeds one by one, and find the smallest range_start in the locations level
        seed_intervals = self.pd.seeds
        result = math.inf

        while seed_intervals:
            curr_seed = seed_intervals.pop()
            new_start, new_end = curr_seed.start, curr_seed.end
            next_level = curr_seed.level + 1
            print(new_start, new_end, curr_seed.level)
            if next_level == 8:
                result = min(new_start, result)
                logger.info(f"- {result}")
                continue
            logger.debug(f"Inspecting: {curr_seed} @ {LEVELS[curr_seed.level]}")
            for other in self.pd.maps[curr_seed.level]:
                logger.debug(f"  comparing {curr_seed} with: {other}")
                new_start, new_end = curr_seed.start, curr_seed.end
                jumplevel = other.dest_start - other.source_start
                if new_end <= other.source_start or other.source_end <= new_start:
                    logger.debug("    no overlap")
                    continue
                if new_start < other.source_start:
                    a, b, c = (
                        new_start,
                        other.source_start,
                        curr_seed.level,
                    )
                    logger.debug(
                        f"    add new seed_range until other_range start [{c}]:{a}-{b}"
                    )
                    seed_intervals.append(SeedRange(a, b, c))
                    new_start = other.source_start
                if other.source_end < new_end:
                    a, b, c = (
                        other.source_end,
                        new_end,
                        curr_seed.level,
                    )
                    logger.debug(f"    cut seed_range by other_range end [{c}]:{a}-{b}")
                    seed_intervals.append(SeedRange(a, b, c))
                    new_end = other.source_end
                a, b, c = new_start + jumplevel, new_end + jumplevel, next_level
                logger.debug(
                    f"    overlap perfectly, jump level by '{jumplevel}' from [{curr_seed.level}]:{new_start}:{new_end} to [{c}]:{a}-{b}"
                )
                seed_intervals.append(SeedRange(a, b, c))
                break
            else:
                a, b, c = new_start, new_end, next_level
                logger.debug(f"    Not found.... propagate to next level [{c}]:{a}-{b}")
                seed_intervals.append(SeedRange(a, b, c))
        return result


class SeedRange:
    start: int
    end: int
    range_len: int
    level: int

    def __repr__(self):
        return f"[{self.level}]:{self.start}-{self.end}"

    def __init__(self, src_start, src_end, level=0):
        self.start = src_start
        self.end = src_end
        self.range_len = src_end - src_start
        self.level = level


@total_ordering
class MappingRange:
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


class ProcessedData:
    seeds: list[SeedRange] = []
    maps: list[list[MappingRange]] = []

    def __repr__(self):
        res = "Seeds:\n"
        res += ",\n".join([str(rng) for rng in self.seeds])
        for i, curr_mapping in enumerate(self.maps):
            res += f"\n\n{LEVELS[i]}:\n"
            res += ",\n".join([str(rng) for rng in curr_mapping])
            res += "\n"
        return res


@utils.profiler
def preprocess(raw_data: str):
    processed_data: ProcessedData = ProcessedData()
    blocks = raw_data.split("\n\n")
    raw_seeds = [int(s) for s in blocks[0].split(": ")[1].split(" ")]
    seeds: list[SeedRange] = []
    for s, s_len in zip(raw_seeds[::2], raw_seeds[1::2]):
        seeds.append(SeedRange(s, s + s_len))
    processed_data.seeds = seeds
    for blk in blocks[1:]:
        block_data = []
        for i, line in enumerate(blk.split("\n")):
            print(i, line)
            if i == 0:
                continue
            r = MappingRange(*[int(x) for x in line.split(" ")])
            block_data.append(r)
        processed_data.maps.append(sorted(block_data))
    logger.debug(processed_data)
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
