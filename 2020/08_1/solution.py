""" Advent of code 2020 day 08/1 """

import math
from os import path
import re
import logging

instruction_parser = re.compile(r'(nop|acc|jmp)\s+([+-]\d+)')


class HandheldDevice(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.ip = 0
        self.acc = 0
        self.terminate = False

    def execute(self, inst):
        should_terminate = inst["visited"] == True
        inst["visited"] = True
        if inst["instruction"] == 'acc':
            return [1, inst["parameter"], should_terminate]
        elif inst["instruction"] == 'jmp':
            return [inst["parameter"], 0, should_terminate]
        elif inst["instruction"] == 'nop':
            return [1, 0,  should_terminate]
        else:
            logging.fatal("Unknown instruction: %s", inst["instruction"])

    def run(self):
        while not self.terminate:
            next_instruction = self.instructions[self.ip]
            ip_diff, acc_diff, should_terminate = self.execute(
                next_instruction)
            if should_terminate:
                self.terminate = True
                break
            self.ip += ip_diff
            self.acc += acc_diff
        return self.acc


def preprocess(raw_data):
    processed_data = raw_data.split("\n")

    def parse_line(line):
        match = instruction_parser.match(line)
        instruction = match.group(1)
        parameter = match.group(2)
        return {
            "instruction": instruction,
            "parameter": int(parameter),
            "visited": False,
        }

    return [parse_line(x) for x in processed_data]


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = HandheldDevice(lines)
    return solver.run()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
