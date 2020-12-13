""" Advent of code 2020 day 13/2 """

import math
from os import path
from functools import reduce


def chinese_remainder(n, a):
    """ 
    theory: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    code: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    """
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


class Schedule(object):
    def __init__(self, data):
        self.shuttle_ids = data

    def solve(self):
        dividers = [bus for _, bus in self.shuttle_ids]
        remainders = [bus - i for i, bus in self.shuttle_ids]
        return chinese_remainder(dividers, remainders)


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    shuttle_ids = [(i, int(id)) for i, id in enumerate(
        processed_data[1].split(',')) if id != 'x']
    return shuttle_ids


def solution(input_data):
    """ Solution to the problem """
    data = preprocess(input_data)
    solver = Schedule(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
