""" Advent of code 2023 day 15 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def hash_alg(self, text):
        """Determine the ASCII code for the current character of the string.
        Increase the current value by the ASCII code you just determined.
        Set the current value to itself multiplied by 17.
        Set the current value to the remainder of dividing itself by 256."""
        curr = 0
        for c in text:
            curr += ord(c)
            curr *= 17
            curr %= 256
        return curr

    def calc_focus(self, boxes):
        """
        One plus the box number of the lens in question.
        The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
        The focal length of the lens.
        """
        focus_power = 0
        for box_index, box in enumerate(boxes):
            for slot_index, slot in enumerate(box["items"], start=1):
                lens_power = (1 + box_index) * slot_index * slot[1]
                focus_power += lens_power
                # print(
                #     f"{slot[0]}: {1+box_index} (box) * {slot_index} (slot) * {slot[1]} (focal length) = {focus_power}"
                # )
        return focus_power

    def solve(self):
        boxes = [{"has": set(), "items": []} for _ in range(256)]
        # pprint(self.lines)
        for line, operation in self.lines:
            hsh = self.hash_alg(line)

            if operation[0] == "-":
                if line in boxes[hsh]["has"]:
                    boxes[hsh]["has"].remove(line)
                    boxes[hsh]["items"] = [
                        x for x in boxes[hsh]["items"] if x[0] != line
                    ]
                else:
                    pass
            elif operation[0] == "=":
                new_value = int(operation[1:])
                if line in boxes[hsh]["has"]:
                    boxes[hsh]["items"] = [
                        (k, v if k != line else new_value)
                        for k, v in boxes[hsh]["items"]
                    ]
                else:
                    boxes[hsh]["has"].add(line)
                    boxes[hsh]["items"].append((line, new_value))

            # print(line, hsh, operation)
            # print([x["items"] for x in boxes if x["has"]])

        return self.calc_focus(boxes)


@utils.profiler
def preprocess(raw_data):
    pattern = re.compile(r"(\w+)(-|=\d+)")
    processed_data = []
    for line in raw_data.split(","):
        match = re.match(pattern, line)
        data = [match.group(1), match.group(2)]
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
