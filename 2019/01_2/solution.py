""" Advent of code 2019 day 1/2 """

from argparse import ArgumentParser
import math
from os import path

def calc_fuel(x: int):
    """ Calculate the fuel necessary for the modules. Including the fuel of fuel. """
    fuel = x
    result = 0
    while fuel > 0:
        fuel = math.floor(fuel / 3) - 2
        result += fuel if fuel > 0 else 0
    return result

def solution(data: str):
    """ Solution to the problem """
    return sum([calc_fuel(int(x)) for x in data.split("\n")])

if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
