""" Advent of code 2022 day 03 / 2 """

import math
from os import path
import re

def calcprio(x):
    if x.islower():
        res = ord(x) - ord('a') + 1
        print("a", res)
        return res
    else:
        res = ord(x) - ord('A') + 1 + 26
        print("A", res)
        return res

    # return ord(x) - (ord('a') if x.islower() else ord('A') + 26)

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def calcprio(self, lines):
        result = 0
        for line in lines:
            comp_1 = line[:len(line)//2]
            comp_2 = line[len(line)//2:]
            contents1 = set(comp_1)
            contents2 = set(comp_2)
            matching = contents2.intersection(contents1)
            print(matching)
            match = [calcprio(x) for x in matching]
            print(match)
            result += sum(match)
        return result

    def solve(self):
        groups = {}
        g_i = 0
        res = 0
        for i in range(0, len(self.lines), 3):
            a,b,c =self.lines[i:i+3]
            sa, sb,sc = set(a),set(b),set(c)
            groupbadge = sa.intersection(sb).intersection(sc)
            print(groupbadge)
            groups[g_i] = (groupbadge, sa,sb,sc)
            g_i+=1
            p = calcprio(groupbadge.pop())
            res += p
        print(groups)
        return res
        

def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append(data)
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
