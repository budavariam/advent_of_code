""" Advent of code 2017	day 4/1	"""

from argparse import ArgumentParser

def is_valid(line):
    tokens = line.split(" ")
    return len(set(tokens)) == len(list(tokens))

def solution(input_data):
    """ Solution to the problem """
    lines = input_data.split("\n")
    valid = 0
    for line in lines:
        valid += 1 if is_valid(lines) else 0
    return valid

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
        DEBUG = "361527"
        print(solution(DEBUG))