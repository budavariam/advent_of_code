""" Advent of code 2020 day 16/2 """

import math
from os import path
import re
from collections import defaultdict


class Code(object):
    def __init__(self, data):
        self.rules = data[0]
        self.own = data[1]
        self.nearby = data[2]

    def eliminate(self, possibilities):
        """ figure out what column is paired with what rule by elimination """
        matrix = defaultdict(set)
        # transpose the matrix to 
        for index, value in possibilities.items():
            for item in value:
                matrix[item].add(index)
        result_mapping = {}
        condition = True
        while condition:
            # print("----------")
            # for i in matrix.items():
            #     print(i)

            # Find a value to eliminate
            value_to_clear = None
            remove_index = None
            for i, values in matrix.items():
                if len(values) == 1:
                    value_to_clear = list(values)[0]
                    remove_index = i
                    result_mapping[value_to_clear] = i
                    break
            # Elominate its line
            del matrix[remove_index]
            # Eliminate the value from all other items
            matrix = {key: value.difference(
                set([value_to_clear])) for key, value in matrix.items()}
            if len(matrix) == 0:
                condition = False
            # print(result_mapping)
        return result_mapping

    def calc_result(self, own, rules, mapping):
        result = 1
        for rule_id, rule in enumerate(rules):
            if rule.is_departure:
                result *= own[mapping[rule_id]]
        return result

    def solve(self):
        possibilities = {index: set(range(len(self.rules)))
                         for index in range(len(self.rules))}
        for ticket in self.nearby:
            should_discard = False
            temp_possibility = defaultdict(set)
            for row_index, rowitem in enumerate(ticket):
                invalid_value = True
                for rule_index, rule in enumerate(self.rules):
                    if rule.is_valid(rowitem):
                        temp_possibility[rule_index].add(row_index)
                        invalid_value = False
                if invalid_value == True:
                    should_discard = True
                    break
            if not should_discard:
                for rule_id, possible_rows in temp_possibility.items():
                    possibilities[rule_id] = possibilities[rule_id].intersection(
                        possible_rows)
        mapping = self.eliminate(possibilities)
        return self.calc_result(self.own, self.rules, mapping)


RULE_PARSE = re.compile(
    r'(?P<name>[^:]+): (?P<firstlow>\d+)-(?P<firsthigh>\d+) or (?P<secondlow>\d+)-(?P<secondhigh>\d+)')


class Rule(object):
    def __init__(self, data):
        self.is_departure = "departure" in data["name"]
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
