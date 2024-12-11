""" Advent of code 2024 day 09 / 2 """

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
            # if file_id == -1:
            #     continue
            for i in range(start, start + length):
                result += file_id * i
        return result

    def solve(self):
        # pprint(self.spaces)
        # pprint(self.files)
        result = []

        for f_index, file_id, file_length in sorted(self.files, reverse=True):
            print(f" {file_id}", end="\r")

            for j, (sp_index, _, space_length) in enumerate(self.spaces):
                if f_index < sp_index:
                    continue
                if file_length == space_length:
                    result.append((sp_index, file_id, file_length))
                    self.spaces[j] = (sp_index, -1, 0)  # make space unusable
                    break
                elif file_length < space_length:
                    result.append((sp_index, file_id, file_length))
                    self.spaces[j] = (
                        sp_index + file_length,
                        -1,
                        space_length - file_length,
                    )  # keep the remaining space
                    break
            else:
                result.append(
                    (f_index, file_id, file_length)
                )  # if the file does not fit anywhere keep it as it is
        result.sort(key=lambda x: x[0])
        # pprint(result)
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
