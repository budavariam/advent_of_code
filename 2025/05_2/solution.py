"""Advent of code 2025 day 05 / 2"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
from functools import total_ordering


@total_ordering
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, num):
        return self.start <= num <= self.end

    def overlaps(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        # self is inside other
        if self.start >= other.start and self.end <= other.end:
            return True
        # other is inside self
        if other.start >= self.start and other.end <= self.end:
            return True
        # self starts earlier than other
        if self.start <= other.start and self.end >= other.start:
            return True
        # other starts earlier than self
        if other.start <= self.start and other.end >= self.start:
            return True
        return False
    
    def item_count(self):
        return self.end - self.start + 1

    def merge_into(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)
        return self

    def __repr__(self) -> str:
        return f"{self.start}-{self.end}"

    def _is_valid_operand(self, other):
        return hasattr(other, "start") and hasattr(other, "end")

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        if self.start == other.start:
            return self.end < other.end
        return self.start < other.start

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.start == other.start and self.end == other.end


class Code(object):
    def __init__(self, data):
        self.data = data

    def solve(self):
        result = 0
        # sort ranges by 'start'
        sorted_ranges = sorted(self.data["ranges"])
        pprint(sorted_ranges)
        # keep track of the current one and update it until reach a new one with greater start than the highest end
        current = sorted_ranges[0]
        distinct_ranges = []
        for r in sorted_ranges[1:]:
            print(f"Compare: {current} vs. {r}")
            if current.overlaps(r):
                current.merge_into(r)
                print(f"..They overlap. Updated item: {current}")
            else:
                distinct_ranges.append(current)
                # when we add it to the list in the meantime keep track of the result,  to save a loop at the end
                result += current.item_count()
                print(f"..They're distinct. result so far: {result}")
                current = r
        # don't forget to add the final one to the result
        distinct_ranges.append(current)
        result += current.item_count()
        print(f"Final Result: {result}")
        
        return result


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\d+)-(\d+)")
    processed_data = {"ranges": []}
    ranges, ingredients = raw_data.split("\n\n")

    for line in ranges.split("\n"):
        match = re.match(pattern, line)
        if match is not None:
            data = Interval(int(match.group(1)), int(match.group(2)))
            processed_data["ranges"].append(data)
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
