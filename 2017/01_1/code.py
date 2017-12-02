""" Advent of code 2017 day 1/1 """

from argparse import ArgumentParser
from functools import reduce

def reducer(acc, elem):
    """ Sumof the same elements """
    return acc + int(elem[0]) if elem[0] == elem[1] else acc

def solution(input_str):
    """ Solution to the problem """
    inputstr = str(input_str)
    rotated = inputstr+inputstr[0]
    result = reduce(reducer, zip(rotated, rotated[1:]), 0)
    return result

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'rb')) as input_file:
            print(solution(input_file.read()))
    else:
        print(solution(str(ARGS.test)))
