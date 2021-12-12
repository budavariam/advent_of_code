""" Advent of code 2021 day 12 / 2 """

import math
from os import path
import re
from collections import deque, defaultdict


class Code(object):
    def __init__(self, lines):
        self.edges = lines[0]
        self.nodes = lines[1]
        self.graph = defaultdict(set)
        for [a, b] in self.edges:
            self.graph[a].add(b)
            self.graph[b].add(a)

    def paths(self, s, e, visited, doubled):
        cnt = 0
        if s == e:
            # get last item
            return 1
        for neighbour in self.graph[s]:
            n_doubled = doubled
            if neighbour in visited and neighbour.islower():
                # check for exceptional case
                if doubled or neighbour in ['start','end']:
                    # ignore visited or doubled or start/end
                    continue
                else:
                    # we let the visited small neighbour calced and mark it in further calcs
                    n_doubled = True
            n_vis = visited.copy().union(set([s]))
            cnt += self.paths(neighbour, e, n_vis, n_doubled)
        return cnt

    def solve(self):
        return self.paths('start', 'end', set(), False)


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
