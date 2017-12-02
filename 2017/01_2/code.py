""" Advent of code 2017 day 1/2 """

from argparse import ArgumentParser
from functools import reduce

def reducer(acc, elem):
    """ Sum of the same elements """
    return acc + int(elem[0]) if elem[0] == elem[1] else acc

def solution(input_data):
    """ Solution to the problem """
    inputstr = str(input_data)
    step_size = len(inputstr)//2
    rotated = inputstr+inputstr[0: step_size]
    result = reduce(reducer, zip(rotated, rotated[step_size:]), 0)
    return result

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
        DEBUG = 44354352
        print(solution(DEBUG))
