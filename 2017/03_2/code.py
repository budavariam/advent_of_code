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

def side_pos(curr_index, level):
    """ Get the position indicator in the current side """
    return divmod(curr_index, (level - 1) * 2)

def ccn(curr_div, curr_mod, curr_list, curr_max):
    """ Caclulate current neighbours """
    if (curr_div == 3) and curr_mod > curr_max-2:
        return curr_list[-1] + curr_list[0]
    elif curr_mod > 0:
        # Default case, only needs to return the previous element
        return curr_list[-1]
    elif (curr_div > 0) and (curr_mod == 0):
        # The one after the corner, it has two neighbours from the current list
        return sum(curr_list[-2:])
    # There is not any current values yet.
    return 0

def cpn(prev_list, prev_level, curr, curr_div, curr_mod, curr_max):
    """ Calculate previous neighbours """
    largest_mod = prev_level
    if prev_level == 1:
        # No calculation needed, it only has 1 element, and every other element sees it
        return prev_list[0]
    else:
        if curr_div > 0:
                # The first case needs a value from the end of the previous list
            if curr_mod == largest_mod:
                # Corner value
                return prev_list[curr - 2*(curr_div+1)]
            elif (curr_mod == 1) or (curr_mod == largest_mod - 1):
                # Needs two neighbours
                corner = curr - 2*(curr_div+1)
                return sum(prev_list[corner: corner+1])
            # Other cases need three neighbours
            prev_max = curr - 2 * (curr_div)
            return sum(prev_list[prev_max - 2: prev_max + 1])
        else:
            if curr_mod == 0:
                return prev_list[-1] + prev_list[0]
            elif curr_mod == 1:
                return prev_list[-1] + prev_list[0:2]
            elif curr_mod == largest_mod - 1:
                corner = curr - 2
                return sum(prev_list[corner-1: corner+1])
            prev_max = curr - 2 * (curr_div)
            return sum(prev_list[prev_max - 2: prev_max + 1])

def calc_value(curr_start, curr, curr_list, prev, prev_list, prev_level, next_start):
    """ Calculate the current value from the currently existing neighbours """
    curr_index = curr - curr_start
    curr_max = next_start - curr_start - 1
    curr_div, curr_mod = side_pos(curr_index, prev_level+1)
    curr_sum = ccn(curr_div, curr_mod, curr_list, curr_max)
    prev_sum = cpn(prev_list, prev_level, curr, curr_div, curr_mod, curr_max)
    value = prev_sum + curr_sum
    print(value)
    return value

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
            value = calc_value(curr_start, curr, curr_list, prev, prev_list, prev_level, next_start)
            curr_list.append(value)
            yield value
            curr += 1
        prev_start, curr_start, next_start = curr_start, next_start, next(start_gen)
        prev_list, curr_list = curr_list, []

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
        DEBUG = "57"
        print(solution(DEBUG))
