""" Advent of code 2022 day 03 / 2 """
from os import path


def calcprio(x):
    if x.islower():
        res = ord(x) - ord("a") + 1
        return res
    else:
        res = ord(x) - ord("A") + 1 + 26
        return res


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        res = 0
        for i in range(0, len(self.lines), 3):
            a, b, c = self.lines[i : i + 3]
            groupbadge = (set(a).intersection(set(b)).intersection(set(c))).pop()
            res += calcprio(groupbadge)
        return res


def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
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
