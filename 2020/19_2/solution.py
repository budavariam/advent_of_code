""" Advent of code 2020 day 19/2 """

import math
from os import path
import re
import sys


class MonsterMessage(object):
    def __init__(self, data):
        self.rules, self.messages = data
        self.cache = {}

    def create_matcher(self, current_rule):
        rulenum = current_rule["num"]
        cached = self.cache.get(rulenum)
        if cached is not None:
            return cached
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
            result = r"(" + '|'.join(nested_rules) + r")"
            self.cache[rulenum] = result
            return result

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


def generate_recursive_rules(limit):
    """
    Note this is not a general solution for ALL possible recursive calls.

    The generated inputs have recursive rules appear only at root in `0: 8 11`.

    Thus I only need to create a rule that has extracted recursion to some levels until I see a difference on matched number in my results.
    """

    return [
        # 8: 42 | 42 8 - recursion creates the pattern: 42 | 42 42 | 42 42 42 etc...
        f"8: {' | '.join([('42 ' * x).strip() for x in range(1, limit + 1)])}",
        # 11: 42 31 | 42 11 31 - recursion creates the pattern: 42 31 | 42 42 31 31 | 42 42 42 31 31 31 etc...
        f"11: {' | '.join([('42 ' * x).strip() + ' ' + ('31 ' * x).strip() for x in range(1, limit + 1)])}"
    ]


def preprocess(raw_data, recursion_limit):
    update_rules = generate_recursive_rules(recursion_limit)
    processed_data = raw_data.split("\n")
    index = None
    rules = {}

    def parse_line(line):
        matches = PARSE_RULE.match(line)
        if matches is None:
            print("Failed to parse rule!", line)
            sys.exit(1)
        rulenum = int(matches.group(1))
        rule_raw_data = matches.group(2)
        rule_data = None
        if rule_raw_data[0] == '"':
            rule_data = {
                "num": rulenum,
                "type": "text",
                "value": rule_raw_data[1:-1]
            }
        else:
            nested_rules = list(
                map(lambda x: list(map(int, x.strip().split(" "))), rule_raw_data.split("|")))
            rule_data = {
                "num": rulenum,
                "type": "nested",
                "value": nested_rules
            }
        rules[rulenum] = rule_data

    for i, line in enumerate(processed_data):
        if line == "":
            index = i
            break
        parse_line(line)
    for line in update_rules:
        parse_line(line)

    messages = processed_data[index:]
    return (rules, messages)


def solution(raw_data):
    """ Solution to the problem """
    recursion_limit = 5  # hardcoded value based on empirical exploration
    data = preprocess(raw_data, recursion_limit)
    solver = MonsterMessage(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
