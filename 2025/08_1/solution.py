"""Advent of code 2025 day 08 / 1"""

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

    def solve(self, limit):
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
                return False
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]
            return True

        for _ in range(limit):
            _, i, j = heappop(edges)
            union(i, j)

        circuit_sizes = defaultdict(int)
        for i in range(n):
            root = find(i)
            circuit_sizes[root] = size[root]

        sizes = sorted(circuit_sizes.values(), reverse=True)
        return math.prod(sizes[0:3])


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
def solution(data, limit=1000):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve(limit)


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
