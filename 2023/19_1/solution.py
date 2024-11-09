""" Advent of code 2023 day 19 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils
from operator import lt, gt

ACCEPT = "A"
REJECT = "R"


class Code(object):
    def __init__(self, lines):
        self.parts = lines["parts"]
        self.workflows = lines["workflows"]

    def run_workflow(self, part, wf_name):
        # print(f"running workflow '{wf_name}' for {part}")
        if wf_name == ACCEPT:
            return True
        elif wf_name == REJECT:
            return False
        for rule in self.workflows[wf_name]:
            # print(f"  {self.workflows[wf_name]}")
            if len(rule) == 2:
                # it has a condition to evaluate
                condition, iftrue = rule
                op = lt if condition[1] == "<" else gt
                res = op(part[condition[0]], int(condition[2:]))
                # print(f"Condition: {condition} -> {res}")
                if res:
                    return self.run_workflow(part, iftrue)
                else:
                    continue
            elif rule[0] == ACCEPT:
                return True
            elif rule[0] == REJECT:
                return False
            else:
                return self.run_workflow(part, rule[0])
        return None

    def solve(self):
        # pprint(self.parts)
        # pprint(self.workflows)
        result = 0
        for p in self.parts:
            verdict = self.run_workflow(p, "in")
            # print("VERDICT:", verdict)
            if verdict:
                result += p["x"] + p["m"] + p["a"] + p["s"]
        return result


@utils.profiler
def preprocess(raw_data):
    workflow_pattern = re.compile(r"(\w+)\{(.*)\}")
    part_pattern = re.compile(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
    processed_data = {
        "workflows": {},
        "parts": [],
    }
    workflows, parts = raw_data.split("\n\n")
    for line in workflows.split("\n"):
        match = re.match(workflow_pattern, line)
        processed_data["workflows"][match.group(1)] = [
            x.split(":") for x in match.group(2).split(",")
        ]

    for line in parts.split("\n"):
        match = re.match(part_pattern, line)
        processed_data["parts"].append(
            {
                "x": int(match.group(1)),
                "m": int(match.group(2)),
                "a": int(match.group(3)),
                "s": int(match.group(4)),
            }
        )
    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read()))
