""" Advent of code 2020 day 6/2 """

import math
from os import path


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def match_everyone(self, people_answers):
        answers = people_answers[0]
        for answer in people_answers[1:]:
            answers = answers.intersection(answer)
        return len(answers)

    def solve(self):
        return sum(map(self.match_everyone, self.lines))


def preprocess(raw_data):
    processed_data = [[set(x) for x in groups.split("\n")]
                      for groups in raw_data.split("\n\n")]
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
