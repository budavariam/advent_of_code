""" Advent of code 2020 day 4/2 """

import logging
import math
from os import path
import re

record_splitter = re.compile(' |\n')

# Field info:
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def height_validator(x):
    match = re.match(r'^(\d+)(cm|in)$', x)
    if match is not None:
        value = match.group(1)
        unit = match.group(2)
        if unit == "cm":
            return 150 <= int(value) <= 193 
        elif unit == "in":
            return 59 <= int(value) <= 76 

expected_fields = [
    {"key": 'byr', "validator": lambda x:
        re.match(r'^\d{4}$', x) is not None and (1920 <= int(x) <= 2002)},  # (Birth Year)
    {"key": 'iyr', "validator": lambda x: \
        re.match(r'^\d{4}$', x) is not None and (2010 <= int(x) <= 2020)},  # (Issue Year)
    {"key": 'eyr', "validator": lambda x: \
        re.match(r'^\d{4}$', x) is not None and (2020 <= int(x) <= 2030)},  # (Expiration Year)
    {"key": 'hgt', "validator": height_validator},  # (Height)
    {"key": 'hcl', "validator": lambda x: \
        re.match(r'^#[a-f0-9]{6}$', x) is not None},  # (Hair Color)
    {"key": 'ecl', "validator": lambda x: \
        re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', x) is not None},  # (Eye Color)
    {"key": 'pid', "validator": lambda x: \
        re.match(r'^\d{9}$', x) is not None},  # (Passport ID)
    # {"key": 'cid', "validator": lambda x: \
    #     True},  # (Country ID),
]


class PassportProcessor(object):
    def __init__(self, records):
        self.records = records

    def validate_field(self, record, field):
        result = field["key"] in record and field["validator"](record[field["key"]])
        # print(result, record)
        return result

    def solve(self):
        result = 0
        for record in self.records:
            result += 1 if all([self.validate_field(record, field) for field in expected_fields]) else 0
        return result


def solution(data):
    """ Solution to the problem """
    # split records by empty lines, split fields by ":"-s, create a list of dictionaries from the records.
    lines = [{key: value for [key, value] in [field.split(
        ":") for field in record_splitter.split(record)]} for record in data.split("\n\n")]
    solver = PassportProcessor(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
