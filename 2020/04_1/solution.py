""" Advent of code 2020 day 4/1 """

import logging
import math
from os import path
import re

record_splitter = re.compile(' |\n')
expected_fields = [
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
    # 'cid', # (Country ID),
]

class PassportProcessor(object):
    def __init__(self, records):
        self.records = records

    def solve(self):
        result = 0
        for record in self.records:
            result += 1 if all([fieldname in record for fieldname in expected_fields]) else 0
        return result

def solution(data):
    """ Solution to the problem """
    # split records by empty lines, split fields by ":"-s, create a list of dictionaries from the records.
    lines = [{ key: value for [key, value] in [field.split(":") for field in record_splitter.split(record)]} for record in data.split("\n\n")]
    solver = PassportProcessor(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
