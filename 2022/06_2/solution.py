""" Advent of code 2022 day 06 / 2 """

from os import path
from collections import deque


class Code(object):
    def __init__(self, lines):
        self.lines = lines[0]

    def solve(self):
        print(self.lines)
        result = 0
        win_size = 14
        last4 = deque(self.lines[0:win_size])
        for i, char in enumerate(self.lines[win_size:]):
            # print(last4, char, i, i + win_size)
            if len(set(last4)) == win_size:
                return i + win_size
            else:
                last4.popleft()
                last4.append(char)
        return result


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
