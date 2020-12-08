""" Advent of code 2020 day 08/2 """

import math
from os import path
import re
import logging

instruction_parser = re.compile(r'(nop|acc|jmp)\s+([+-]\d+)')


class HandheldDevice(object):
    def __init__(self, instructions, id):
        self.instructions = instructions
        self.id = id
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
            if self.ip >= len(self.instructions):
                logging.info(
                    "Ferminated %d: Index out of bounds: %d", self.id, self.ip)
                return None
            next_instruction = self.instructions[self.ip]
            ip_diff, acc_diff, should_terminate = self.execute(
                next_instruction)
            if should_terminate:
                logging.info("Terminated %d: Infinite loop: %d",
                             self.id, self.ip)
                self.terminate = True
                return None
            self.ip += ip_diff
            self.acc += acc_diff
            if self.ip == len(self.instructions):
                logging.info("SUCCESS %d. Solution(%d)", self.id, self.acc)
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

    def evolution_instructions(blueprint):
        result = []
        for i in range(0, len(blueprint)):
            match = instruction_parser.match(blueprint[i])
            change_instruction = match.group(1)
            if change_instruction == 'acc':
                continue
            instructions = [parse_line(x) for x in blueprint]
            if change_instruction == 'jmp':
                instructions[i]["instruction"] = 'nop'
            elif change_instruction == 'nop':
                instructions[i]["instruction"] = 'jmp'
            result.append(instructions)
        return result

    return evolution_instructions(processed_data)


def solution(data):
    """ Solution to the problem """
    instructionset = preprocess(data)
    for instructions in instructionset:
        solver = HandheldDevice(instructions, 0)
        result = solver.run()
        if result is not None:
            return result
    return None


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
