""" Advent of code 2024 day 23 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler
from itertools import combinations


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def bronKerbosch(self, R: set, P: set, X: set, depth=0):
        """
        Bron-Kerbosch algorithm for finding a maximal clique.
        https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
        """
        if not P and not X:
            return R

        maximal_clique = set()
        for vertex in list(P):
            new_R = R | {vertex}
            new_P = P & self.lines[vertex]
            new_X = X & self.lines[vertex]

            clique = self.bronKerbosch(new_R, new_P, new_X, depth + 1)
            if len(clique) > len(maximal_clique):
                maximal_clique = clique

            P.remove(vertex)
            X.add(vertex)

        return maximal_clique

    def solve(self):
        computer_names = self.lines.keys()
        maximal_graph = self.bronKerbosch(R=set(), P=set(computer_names), X=set())

        return ",".join(sorted(list(maximal_graph)))


@profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\w+)-(\w+)")
    processed_data = defaultdict(set)
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        c1, c2 = [match.group(1), match.group(2)]
        # data = list(line)
        processed_data[c1].add(c2)
        processed_data[c2].add(c1)
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
