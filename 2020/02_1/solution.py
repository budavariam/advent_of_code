""" Advent of code 2020 day 2/1 """

from argparse import ArgumentParser
import math
from os import path
import re

line_matcher = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


class Validator(object):
    def __init__(self, line):
        match = re.match(line_matcher, line)
        self.minNum = int(match.group(1))
        self.maxNum = int(match.group(2))
        self.char = match.group(3)
        self.text = match.group(4)

    def validate(self):
        char_number_to_check = self.text.count(self.char)
        return (char_number_to_check >= self.minNum) and (char_number_to_check <= self.maxNum)

def solution(data):
    """ Solution to the problem """
    lines = data.split("\n")
    result = 0
    for line in lines:
        pw_validator = Validator(line)
        if pw_validator.validate():
            result += 1

    return result


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
