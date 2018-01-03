""" Advent of code 2017 day 24/1 """
from argparse import ArgumentParser
from copy import deepcopy
import re
from collections import defaultdict

def read_data(data):
    """ Read data blocks """
    pattern = re.compile(r'(\d+)/(\d+)')
    edges = defaultdict(set)
    for line in data.split('\n'):
        matches = re.match(pattern, line)
        val_a = int(matches.group(1))
        val_b = int(matches.group(2))
        edge = Edge(line, sorted([val_a, val_b]), (val_a + val_b))
        edges[val_a].add(edge)
        edges[val_b].add(edge)
    return edges

class Edge(object):
    """ Graph edge """
    def __init__(self, line, ends, strength):
        """ Constructor """
        self.val_l = ends[0]
        self.val_g = ends[1]
        self.strength = strength
        self.repr = line

    def __repr__(self):
        """ Reprecentation of the block """
        return "{}: {}".format(self.repr, self.strength)

    def other(self, connect):
        """ Return the other end of the edge """
        return self.val_l if connect == self.val_g else self.val_g

class Generator(object):
    """ Graph solver with generating all paths"""

    def __init__(self, edges):
        """ Constructor """
        self.edges = edges

    def find(self, connect, current_edge=None, visited=None, strength=0):
        """ Recursively generate the paths from start until it can
            * run the pathfinding to these edges
              * mark the edge as visited
              * find all edges that has the same end as its free slot
              * run the pathfinding to all edges that can be connected to it
              * if there isn't any edges, return with the value
              * return the highest score
        """
        if visited is None:
            visited = set()
        if current_edge is not None:
            visited = visited | {current_edge}
            strength += current_edge.strength
            connect = current_edge.other(connect)
        available = [edge for edge in self.edges[connect] if not edge in visited]
        if not available:
            return strength
        return max(self.find(connect, edge, visited, strength) for edge in available)

def solution(data):
    """ Solution to the problem """
    edges = read_data(data)
    solver = Generator(edges)
    start = 0
    strongest = solver.find(start)
    return strongest

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(input_file.read()))
    elif ARGS.test:
        print(solution(str(ARGS.test)))
    else:
        DEBUG = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""
        print(solution(DEBUG))
