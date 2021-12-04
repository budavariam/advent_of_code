""" Advent of code 2021 day 04/1 """

import math
from os import path
import re


class Board(object):
    def __init__(self, lines):
        self.lines = lines
        self.cols = [list(map(int, row.split())) for row in lines]
        self.rows = [list(i) for i in zip(*self.cols)]
        self.nums = set([])

    def __repr__(self) -> str:
        return ", ".join(sorted(self.nums))

    def call_num(self, num) -> bool:
        self.nums.add(num)

    def won(self) -> bool:
        res = False
        for line in self.cols:
            isfull = all([n in self.nums for n in line])
            if isfull:
                return True
            
        for line in self.rows:
            isfull = all([n in self.nums for n in line])
            if isfull:
                return True
        return res

    def unmarkedsum(self) -> bool:
        res = 0
        for line in self.cols:
            for n in line:
                if n not in self.nums:
                    res += n
        return res


class Code(object):
    def __init__(self, lines):
        self.numbers = list(map(int,lines[0].split(",")))
        self.boards = []
        for i in range(2, len(lines), 6):
            self.boards.append(Board(lines[i:i+5]))

    def solve(self):
        print(self.numbers, self.boards)
        for num in self.numbers:
            for b in self.boards:
                b.call_num(num)
                if b.won():
                    return b.unmarkedsum() * num


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
