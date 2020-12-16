""" Advent of code 2020 day 16/1 """

import math
from os import path
import re


class Code(object):
    def __init__(self, data):
        self.rules = data[0]
        self.own = data[1]
        self.nearby = data[2]

    def solve(self):
        invalid_sum = 0
        for tickets in self.nearby:
            for ticket in tickets:
                if not any([rule.is_valid(ticket) for rule in self.rules]):
                    invalid_sum += ticket
        return invalid_sum


RULE_PARSE = re.compile(
    r'(?P<name>[^:]+): (?P<firstlow>\d+)-(?P<firsthigh>\d+) or (?P<secondlow>\d+)-(?P<secondhigh>\d+)')


class Rule(object):
    def __init__(self, data):
        self.a1 = int(data["firstlow"])
        self.a2 = int(data["firsthigh"])
        self.b1 = int(data["secondlow"])
        self.b2 = int(data["secondhigh"])

    def is_valid(self, num):
        return (self.a1 <= num <= self.a2) or (self.b1 <= num <= self.b2)


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    own = []
    rules = []
    nearby = []
    part = "RULES"
    for line in processed_data:
        if part == "RULES":
            match = RULE_PARSE.match(line)
            if match is not None:
                data = match.groupdict()
                rules.append(Rule(data))
            else:
                part = "MINE"
                continue
        elif part == "MINE":
            if "ticket" in line:
                continue
            own = list(map(int, line.split(",")))
            part = "NEARBY"
        elif part == "NEARBY":
            if line == "" or "ticket" in line:
                continue
            nearby.append(list(map(int, line.split(","))))

    return (rules, own, nearby)


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
