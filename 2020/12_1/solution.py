""" Advent of code 2020 day 12/1 """

import math
from os import path
import re
from operator import mul
from functools import reduce

INSTRUCTION_PARSER = re.compile(r'(\w)(\d+)')
DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}
DEGREE_TO_DIREECTION = {
    270: "N",
    90: "S",
    0: "E",
    180: "W",
}


def add(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def multiply(t1, t2):
    return tuple(map(lambda tpl: mul(tpl[0], tpl[1]), zip(t1, t2)))


class Ferry(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.face_direction = 0
        self.location = (0, 0)

    def navigate(self, instruction):
        face_direction = self.face_direction
        location = self.location
        command = instruction["command"]
        parameter = instruction["parameter"]
        direction = DIRECTIONS.get(command)
        if direction is not None:
            location = add(location, multiply(
                (parameter, parameter), direction))
        elif command == "L":
            face_direction = (face_direction - parameter) % 360
        elif command == "R":
            face_direction = (face_direction + parameter) % 360
        elif command == "F":
            face_orient = DEGREE_TO_DIREECTION[face_direction]
            direction = DIRECTIONS.get(face_orient)
            location = add(location, multiply(
                (parameter, parameter), direction))
        else:
            print("Unknown command", instruction)
        return location, face_direction

    def solve(self):
        for instr in self.instructions:
            self.location, self.face_direction = self.navigate(instr)
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
