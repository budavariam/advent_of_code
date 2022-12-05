""" Advent of code 2022 day 05 / 2 """

from os import path
import re


def not_empty(item):
    return item != ""

class Code(object):
    def __init__(self, input_data):
        self.crates = input_data[0]
        self.instructions = input_data[1]

    def get_result(self, crates):
        return "".join([x[-1] for x in crates])

    def move(self, inst, data):
        crts = data
        count, frm, to = inst
        tmp = []
        for _ in range(count):
            popped = data[frm - 1].pop()
            tmp.append(popped)
        data[to - 1].extend(tmp[::-1])
        return crts

    def solve(self):
        # print(self.crates)
        for inst in self.instructions:
            self.move(inst, self.crates)
        return self.get_result(self.crates)


def preprocess(raw_data):
    pattern_instr = re.compile(r"move (\d+) from (\d+) to (\d+)")
    lines = raw_data.split("\n")
    i = 0
    crates = []
    instructions = []
    for line in lines:
        n = 4
        crts = [line[i : i + n].strip().strip("[]") for i in range(0, len(line), n)]
        i += 1
        if line == "":
            break
        if crts[0] == "1":
            continue
        crates.append(crts)

    crates = list(map(list, zip(*crates)))
    crates = [list(filter(not_empty, x[::-1])) for x in crates]

    for line in lines[i:]:
        match = re.match(pattern_instr, line)
        data = [int(x) for x in [match.group(1), match.group(2), match.group(3)]]
        instructions.append(data)

    return (crates, instructions)


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
