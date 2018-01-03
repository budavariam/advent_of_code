""" Advent of code 2017 day 23/1 """
from argparse import ArgumentParser
from copy import deepcopy
import re
from collections import defaultdict

def read_data(data):
    """ Read data blocks """
    pattern = re.compile(r'(\d+)/(\d+)')
    edges = defaultdict(list)
    for line in data.split('\n'):
        matches = re.match(pattern, line)
        val_a = int(matches.group(1))
        val_b = int(matches.group(2))
        edge = Edge(line, sorted([val_a, val_b]), (val_a + val_b))
        edges[val_a].append(edge)
        if val_a != val_b:
            edges[val_b].append(edge)
    return edges

class Edge(object):
    """ Graph edge """
    def __init__(self, line, ends, strength):
        """ Constructor """
        self.val_l = ends[0]
        self.val_g = ends[1]
        self.ends = set(ends)
        self.strength = strength
        self.repr = line

    def __repr__(self):
        """ Reprecentation of the block """
        return "{}: {}".format(self.repr, self.strength)

    def other(self, connect):
        """ Return the other end of the edge """
        return list(self.ends.difference([connect]))[0] if len(self.ends) == 2 else connect

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
            visited.add(current_edge.repr)
            strength += current_edge.strength
            connect = current_edge.other(connect)
            #debug.append((strength, current_edge))
        available = [edge for edge in self.edges[connect] if not edge.repr in visited]
        empty = len(available) == 0
        if empty:
            print(strength)
            return strength
        return max(self.find(connect, edge, deepcopy(visited), strength) for edge in available)

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
        DEBUG = """25/13
4/43
42/42
39/40
17/18
30/7
12/12
32/28
9/28
1/1
16/7
47/43
34/16
39/36
6/4
3/2
10/49
46/50
18/25
2/23
3/21
5/24
46/26
50/19
26/41
1/50
47/41
39/50
12/14
11/19
28/2
38/47
5/5
38/34
39/39
17/34
42/16
32/23
13/21
28/6
6/20
1/30
44/21
11/28
14/17
33/33
17/43
31/13
11/21
31/39
0/9
13/50
10/14
16/10
3/24
7/0
50/50"""

        ASD = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""
        print(solution(ASD))
