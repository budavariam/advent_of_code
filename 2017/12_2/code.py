""" Advent of code 2017 day 12/2 """
from argparse import ArgumentParser
import re
from collections import deque

class Node(object):
    """ Node of the network """
    def __init__(self, name, connections):
        """ Constructor of the node """
        self.name = name
        self.connections = [] if not connections else connections.split(', ')

class Network(object):
    """ Representation of the network """
    def __init__(self, data):
        """ Constructor of the node """
        self.nodes = self.parse_input(data)

    @staticmethod
    def parse_input(data):
        """ load the graph """
        pattern = re.compile(r'(\d+) <-> (\d+(?:, \d+)*)')
        nodes = {}
        for line in data.split('\n'):
            match = re.match(pattern, line)
            name = match.group(1)
            nodes[name] = Node(name, match.group(2))
        return nodes

    def contains(self, name):
        """ Return the group that contains the id """
        name_to_visit = deque(self.nodes[name].connections)
        name_visited = set(name)
        while name_to_visit:
            current = name_to_visit.popleft()
            if current not in name_visited:
                name_visited.add(current)
                name_to_visit.extend(self.nodes[current].connections)
        return name_visited

    def count_groups(self):
        """ Count the distinct networks amongst the nodes """
        all_nodes = set(self.nodes.keys())
        visited_nodes = set()
        group_count = 0
        for name in all_nodes:
            if name not in visited_nodes:
                group = self.contains(name)
                visited_nodes.update(group)
                group_count += 1
        return group_count

def solution(input_data):
    """ Solution to the problem """
    return Network(input_data).count_groups()

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
        DEBUG = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""
        print(solution(DEBUG))
