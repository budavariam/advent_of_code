""" Advent of code 2021 day 03/2 """

import math
from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def bit_hist(self, lns):
        bits = [[0, 0] for x in range(12)]
        gamma = ""  # most common
        epsilon = ""  # least common
        for line in lns:
            for num, bit in enumerate(line):
                bits[num][int(bit)] += 1
        for [zero, one] in bits:
            if zero > one:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        return bits

    def src(self, lines, ftype):
        lns = [x for x in lines]
        while len(lns) > 0:
            for i in range(12):
                # print(ftype, len(lns), i)
                bits = self.bit_hist(lns)
                bitin = bits[i] # cnt of zero and 1
                if bitin[0] > bitin[1]:
                    # mostcommon is 0
                    whattokeep = '0' if ftype == 'o' else '1'
                    lns = [x for x in lns if x[i] == whattokeep]
                    pass
                elif bitin[0] < bitin[1]:
                    whattokeep = '1' if ftype == 'o' else '0'
                    lns = [x for x in lns if x[i] == whattokeep]
                    pass
                    # mostcommon is 1
                else:
                    whattokeep = '1' if ftype == 'o' else '0'
                    lns = [x for x in lns if x[i] == whattokeep]
                    pass
                    # mostcommon eq
                if len(lns) == 0:
                    raise 'shouldnotcomehere'
                if len(lns) == 1:
                    return lns[0]

    def solve(self):
        # print(self.lines)
        o = int(self.src(self.lines, 'o'), base=2)
        c = int(self.src(self.lines, 'c'), base=2)
        life_supp = o * c

        return life_supp


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
