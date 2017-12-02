""" Advent of code 2017	day 2/1	"""

from argparse import ArgumentParser
from functools import reduce

def row(line):
    """ Count the checksum of a row """
    elemlist = map(int, line.strip().split("\t"))
    return max(elemlist) - min(elemlist)

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
        DEBUG = """5	1	9	5
                7	5	3
                2	4	6	8"""
        print(solution(DEBUG))
