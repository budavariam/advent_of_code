""" Advent of code 2023 day 06 / 2 """

from pprint import pprint
from os import path
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        pprint(self.lines)
        record_time, record_distance = self.lines
        win_times = 0
        for hold_time in range(1, record_time):
            if hold_time + (record_time - hold_time - 1) * hold_time > record_distance:
                win_times += 1
            elif win_times > 0:
                break
        return win_times


@utils.profiler
def preprocess(raw_data):
    raw_lines, raw_distances = raw_data.split("\n")
    processed_data = [
        int(raw_lines.split(": ")[1].replace(" ", "")),
        int(raw_distances.split(": ")[1].replace(" ", "")),
    ]
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
