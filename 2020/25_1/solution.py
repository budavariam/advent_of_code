""" Advent of code 2020 day 25/1 """

import math
from os import path


class ComboBreaker(object):
    def __init__(self, data):
        self.card_pk, self.door_pk = data

    def transform_number(self, subject_number, loop_size):
        """
        Set the value to itself multiplied by the subject number.
        Set the value to the remainder after dividing the value by 20201227.
        """
        return pow(subject_number, loop_size, 20201227)

    def figureout_loopsize(self):
        limit = 20201227
        for iteration in range(1, limit + 1):
            if iteration % 1000000 == 0:
                print(f"-- {iteration}")
            public_key = self.transform_number(7, iteration)
            if public_key == self.card_pk:
                return iteration

    def solve(self):
        loopsize = self.figureout_loopsize()
        return self.transform_number(self.door_pk, loopsize)


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    card_pk = int(processed_data[0])
    door_pk = int(processed_data[1])
    return (card_pk, door_pk)


def solution(raw_data):
    """ Solution to the problem """
    data = preprocess(raw_data)
    solver = ComboBreaker(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
