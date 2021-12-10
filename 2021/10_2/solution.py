""" Advent of code 2021 day 10 / 2 """

import math
from os import path
from collections import defaultdict, deque
import re
p = {
    "()": 1,
    "[]": 2,
    "kk": 3,
    "<>": 4,
}
m = {
    "(": "()",
    "[": "[]",
    "{": "kk",
    "<": "<>",
    ")": "()",
    "]": "[]",
    "}": "kk",
    ">": "<>",
}

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        scrs = []
        for line in self.lines:
            score = 0
            chk = deque([])
            opening = {
                "(": 0,
                "[": 0,
                "{": 0,
                "<": 0,
            } 
            closed = {
                ")": 0,
                "]": 0,
                "}": 0,
                ">": 0,
            }
            r = defaultdict(int)
            for c in line:
                # corrupted = False
                if c in opening.keys():
                    opening[c] += 1
                    r[m[c]] += 1
                    chk.append(c)
                elif c in closed.keys():
                    closed[c] += 1
                    r[m[c]] -= 1
                    shouldclose = chk.pop()
                    if m[shouldclose] != m[c]:
                        # illcars.append(c)
                        # corrupted = True
                        break
            else:
                while len(chk) > 0:
                    nex = chk.pop()
                    score *= 5
                    score += p[m[nex]]
                scrs.append(score)


            # print(line, r, corrupted)
            # print("point",illcars)
            # mid = list(sorted(scrs))[math.ceil(len(scrs)/2) -1]
        return sorted(scrs)[len(scrs)//2] # sum([p[ca] for ca in illcars])
            

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
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
