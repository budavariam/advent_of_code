""" Advent of code 2020 day 19/1 """

import math
from os import path
import re
import sys


class MonsterMessage(object):
    def __init__(self, data):
        self.rules, self.messages = data

    def create_matcher(self, current_rule):
        if current_rule["type"] == "text":
            return current_rule["value"]
        else:
            options = current_rule["value"]
            nested_rules = []
            for nested_rule_list in options:
                evaluated_rule = ""
                for nested_rule in nested_rule_list:
                    next_rule = self.create_matcher(self.rules[nested_rule])
                    evaluated_rule += next_rule
                nested_rules.append(r"(" + evaluated_rule + r")")
            return r"(" + '|'.join(nested_rules) + r")"

    def solve(self):
        start_rule = 0
        raw_matcher = r"^" + self.create_matcher(self.rules[start_rule]) + r"$"
        # print("Matcher", raw_matcher)
        matcher = re.compile(raw_matcher)
        result = 0
        for line in self.messages:
            match_result = matcher.match(line)
            if match_result is not None:
                # print("Matched: ", match_result)
                result += 1
        return result


PARSE_RULE = re.compile(r'(\d+): (.*)')


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    index = None
    rules = {}
    for i, line in enumerate(processed_data):
        if line == "":
            index = i
            break
        matches = PARSE_RULE.match(line)
        if matches is None:
            print("Failed to parse rule!", line)
            sys.exit(1)
        rulenum = int(matches.group(1))
        rule_raw_data = matches.group(2)
        rule_data = None
        if rule_raw_data[0] == '"':
            rule_data = {"type": "text", "value": rule_raw_data[1:-1]}
        else:
            nested_rules = list(
                map(lambda x: list(map(int, x.strip().split(" "))), rule_raw_data.split("|")))
            rule_data = {"type": "nested", "value": nested_rules}
        rules[rulenum] = rule_data
    messages = processed_data[index:]
    return (rules, messages)


def solution(raw_data):
    """ Solution to the problem """
    data = preprocess(raw_data)
    solver = MonsterMessage(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
