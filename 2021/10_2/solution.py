""" Advent of code 2021 day 10 / 2 """

from os import path
from collections import deque

p = {
    "()": 1,
    "[]": 2,
    "kk": 3,
    "<>": 4,
}
m = {
    "(": "()",
    "[": "[]",
    "{": "kk",
    "<": "<>",
    ")": "()",
    "]": "[]",
    "}": "kk",
    ">": "<>",
}

opening = set(["(", "[", "{", "<"])
closing = set([")", "]", "}", ">"])

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        scores = deque()
        for line in self.lines:
            s = 0
            check_stack = deque()
            for c in line:
                if c in opening:
                    check_stack.append(c)
                elif c in closing:
                    shouldclose = check_stack.pop()
                    if m[shouldclose] != m[c]:
                        # ignore corrupted line
                        break
            else:
                # calc incomplete line
                while len(check_stack) > 0:
                    next_char = check_stack.pop()
                    s *= 5
                    s += p[m[next_char]]
                scores.append(s)
        return sorted(scores)[len(scores)//2]


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
