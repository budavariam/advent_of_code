""" Advent of code 2020 day 14/2 """

import math
from os import path
import sys
import re
from functools import reduce

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

    def replace_chars_at_index(self, addressbinary, locations_to_replace):
        result = list(addressbinary)
        for pos, char in locations_to_replace:
            result[pos] = char
        return "".join(result)

    def calc_possible_floats(self, address, locations):
        possible_floats = []
        comb_count = 2 ** len(locations)
        for i in range(comb_count):
            # generate possible binary combinations for the floating variables
            x_mask = bin(i)[2:].zfill(len(locations))
            # match the original locations with the generated floating values
            loc = [(pos, x_mask[i]) for i, pos in enumerate(locations)]
            # replace the X-es in float
            floating_bin = self.replace_chars_at_index(
                bin(address)[2:].zfill(36), loc)
            floatint_int = int(floating_bin, base=2)
            possible_floats.append(floatint_int)
        return possible_floats

    def process_instruction(self, instruction):
        if instruction["type"] == TYPE_MEMORY:
            number = instruction["number"]
            address = instruction["location"]
            if self.current_mask is None:
                print("Mask is not available")
                sys.exit(1)
            address |= self.current_mask["mask_zeroes"]
            locations = self.current_mask["floating_locations"]
            possible_floats = self.calc_possible_floats(address, locations)
            for floating_address in possible_floats:
                self.memory[floating_address] = number
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
                "location": int(memory_line.group(1)),
                "number": int(memory_line.group(2)),
            }
        mask_line = MASK_REGEX.match(line)
        if mask_line is not None:
            original_mask = mask_line.group(1)
            return {
                "type": TYPE_MASK,
                "original_mask": original_mask,
                "mask_ones": int(f"{original_mask.translate(map_ones)}", base=2),
                "mask_zeroes": int(f"{original_mask.translate(map_zeroes)}", base=2),
                "floating_locations": reduce(lambda acc, data: [*acc, data[0]] if data[1] == "X" else acc, enumerate(original_mask), [])
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
