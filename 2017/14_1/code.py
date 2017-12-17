""" Advent of code 2017 day 14/1 """
from argparse import ArgumentParser
from knot import Knot

def convert(line):
    """ Convert a line to binary representation """
    return ''.join(bin(int(line, 16))[2:].zfill(128))

def count_used(matrix):
    """ Count the 1-s in the lines """
    return sum([line.count('1') for line in matrix])

def solution(data):
    """ Solution to the problem """
    matrix = [convert(Knot(256, '{}-{}'.format(data, index)).knot_hash()) for index in range(128)]
    return count_used(matrix)

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(input_file.read()))
    elif ARGS.test:
        print(solution(str(ARGS.test)))
    else:
        DEBUG = """flqrgnkx"""
        print(solution(DEBUG))
