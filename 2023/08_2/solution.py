""" Advent of code 2023 day 08 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import deque
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        steps = 0
        location = {k: (k, False) for k in self.lines["start_nodes"]}
        found_ends = {k: None for k in self.lines["start_nodes"]}
        movement = []
        found_all = False
        while not found_all:
            # get next direction feed location if empty
            if len(movement) == 0:
                movement = deque(self.lines["movement"])
            direction = movement.popleft()
            # mark a step has happened
            steps += 1

            # collect reached ends, and assume each start point can reach to a single end
            new_location = {}
            for curr, (start_node, found) in location.items():
                step_to = self.lines["nodes"][curr][0 if direction == "L" else 1]
                found = step_to in self.lines["end_nodes"]
                if found:
                    # print(f"[{curr}] at '{step_to}' #{steps}")
                    found_ends[start_node] = (step_to, steps)
                    found_all = all(found_ends.values())
                new_location[step_to] = (start_node, found)
            location = new_location
        # now that I have the sizes of the loops, I can calculate the point where each of those overlap with a least common multiplier
        return math.lcm(*[x for _, (_, x) in found_ends.items()])


@utils.profiler
def preprocess(raw_data):
    "AAA = (BBB, CCC)"
    pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    lines = raw_data.split("\n")
    movement = lines[0]
    nodes = {}
    processed_data = {
        "movement": movement,
        "nodes": nodes,
        "start_nodes": set([]),
        "end_nodes": set([]),
    }
    for line in lines[2:]:
        match = re.match(pattern, line)
        curr = match.group(1)
        if curr[2] == "A":
            processed_data["start_nodes"].add(curr)
        if curr[2] == "Z":
            processed_data["end_nodes"].add(curr)
        processed_data["nodes"][curr] = (match.group(2), match.group(3))
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
