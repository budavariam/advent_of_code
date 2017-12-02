""" Advent of code 2017	day 2/2	"""

from argparse import ArgumentParser
from functools import reduce
from itertools import combinations

def row(line):
    """ Count the checksum of a row """
    pairs = list(combinations(map(int, line.strip().split("\t")), 2))
    for elem_x, elem_y in pairs:
        divide, modulo = divmod(max(elem_x, elem_y), min(elem_x, elem_y))
        if modulo == 0:
            return divide
    return -1

def solution(input_data):
    """ Solution to the problem """
    return sum([row(line) for line in input_data.split("\n")])

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'rb')) as input_file:
            print(solution(input_file.read()))
    elif ARGS.test:
        print(solution(str(ARGS.test)))
    else:
        DEBUG = """5	9	2	8
                9	4	7	3
                3	8	6	5"""
        print(solution(DEBUG))