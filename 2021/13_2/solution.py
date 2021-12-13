""" Advent of code 2021 day 13 / 2 """

from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.opoints = lines[0]
        self.points = lines[0]
        self.instr = lines[1]

    def printmap(self):
        ly, lx = set(), set()
        for [x, y] in self.points:
            ly.add(y)
            lx.add(x)
        for y in range(min(ly), max(ly)+1):
            line = ""
            for x in range(min(lx), max(lx)+1):
                line += "#" if (x, y) in self.points else " "
            print(line)

    def fold(self, ins):
        [dire, fpos] = ins
        newp = set()
        for [x, y] in self.points:
            n_x, n_y = x, y
            if dire == 'x' and x > fpos:
                # fold left x
                n_x = fpos - abs(fpos - x)
            elif dire == 'y' and y > fpos:
                # fold up y
                n_y = fpos - abs(fpos - y)
            newp.add((n_x, n_y))
        self.points = newp
        return len(self.points)

    def solve(self):
        res = 0
        for ins in self.instr:
            res += self.fold(ins)
        self.printmap()
        return res


def preprocess(raw_data):
    pattern = re.compile(r'fold along ([xy])=(\d+)')
    processed_data = [[], []]
    resIndex = 0
    for line in raw_data.split("\n"):
        if line == "":
            resIndex = 1
            continue
        if resIndex == 0:
            # points
            data = list(map(int, line.split(",")))
        else:
            # instructions
            match = re.match(pattern, line)
            data = [match.group(1), int(match.group(2))]
        processed_data[resIndex].append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
