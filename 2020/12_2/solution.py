""" Advent of code 2020 day 12/2 """

import math
from os import path
import re
from operator import mul

INSTRUCTION_PARSER = re.compile(r'(\w)(\d+)')
DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}


def add(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def multiply(t1, t2):
    return tuple(map(lambda tpl: mul(tpl[0], tpl[1]), zip(t1, t2)))


class Ferry(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.waypoint_location = (-1, 10)
        self.location = (0, 0)

    def rotate_around_ship(self, coord, rotation):
        y, x = coord
        return {
            90: (x, -y),
            180: (-y, -x),
            270: (-x, y),
        }[rotation]

    def navigate(self, instruction):
        waypoint_location = self.waypoint_location
        location = self.location
        command = instruction["command"]
        parameter = instruction["parameter"]
        direction = DIRECTIONS.get(command)
        if direction is not None:
            waypoint_location = add(waypoint_location, multiply(
                (parameter, parameter), direction))
        elif command == "L":
            waypoint_location = self.rotate_around_ship(
                waypoint_location, 360 - parameter)
        elif command == "R":
            waypoint_location = self.rotate_around_ship(
                waypoint_location, parameter)
        elif command == "F":
            location = add(location, multiply(
                (parameter, parameter), waypoint_location))
        else:
            print("Unknown command", instruction)
        return waypoint_location, location

    def solve(self):
        for instr in self.instructions:
            self.waypoint_location, self.location = self.navigate(instr)
        return sum(map(abs, self.location))


def preprocess(raw_data):
    def parse_instruction(line):
        match = INSTRUCTION_PARSER.match(line)
        command = match.group(1)
        num = int(match.group(2))
        return {"command": command, "parameter": num}
    processed_data = [parse_instruction(line) for line in raw_data.split("\n")]
    return processed_data


def solution(data):
    """ Solution to the problem """
    instructions = preprocess(data)
    solver = Ferry(instructions)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
