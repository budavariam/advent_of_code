""" Advent of code 2017	day 7/2	"""

from argparse import ArgumentParser
from collections import deque, defaultdict
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

def fix_data(data):
    """ Fix the wrongly weighted element """
    histogram = defaultdict(int)
    for elem in data:
        histogram[elem.sum_weight] += 1
    single_value = list(filter(lambda elem: elem[1] == 1, histogram.items()))[0][0]
    other_values = list(filter(lambda elem: elem[1] != 1, histogram.items()))[0][0]
    single_index, single_elem = list(filter(lambda elem: elem[1].sum_weight == single_value, enumerate(data)))[0]
    difference = single_value - other_values
    single_fixed_weight = single_elem.weight - difference
    print("{}'s weight should be fixed to: {}".format(single_elem.name, single_fixed_weight))
    fixed_data = data
    single_elem.weight = single_fixed_weight
    single_elem.sum_weight -= difference
    fixed_data[single_index] = single_elem
    return fixed_data

def build_tree(top, data):
    """ Build a tree from the given data """
    tree = data[top]
    tree.sum_weight = tree.weight
    if tree.children:
        new_children = []
        child_sizes = []
        for child in tree.children:
            child_tree = build_tree(child, data)
            new_children.append(child_tree)
            child_sizes.append(child_tree.sum_weight)
        if len(set(child_sizes))>1:
            new_children = fix_data(new_children)                
        tree.children = new_children
        tree.sum_weight = reduce(lambda acc, elem: elem.sum_weight + acc, new_children, tree.weight)
    #print("{}".format(data[top]))
    return tree

def solution(input_data):
    """ Solution to the problem """
    data = dict(read_data(input_data))
    top_node = get_top_node(data)[0]
    tree = build_tree(top_node, data)
    return tree

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
