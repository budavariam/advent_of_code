""" Advent of code 2020 day 2/2 """

import math
from os import path
import re

line_matcher = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


class Validator(object):
    def __init__(self, line):
        match = re.match(line_matcher, line)
        self.posFirst = int(match.group(1)) - 1
        self.posSecond = int(match.group(2)) - 1
        self.char = match.group(3)
        self.text = match.group(4)

    def validate(self):
        firstCharMatch = self.text[self.posFirst] == self.char
        secondCharMatch = self.text[self.posSecond] == self.char
        return firstCharMatch ^ secondCharMatch


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
