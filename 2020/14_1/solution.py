""" Advent of code 2020 day 14/1 """

import math
from os import path
import sys
import re

TYPE_MASK = "mask"
TYPE_MEMORY = "memory"
MASK_REGEX = re.compile(r'mask = ([X01]+)')
MEM_REGEX = re.compile(r'mem\[(\d+)\] = (\d+)')
map_ones = str.maketrans("X", "1")
map_zeroes = str.maketrans("X", "0")


class DockData(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.current_mask = None
        self.memory = {}

    def process_instruction(self, instruction):
        if instruction["type"] == TYPE_MEMORY:
            number = instruction["number"]
            if self.current_mask is None:
                print("Mask is not available")
                sys.exit(1)
            number &= self.current_mask["mask_ones"]
            number |= self.current_mask["mask_zeroes"]
            self.memory[instruction["location"]] = number
            return
        elif instruction["type"] == TYPE_MASK:
            self.current_mask = instruction
            return
        else:
            print("Unknown instruction", instruction)
            return

    def solve(self):
        for instr in self.instructions:
            self.process_instruction(instr)

        return sum(self.memory.values())


def preprocess(raw_data):
    def process_line(line):
        memory_line = MEM_REGEX.match(line)
        if memory_line is not None:
            return {
                "type": TYPE_MEMORY,
                "location": memory_line.group(1),
                "number": int(memory_line.group(2)),
            }
        mask_line = MASK_REGEX.match(line)
        if mask_line is not None:
            original_mask = mask_line.group(1)
            return {
                "type": TYPE_MASK,
                "original_mask": original_mask,
                "mask_ones": int(f"{original_mask.translate(map_ones)}", base=2),
                "mask_zeroes": int(f"{original_mask.translate(map_zeroes)}", base=2)
            }

    processed_data = [process_line(line) for line in raw_data.split("\n")]
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = DockData(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
