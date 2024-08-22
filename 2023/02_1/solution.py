""" Advent of code 2023 day 02 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines, initstate):
        self.limits = initstate
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        result = 0
        for line in self.lines:
            possible = True
            for s in line.get("sets"):
                for limit_k, limit_v in self.limits.items():
                    if s.get(limit_k, 0) > limit_v:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                result += line.get("id")
        return result


@utils.profiler
def preprocess(raw_data):
    """Collect the game id and create data format"""
    # Game 1: 6 green, 3 blue; 3 red, 1 green; 4 green, 3 red, 5 blue
    id_pattern = re.compile(r"Game (\d+):")
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(id_pattern, line)
        sets = line.split(": ")[1].split("; ")
        sets = [x.split(", ") for x in sets]
        result = []
        for s in sets:
            play = {}
            for raw in s:
                num, tp = raw.split(" ")
                play[tp] = int(num)
            result.append(play)

        data = {
            "id": int(match.group(1)),
            "sets": result,
        }
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data, initstate):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines, initstate)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read(), {"red": 12, "green": 13, "blue": 14}))
