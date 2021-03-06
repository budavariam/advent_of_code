""" Advent of code 2020 day 5/1 """

import logging
import math
from os import path
import re

seat_matcher = re.compile(r'^([FB]{7})([LR]{3})$')
map_binary = str.maketrans("BFRL", "1010")


class Seats(object):
    def __init__(self, seats):
        self.seats = seats

    def solve(self):
        return max(self.seats, key=lambda seat: seat["seat_id"])["seat_id"]


def parse_seat(line):
    match = seat_matcher.match(line)
    if match is None:
        logging.fatal(f"Failed to parse line {line}")
    row = int(f"{match.group(1).translate(map_binary)}", base=2)
    col = int(f"{match.group(2).translate(map_binary)}", base=2)
    id = (row * 8) + col
    return {
        "row": row,
        "col": col,
        "seat_id": id,
    }


def preprocess(raw_data):
    processed_data = map(parse_seat, raw_data.split("\n"))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Seats(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
