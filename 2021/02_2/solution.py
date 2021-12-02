""" Advent of code 2021 day 02/2 """

from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        hor = 0
        dep = 0
        aim = 0
        # print(self.lines)
        for [direct, num] in self.lines:
            if direct == 'forward':
                hor += num
                dep += aim*num
            elif direct == 'down':
                aim += num
            elif direct == 'up':
                aim -= num
        res = hor * dep
        return res

def preprocess(raw_data):
    pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        processed_data.append([match.group(1), int(match.group(2))])
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
