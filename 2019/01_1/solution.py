""" Advent of code 2019 day 1/1 """

from argparse import ArgumentParser
import math
from os import path

def solution(data):
    """ Solution to the problem """
    return sum([math.floor(int(x)/3)-2 for x in data.split("\n")])

if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))