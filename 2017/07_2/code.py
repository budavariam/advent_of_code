""" Advent of code 2017	day 7/2	"""

from argparse import ArgumentParser
from collections import deque
from functools import reduce
import re

class MemNode(object):
    """ Graph node that has a name, weight and children """

    def __init__(self, data):
        """ Constructor for node from regexp data """
        self.repr = data.group(0)
        self.name = data.group(1)
        self.weight = int(data.group(2))
        self.sum_weight = 0
        self.children = data.group(3).split(", ") if data.group(3) is not None else []

    def __repr__(self):
        """ Show the data in debugger as it is shown in the input data """
        return "{}[{}]".format(self.repr, self.sum_weight)

    def dict_data(self):
        """ Return the node to be easily put in a dict """
        return (self.name, self)

def read_data(input_data):
    """ Create nodes from input data """
    pattern = re.compile(r'(\w+) \((\d+)\)(?: -> (.*))?')
    return [MemNode(re.match(pattern, line)).dict_data() for line in input_data.split("\n")]

def get_top_node(data):
    """ The top node is what is not present in any other node's children list"""
    child_nodes = set()
    for key, node in data.items():
        [child_nodes.add(elem) for elem in node.children]
    return list(filter(lambda node_name: node_name not in child_nodes, data.keys()))

def build_tree(top, data):
    tree = data[top]
    if tree.children:
        tree.children = [build_tree(child, data) for child in tree.children]
        tree.sum_weight = tree.weight + reduce(lambda acc, x: acc+x.weight, tree.children, 0)
    print("{}".format(data[top]))
    return tree

def get_uneven_data(tree):

    return 0

def solution(input_data):
    """ Solution to the problem """
    data = dict(read_data(input_data))
    top_node = get_top_node(data)[0]
    #top_node = 'hlhomy'
    tree = build_tree(top_node, data)
    return get_uneven_data(tree)

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
        DEBUG = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
        print(solution(DEBUG))
