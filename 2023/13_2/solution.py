""" Advent of code 2023 day 13 / 2 """

from os import path
import utils

MAPPING = str.maketrans({".": "0", "#": "1"})


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def process(self, index, d):
        data = d[index]
        # print(data.get("matrix"))
        height = data.get("height")
        found_index = -1
        for i in range(1, height):
            # NOTE: assuming that the mirror line is between i-1 and i, check all reflection pairs in the list.
            bit_diffs = sum([
                (data.get("matrix")[i - 1 - width] ^ data.get("matrix")[i + width]).bit_count()
                for width in range(i)
                if ((i - 1 - width) >= 0) and ((i + width) < height)
            ])
            if bit_diffs == 1:
                # NOTE: In case there is an error, there should be exactly one bit difference in the reflected pairs
                # And in this task we aim to get exactly one error
                found_index = i
        if found_index >= 0:
            return found_index * 100 if index == 0 else found_index
        return 0

    def solve(self):
        # pprint(self.lines)
        result = 0
        for i, line in enumerate(self.lines):
            result += self.process(0, line)
            result += self.process(1, line)
        return result


@utils.profiler
def preprocess(raw_data):
    def transform(m):
        return [int("".join(line).translate(MAPPING), 2) for line in m]

    processed_data = []
    for matrix in raw_data.split("\n\n"):
        raw = matrix.rstrip("\n").split("\n")
        vertical = [tuple(line) for line in raw]
        horizontal = list(zip(*(raw)))

        data = [
            {
                "matrix": transform(vertical),
                "width": len(vertical[0]),
                "height": len(vertical),
            },
            {
                "matrix": transform(horizontal),
                "width": len(horizontal[0]),
                "height": len(horizontal),
            },
        ]

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
