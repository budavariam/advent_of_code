""" Advent of code 2017	day 8/1	"""

from argparse import ArgumentParser
from collections import defaultdict
import re

class Memory(object):
    """ Graph node that has a name, weight and children """

    @staticmethod
    def eval_cond(reg, sign, value):
        """ evaluate the condition """
        return {
            '<': lambda val: reg < val,
            '>': lambda val: reg > val,
            '>=': lambda val: reg >= val,
            '<=': lambda val: reg <= val,
            '==': lambda val: reg == val,
            '!=': lambda val: reg != val
        }[sign](value)

    def statement(self, match):
        """ run the statement line if the condition applies"""
        c_reg = self.registers[match.group(4)]
        c_dir = match.group(5)
        c_val = int(match.group(6))
        if self.eval_cond(c_reg, c_dir, c_val):
            m_reg = match.group(1)
            m_val = int(match.group(3)) * (1 if match.group(2) == 'inc' else -1)
            self.registers[m_reg] += m_val

    def largest(self):
        """ get the largest value from the registers """
        return max(self.registers.values())

    def __init__(self):
        """ Constructor for node from regexp data """
        self.registers = defaultdict(int)

def read_data(input_data):
    """ Create nodes from input data """
    pattern = re.compile(r'(\w+) (inc|dec) ((?:-?)\d+) if (\w+) (>|<|>=|<=|==|!=) ((?:-?)\d+)')
    return [re.match(pattern, line) for line in input_data.split("\n")]

def solution(input_data):
    """ Solution to the problem """
    data = read_data(input_data)
    memory = Memory()
    for match in data:
        memory.statement(match)
    return memory.largest()

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
