""" Advent of code 2017	day 2/2	"""

from argparse import ArgumentParser

def start_point():
    """ Get the start points"""
    n, start = 1, 1
    yield (start, n)
    while True:
        start = (4*pow(n, 2)) + (4*n) + 2
        yield (start, n)
        n += 1

def calc_value(curr_start, curr, curr_list, prev, prev_list, prev_level):
    """ Calculate the current value from the currently existing neighbours """
    curr_index = curr - curr_start
    if prev_level == 1:
        result = curr_list[curr_index-1] + (curr_list[curr_index-2] if is_corner(curr_index, prev_level+1))


def calc_circle(start_gen):
    """ Calculate ew circle values """
    prev_list = [1]
    curr_list = []
    prev_start, prev_level = next(start_gen)
    curr_start, _ = next(start_gen)
    next_start, _ = next(start_gen)
    while True: 
        prev = prev_start
        curr = curr_start
        while curr < next_start:
            curr_list.append(calc_value(curr_start, curr, curr_list, prev, prev_list, prev_level))
        prev_start = curr_start
        curr_start = next_start
        next_start = next(start_gen)

def solution(input_data):
    """ Solution to the problem """
    start_values = start_point()
    circle_values = calc_circle(start_values)
    current = -1
    upper_bound = int(input_data)
    while current < upper_bound:
        current = next(circle_values)
    return current

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
        DEBUG = "361527"
        print(solution(DEBUG))