""" Advent of code 2018 day 4/1 """

import math
from os import path


def count_passwords(r_start: int, r_end: int):
    """ Calculate the number of passwrods that meet the predefined criteria """
    counter = 0
    for i in range(r_start, r_end):
        numbers = str(i)
        prev = numbers[0]
        if len(numbers) != 6:
            continue
        increasing, similar_digits = True, False
        for x in numbers[1:]:
            if prev > x:
                increasing = False
                break
            if prev == x:
                similar_digits = True
            prev = x
        if increasing and similar_digits:
            counter += 1
    return counter


def solution(data: str):
    """ Solution to the problem """
    r_start, r_end = [int(x) for x in data.split("-")]
    return count_passwords(r_start, r_end)


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
