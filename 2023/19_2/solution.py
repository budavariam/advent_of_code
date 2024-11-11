""" Advent of code 2023 day 19 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict, deque
import utils
from typing import Optional

ACCEPT = "A"
REJECT = "R"

MIN_VALUE = 1
MAX_VALUE = 4000


class Condition:
    def __init__(self, condition):
        self.raw = condition
        self.variable = condition[0]
        self.operator = condition[1]
        self.value = int(condition[2:])

    def __repr__(self):
        return self.raw

    def get_info(self, flip=False) -> tuple[str, str, int, Optional["Interval"]]:
        other = {"<": ">=", ">": "<="}
        op = other[self.operator] if flip else self.operator
        interval = None
        if op == "<":
            interval = Interval(
                self.variable, MIN_VALUE, max(MIN_VALUE, self.value - 1)
            )
        elif op == ">":
            interval = Interval(
                self.variable, min(MAX_VALUE, self.value + 1), MAX_VALUE
            )
        elif op == "<=":
            interval = Interval(self.variable, MIN_VALUE, max(MIN_VALUE, self.value))
        elif op == ">=":
            interval = Interval(self.variable, min(MAX_VALUE, self.value), MAX_VALUE)
        return (self.variable, op, self.value, interval)


class Node:
    def __init__(self, wf_name="", parent=None, condition=None, l=None, r=None) -> None:
        self.wf_name = wf_name
        self.condition = None if condition is None else Condition(condition)
        self.parent: Optional["Node"] = parent
        self.l: Optional["Node"] = l
        self.r: Optional["Node"] = r

    def is_left_child(self) -> bool:
        if self.parent is None:
            return True
        return self == self.parent.l

    def __repr__(self):
        if self.wf_name in [ACCEPT, REJECT]:
            return f'"{self.wf_name}"'
        return f'{{"{self.wf_name}({self.condition})": {{"l":{self.l}, "r":{self.r}}}}}'


class Interval:
    def __init__(self, variable, start, end) -> None:
        self.var = variable
        self.start = start
        self.end = end

    def intersect(self, other: "Interval") -> "Interval":
        if other is None:
            return self
        sorted_s = sorted([self.start, other.start])
        sorted_e = sorted([self.end, other.end])
        s = max(sorted_s)
        e = min(sorted_e)
        res = None
        if e > s:
            res = Interval(self.var, 0, 0)
        res = Interval(self.var, s, e)
        # print(f"Intersection between {self} - {other} is {res}")
        return res

    def __len__(self):
        return abs(self.end - self.start) + 1

    def __repr__(self):
        return f"({self.var}:{self.start}-{self.end})[{self.__len__()}]"


class Code(object):
    def __init__(self, lines):
        self.workflows = lines["workflows"]
        self.accept_nodes: list[Node] = []

    def parse_workflow(self, label: str) -> Node:
        root = Node(label)
        if label == ACCEPT:
            # print("HAY", label)
            n = Node(wf_name=ACCEPT, parent=root)
            self.accept_nodes.append(n)
            return n

        elif label == REJECT:
            return Node(wf_name=REJECT)
        rules = self.workflows[label]
        prev = root
        curr = root
        for i, rule in enumerate(rules):
            if i > 0:
                curr = Node(wf_name=label)

            if len(rule) == 2:
                condition, iftrue = rule
                curr.condition = Condition(condition)
                left_child = self.parse_workflow(iftrue)
                left_child.parent = curr
                curr.l = left_child
                if i > 0:
                    prev.r = curr
                    curr.parent = prev
                prev = curr
            elif len(rule) == 1:
                label = rule[0]
                if label == ACCEPT or label == REJECT:
                    # leaf node
                    if i > 0:
                        curr = self.parse_workflow(label)
                        prev.r = curr
                        curr.parent = prev
                    prev = curr
                else:
                    # jump
                    child = self.parse_workflow(label)
                    child.parent = curr
                    curr = child
                    if i > 0:
                        prev.r = curr
                        curr.parent = prev
                    prev = curr
        return root

    def calc_conditions(self, operation_graph: Node, start_points: list[Node]):
        res: list[list[Interval]] = []
        for i, start in enumerate(start_points):
            # print(i)
            flat = []
            curr = start
            while curr.parent is not None:
                cond = None
                if curr.condition is not None:
                    cond = curr.condition
                flat.append((curr.wf_name, cond, curr.is_left_child()))
                curr = curr.parent
            flat.append((curr.wf_name, curr.condition, curr.is_left_child()))
            rev = flat[::-1]
            sub_res = []
            for p_value, c_value in zip(rev, rev[1:]):
                is_left_node = c_value[2]
                if p_value[1] is not None:
                    cc: Condition = p_value[1]
                    condition = cc.get_info(not is_left_node)
                    if condition[3] is not None:
                        sub_res.append(condition[3])
                else:
                    condition = None
                name = p_value[0]
                # print(name, condition)

            res.append(sub_res)
        # pprint(res)
        result = 0
        debug_intervals = []
        for approved_intervals in res:
            intervals = {
                "x": Interval("x", MIN_VALUE, MAX_VALUE),
                "m": Interval("m", MIN_VALUE, MAX_VALUE),
                "a": Interval("a", MIN_VALUE, MAX_VALUE),
                "s": Interval("s", MIN_VALUE, MAX_VALUE),
            }
            for iv in approved_intervals:
                if iv.var in intervals:
                    intervals[iv.var] = iv.intersect(intervals[iv.var])
            product = math.prod(map(len, intervals.values()))
            #print(list(map(len, intervals.values())), product)
            result += product
            debug_intervals.append(intervals)
        #pprint(debug_intervals)
        return result

    def solve(self):
        operation_graph = self.parse_workflow("in")
        #print(operation_graph)
        result = self.calc_conditions(operation_graph, self.accept_nodes)
        return result


@utils.profiler
def preprocess(raw_data):
    workflow_pattern = re.compile(r"(\w+)\{(.*)\}")
    processed_data = {
        "workflows": {},
        "parts": [],
    }
    workflows, parts = raw_data.split("\n\n")
    for line in workflows.split("\n"):
        match = re.match(workflow_pattern, line)
        processed_data["workflows"][match.group(1)] = deque(
            [x.split(":") for x in match.group(2).split(",")]
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
