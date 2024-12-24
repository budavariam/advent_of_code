""" Advent of code 2024 day 22 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def mix_and_prune(self, secret_num, new_value):
        """To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)

        To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
        """
        return (secret_num ^ new_value) % 16777216

    def next_secret_num(self, secret_num):
        """In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:

        Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
        Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
        Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
        """
        res = secret_num * 64
        secret_num = self.mix_and_prune(secret_num, res)
        res = math.floor(secret_num / 32)
        secret_num = self.mix_and_prune(secret_num, res)
        res = secret_num * 2048
        secret_num = self.mix_and_prune(secret_num, res)
        return secret_num

    def solve(self):
        # pprint(self.lines)
        result = 0
        for n in self.lines:
            for _ in range(2000):
                n = self.next_secret_num(n)
            result += n
        return result


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = int(line)
        processed_data.append(data)
    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
