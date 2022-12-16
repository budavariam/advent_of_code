""" Advent of code 2022 day 16 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils

P_NAME=0
P_FLOW_RATE=1
P_CONNECTIONS=2


def step_floydwarshal(
    valves, steps, start_valve, time_remaining, state_bitmap, state, flow, answer
):
    """https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/"""
    answer[state] = max(answer.get(state, 0), flow)
    for curr_valve in valves:
        minutes = time_remaining - steps[start_valve][curr_valve] - 1
        if (state_bitmap[curr_valve] & state) or (minutes <= 0):
            continue
        step_floydwarshal(
            valves,
            steps,
            curr_valve,
            minutes,
            state_bitmap,
            state | state_bitmap[curr_valve],
            flow + (minutes * valves[curr_valve][P_FLOW_RATE]),
            answer,
        )
    return answer


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self, minutes_left, start_valve):
        pprint(self.lines)

        ## Prepare
        valve_dict = {}
        for line in self.lines:
            valve_dict[line[0]] = line
        
        steps = {
            x: {
                y: 1 if y in valve_dict[x][P_CONNECTIONS] else math.inf
                for y in valve_dict
            }
            for x in valve_dict
        }

        # Floyd-Warshall step init
        for k in steps:
            for i in steps:
                for j in steps:
                    steps[i][j] = min(steps[i][j], steps[i][k] + steps[k][j])


        flowable_valves = {
            name: valve for (name, valve) in valve_dict.items() if valve[P_FLOW_RATE] > 0
        }
        state_bitmap = {v: 1 << i for i, v in enumerate(flowable_valves)}
        total_flow = max(
            step_floydwarshal(
                flowable_valves,
                steps,
                start_valve,
                minutes_left,
                state_bitmap,
                0,
                0,
                {},
            ).values()
        )
        return total_flow


@utils.profiler
def preprocess(raw_data):
    pattern = re.compile(
        r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.+)$"
    )
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = [match.group(1), int(match.group(2)), match.group(3).split(", ")]
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    minutes_left = 30
    start_valve = "AA"

    return solver.solve(minutes_left, start_valve)


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
