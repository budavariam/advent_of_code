""" Advent of code 2022 day 05 / 2 """

import math
from os import path
import re
from collections import defaultdict


def is_empty(item):
    if item == '':
        return False
    return True

def get_result(crates):
    return ''.join([x[-1] for x in crates])

def move(inst, data):
    crts = data
    count, frm, to = inst
    tmp = []
    for _ in range(count):
        popped = data[frm - 1].pop()
        tmp.append(popped)
    data[to - 1 ].extend(tmp[::-1])
    return crts

class Code(object):
    def __init__(self, input_data):
        self.raw_crates = input_data[0]
        self.crates = list(map(list, zip(*input_data[0])))
        self.crates = [list(filter(is_empty, x[::-1])) for x in self.crates]
        self.instructions = input_data[1]

    def solve(self):
        print(self.crates)
        for inst in self.instructions:
            move(inst, self.crates)
        return get_result(self.crates)


def preprocess(raw_data):
    pattern_instr = re.compile(r'move (\d+) from (\d+) to (\d+)')
    lines = raw_data.split("\n")
    i = 0
    crates = []
    instructions = []
    for line in lines:
        n = 4
        crts=[line[i:i+n].strip().strip('[]') for i in range(0, len(line), n)]
        i+=1
        if line == '':
            break
        if crts[0] == '1':
            continue
        crates.append(crts)
    for line in lines[i:]:
        match = re.match(pattern_instr, line)
        data = [int(x) for x in [match.group(1), match.group(2), match.group(3)]]
        instructions.append(data)
    return (crates, instructions)


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
