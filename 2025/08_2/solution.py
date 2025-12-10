"""Advent of code 2025 day 08 / 2"""

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from functools import cache
from utils import log, profiler
from itertools import combinations
from heapq import heappush, heappop


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    @cache
    def distance(self, a, b):
        return math.sqrt(sum([(b[i] - a[i]) ** 2 for i in range(3)]))

    def solve(self):
        n = len(self.lines)

        edges = []
        for i, j in combinations(range(n), 2):
            dist = self.distance(self.lines[i], self.lines[j])
            heappush(edges, (dist, i, j))

        # Union-Find to track circuits: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return None
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]
            return self.lines[x], self.lines[y]

        last_pair = ((0, 0, 0), (0, 0, 0))
        for _ in range(len(edges)):
            _, i, j = heappop(edges)
            connected_pair = union(i, j)
            if connected_pair:
                last_pair = connected_pair

        print(last_pair)
        if last_pair is not None:
            return last_pair[0][0] * last_pair[1][0]
        return -1


@profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = line.strip()
        if data:
            data = map(int, line.strip().split(","))
            processed_data.append(tuple(data))
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
