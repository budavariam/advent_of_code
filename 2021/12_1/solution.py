""" Advent of code 2021 day 12 / 1 """

import math
from os import path
import re
from collections import deque, defaultdict

class Code(object):
    def __init__(self, lines):
        self.edges = lines[0]
        self.nodes = lines[1]
        self.graph = defaultdict(set)
        for [a,b] in self.edges:
            self.graph[a].add(b)
            self.graph[b].add(a)

    def paths(self, s, e, visited):
        if s in visited and s.islower():
            return
        visited.add(s)
        if s == e:
            # get last item
            yield visited 
        for neighbour in self.graph[s]:
            # split into multiple generators
            yield from self.paths(neighbour, e, visited.copy()) 

    def solve(self):
        visited = set()
        paths = [path for path in self.paths('start', 'end', visited)]
        return len(paths)

def preprocess(raw_data):
    processed_data = []
    nodes = set()
    for line in raw_data.split("\n"):
        data = line.split("-")
        nodes.add(data[0])
        nodes.add(data[1])
        processed_data.append(data)
    nodelst = [(x, x.isupper()) for x in (nodes - set(['start', 'end']))]
    return [processed_data, nodelst]


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
