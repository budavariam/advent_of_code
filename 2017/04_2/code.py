""" Advent of code 2017	day 4/2	"""

from argparse import ArgumentParser
from functools import reduce

def is_valid(line):
    tokens = [''.join(sorted(word)) for word in line.split(" ")]
    return len(set(tokens)) == len(list(tokens))

def solution(input_data):
    """ Solution to the problem """
    return reduce(lambda acc, line: acc + (1 if is_valid(line) else 0), input_data.split("\n"), 0)

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
        DEBUG = "abcde edcab"
        print(solution(DEBUG))