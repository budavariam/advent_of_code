""" Advent of code 2017	day 7/1	"""

from argparse import ArgumentParser
import re

class MemNode(object):
    """ Graph node that has a name, weight and children """

    def __init__(self, data):
        """ Constructor for node from regexp data """
        self.repr = data.group(0)
        self.name = data.group(1)
        self.weight = data.group(2)
        self.children = data.group(3).split(", ") if data.group(3) is not None else []

    def __repr__(self):
        """ Show the data in debugger as it is shown in the input data """
        return self.repr

def read_data(input_data):
    """ Create nodes from input data """
    pattern = re.compile(r'(\w+) \((\d+)\)(?: -> (.*))?')
    return [MemNode(re.match(pattern, line)) for line in input_data.split("\n")]

def get_top_node(data):
    """ The top node is what is not present in any other node's children list"""
    child_nodes = set()
    for node in data:
        [child_nodes.add(elem) for elem in node.children]
    return list(filter(lambda node: node.name not in child_nodes, data))

def solution(input_data):
    """ Solution to the problem """
    data = read_data(input_data)
    top_node = get_top_node(data)
    return [node.name for node in top_node]

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
