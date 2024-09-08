""" Advent of code 2023 day 12 / 1 """

from pprint import pprint
from os import path
import utils
import re

MAPPING = str.maketrans({"0": ".", "1": "#"})


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def parse(self, original: str, x: int, max_len: int, solver_key: tuple):
        bin_num = bin(x)[2:].rjust(max_len, "0")
        code = bin_num.translate(MAPPING)
        res: list[str] = []
        i = 0
        for s in original:
            if s == "?":
                res.append(code[i])
                i += 1
            else:
                res.append(s)

        restored_code = "".join(res)
        cnt = 0
        res2: list[int] = []
        prev = "x"
        for c in restored_code:
            if c == "#":
                cnt += 1
            elif prev == "#" and c == ".":
                res2.append(cnt)
                cnt = 0
            prev = c
        if cnt != 0:
            res2.append(cnt)
        translated_code = tuple(res2)
        # print("TRY:", bin_num, x, original, restored_code, translated_code)
        if translated_code == solver_key:
            # print("FOUND: ", restored_code, translated_code)
            return restored_code, True
        return "", False

    def solve(self):
        # pprint(self.lines)
        result = 0
        for i, (code, solver_key) in enumerate(self.lines):
            res = set([])
            num_error = code.count("?")
            print(f"{i+1}/{len(self.lines)} found {num_error} slots")
            for x in range(2**num_error + 1):
                p_result, is_valid = self.parse(code, x, num_error, solver_key)
                if is_valid:
                    # print(code, x, num_error, solver_key)
                    res.add(p_result)
            different = len(res)
            # print(different)
            result += different
        return result


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        data = line.split(" ")
        processed_data.append([data[0], tuple(map(int, data[1].split(",")))])
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
