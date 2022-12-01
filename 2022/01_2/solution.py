""" Advent of code 2022 day 01 / 1 """

from os import path


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        res = []
        for line in self.lines:
            res.append(sum(line))
        return sum(sorted(res, reverse=True)[0:3])


def preprocess(raw_data):
    processed_data = []
    data = []
    line = ''
    for line in raw_data.split("\n"):
        if line != '':
            data.append(int(line))
        elif line == '':
            processed_data.append(data)
            data = []
    # add the last batch
    if line != '':
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
