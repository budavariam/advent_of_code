""" Advent of code 2022 day 07 / 1 """

import math
from os import path
import re
from collections import defaultdict
import operator

TYPE_DIR = 0
TYPE_FIL = 1
TYPE_COM = 2


def get_filename(curr):
    return "/".join(curr)


def calcsize(structure):
    usedspace = 0
    res = defaultdict(int)
    folders = sorted(structure.keys(), reverse=True)
    for folder in folders:
        for data in structure[folder]:
            if data[0] == TYPE_FIL:
                res[folder] += data[1]
            if data[0] == TYPE_DIR:
                res[folder] += res[folder + f"/{data[1]}"]
    usedspace = res["/"]
    total = 70000000
    need = 30000000
    needspace = need - abs(total - usedspace)
    dir_sorted_reverse_by_size = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    candidates = [size for _, size in dir_sorted_reverse_by_size if size > needspace]
    return candidates.pop()


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        curr = []
        structure = defaultdict(list)
        for line in self.lines:
            if line[0] == TYPE_DIR:
                structure[get_filename(curr)].append(line)
            if line[0] == TYPE_FIL:
                structure[get_filename(curr)].append(line)
            if line[0] == TYPE_COM:
                _, command, param = line
                if command == "cd":
                    # print(f"moving into {param}")
                    if param == "..":
                        curr.pop()
                    else:
                        curr.append(param)
        return calcsize(structure)


def preprocess(raw_data):
    pattern_command = re.compile(r"^\$\s*(\w+)(.*)$")
    pattern_file = re.compile(r"^(\d+) (.*)$")
    pattern_dir = re.compile(r"^dir (\w+)")
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern_command, line)
        data = []
        if match is not None:
            data = [TYPE_COM, match.group(1).strip(), match.group(2).strip()]
        match = re.match(pattern_file, line)
        if match is not None:
            data = [TYPE_FIL, int(match.group(1)), match.group(2).strip()]
        match = re.match(pattern_dir, line)
        if match is not None:
            data = [TYPE_DIR, match.group(1).strip()]
        processed_data.append(data)
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
