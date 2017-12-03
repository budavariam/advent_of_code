""" Advent of code 2017	day 2/2	"""

from argparse import ArgumentParser
from functools import reduce
from itertools import combinations

def start_point(upper_int):
    """ Get the circle that this element is in, and its first elem """
    n, last, start = 1, 1, 2
    while start < upper_int:
        last = start
        start = (4*pow(n, 2)) + (4*n) + 2
        n += 1
    return (last, n)

def side_pos(input_num, start, x_dist):
    """ Get the position indicator in the current side """
    return (input_num - start) % ((x_dist - 1) * 2)

def count_y(side_pos, x_dist):
    """ Get the y dist of the element in its side """
    return abs(side_pos - (x_dist - 2))

def solution(input_data):
    """ Solution to the problem """
    input_num = int(input_data)
    circle_start, circle_num = start_point(input_num)
    x_dist = circle_num - 1
    position = side_pos(input_num, circle_start, x_dist)
    y_dist = count_y(position, circle_num)
    print(input_num, x_dist, y_dist, circle_start, circle_num)
    return x_dist + y_dist

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