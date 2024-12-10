""" Advent of code 2024 day 09 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict, deque
from utils import log, profiler


class Code(object):
    def __init__(self, lines):
        self.og = lines["og"]
        self.files = deque(lines["files"])
        self.spaces = deque(lines["spaces"])

    def calc_result(self, fragments):
        result = 0
        # pprint(fragments)
        for start, file_id, length in fragments:
            # if file_id == -1:
            #     print(".", end="")
            # else:
            #     print(f"{file_id}*{length}",end=" ")

            for i in range(start, start + length):
                result += file_id * i
        return result

    def solve(self):
        # pprint(self.og)
        # pprint(self.files)
        # pprint(self.spaces)
        result = []
        curr_file = None
        curr_space = None
        curr_index = 0
        while len(self.spaces) > 1 and len(self.files) > 0:
            # print(
            #     f"{len(self.spaces)} blocks left. files start at: {self.files[0][0]} spaces start at: {self.spaces[0][0]}"
            # )
            if self.files[0][0] < self.spaces[0][0]:
                curr_file = self.files.popleft()
                # print(f".. a file block is next at: {curr_file[0]}")
                result.append((curr_index, curr_file[1], curr_file[2]))
                curr_index += curr_file[2]
                curr_file = None
            elif self.files[0][0] > self.spaces[0][0]:
                # print(f".. a space block is next at: {self.spaces[0][0]}")
                #   get a file from the end and split until the space lasts
                curr_file = self.files.pop()
                curr_space = self.spaces.popleft()
                # print(f".... interval positions: f:{curr_file[2]} s:{curr_space[2]}")
                if curr_file[2] == curr_space[2]:
                    # print("their lengths match up, the file fills in the space")
                    result.append((curr_space[0], curr_file[1], curr_space[2]))
                    curr_index += curr_space[2]
                elif curr_file[2] < curr_space[2]:
                    # print("the file does not fill up the available space.")
                    result.append((curr_space[0], curr_file[1], curr_file[2]))
                    curr_index += curr_file[2]
                    # add back the remaining space to spaces
                    self.spaces.appendleft(
                        (curr_index, -1, curr_space[2] - curr_file[2])
                    )
                elif curr_file[2] > curr_space[2]:
                    # print("the file is larger than the space")
                    #   fill the available space in the result, and add back the file remains at the end
                    result.append((curr_space[0], curr_file[1], curr_space[2]))
                    curr_index += curr_space[2]
                    self.files.append(
                        (-1, curr_file[1], curr_file[2] - curr_space[2])
                    )

        return self.calc_result(result)


@profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = {"files": [], "spaces": [], "og": raw_data}
    is_file = True
    curr = 0
    file_id = 0
    for x in list(raw_data):
        length = int(x)
        arr = "files" if is_file else "spaces"
        if (is_file) or (not is_file and length > 0):
            processed_data[arr].append((curr, file_id if is_file else -1, length))
        # prepare next step
        curr += length
        if is_file:
            file_id += 1
        is_file = not is_file

    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
