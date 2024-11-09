""" Advent of code 2023 day 18 / 2 """

from os import path
import re
import utils


DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


class Code(object):
    def __init__(self, lines):
        self.instructions = lines

    def calculate_shoelace_formula(self, vertices):
        n = len(vertices)
        area = 0

        for i in range(n):
            y1, x1 = vertices[i]
            y2, x2 = vertices[(i + 1) % n]
            area += x1 * y2 - y1 * x2
            border_length = abs(x2 - x1) + abs(y2 - y1)
            area += border_length

        return abs(area) // 2 + 1

    def dig(self, pos, instruction):
        next_d, count, _ = instruction
        d = DIRECTIONS[next_d]
        d_y, d_x = d
        c_y, c_x = pos
        new_pos = (c_y + (d_y * count), c_x + (d_x * count))
        return new_pos

    def solve(self):
        # pprint(self.instructions)
        pos = (0, 0)
        vertices = [pos]
        for _, ins in enumerate(self.instructions):
            # print(f"{i+1}/{len(self.instructions)}")
            pos = self.dig(pos, ins)
            vertices.append(pos)
        return self.calculate_shoelace_formula(vertices)


def convert_code(hexcode):
    """
    Each hexadecimal code is six hexadecimal digits long.
        The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number.
        The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.
    """
    return [["R", "D", "L", "U"][int(hexcode[-1])], int(hexcode[:-1], 16), "."]


@utils.profiler
def preprocess(raw_data):
    pattern = re.compile(r"(U|D|L|R) (\d+) \(#(\w+)\)")
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = convert_code(match.group(3))
        processed_data.append(data)
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
