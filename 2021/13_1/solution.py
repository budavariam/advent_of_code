""" Advent of code 2021 day 13 / 1 """

import math
from os import path
import re



class Code(object):
    def __init__(self, lines):
        self.opoints = lines[0]
        self.points = lines[0]
        self.instr = lines[1]

    def fold(self, foldcnt):
        [dire, fpos] = self.instr[foldcnt]
        useX = False
        if dire == 'x':
            useX = True
            # fold left x
            pass
        elif dire == 'y':
            useX = False
            # fold up y
            pass
        newp = set()
        for [x,y] in self.points:
            if useX:
                if x < fpos:
                    newp.add((x,y))
                else:
                    newp.add((fpos - abs(fpos - x), y))
            else:
                if y < fpos:
                    newp.add((x,y))
                else:
                    newp.add((x, fpos - abs(fpos - y)))
        self.points = newp
        return len(self.points)

    def solve(self):
        print(self.points)
        print(self.instr)
        res = 0
        for i in range(0, 1):
            print("visiting", i)
            res += self.fold(i)
        return res


def preprocess(raw_data):
    pattern = re.compile(r'fold along ([xy])=(\d+)')
    processed_data = [[], []]
    isPoints = True
    for line in raw_data.split("\n"):
        if line == "":
            isPoints = False
            continue
        if isPoints:
            data = list(map(int, line.split(",")))
        else:
            match = re.match(pattern, line)
            data = [match.group(1), int(match.group(2))]
        processed_data[0 if isPoints else 1].append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
