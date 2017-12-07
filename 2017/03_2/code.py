""" Advent of code 2017	day 3/1	"""

from argparse import ArgumentParser

def start_point():
    """ Get the start points"""
    n, start = 1, 2
    yield (start, n)
    while True:
        start = (4*pow(n, 2)) + (4*n) + 2
        yield (start, n)
        n += 1

def side_pos(curr_index, level):
    """ Get the position indicator in the current side """
    return divmod(curr_index, (level - 1) * 2)

def ccn(curr_div, curr_mod, curr_list, prev_level):
    """ Caclulate current neighbours """
    value = 0
    largest_mod = max(2 * prev_level - 1, 0)
    #TODO error: larges mod gets calculated wrong
    if (curr_div == 3) and curr_mod > largest_mod-2:
        value += curr_list[0]
    if curr_mod > 0:
        # Default case, only needs to return the previous element
        value += curr_list[-1]
    elif (curr_div > 0) and (curr_mod == 0):
        # The one after the corner, it has two neighbours from the current list
        value += sum(curr_list[-2:])
    # There is not any current values yet.
    return value

def cpn(prev_list, prev_level, curr_index, curr_div, curr_mod):
    """ Calculate previous neighbours """
    largest_mod = max(2 * prev_level - 1, 0)
    if prev_level == 1:
        # No calculation needed, it only has 1 element, and every other element sees it
        return prev_list[0]
    else:
        if curr_div > 0:
                # The first case needs a value from the end of the previous list
            if curr_mod == largest_mod:
                # Corner value
                return prev_list[curr_index - 2*(curr_div+1)]
            elif curr_mod == 0:
                # Needs two neighbours
                corner = curr_index - 1 - 2*(curr_div)
                return sum(prev_list[corner: corner+2])
            elif curr_mod == largest_mod - 1:
                # Needs two neighbours
                corner = curr_index + 1 - 2*(curr_div + 1)
                return sum(prev_list[corner-1: corner+1])
            # Other cases need three neighbours
            prev_max = curr_index - 2 * (curr_div)
            return sum(prev_list[prev_max - 2: prev_max + 1])
        else:
            if curr_mod == 0:
                # First element
                return prev_list[-1] + prev_list[0]
            elif curr_mod == 1:
                # Second element
                return prev_list[-1] + sum(prev_list[0:2])
            elif curr_mod == largest_mod - 1:
                # One before the right corner
                corner = curr_mod - 1
                return sum(prev_list[corner-1: corner+1])
            elif curr_mod == largest_mod:
                # Corner value
                first_corner = curr_mod - 2
                return prev_list[first_corner]
            # Three neighbours
            prev_max = curr_index
            return sum(prev_list[prev_max - 2: prev_max + 1])

def calc_value(curr_start, curr, curr_list, prev_list, prev_level):
    """ Calculate the current value from the currently existing neighbours """
    curr_index = curr - curr_start
    curr_div, curr_mod = side_pos(curr_index, prev_level+1)
    prev_sum = cpn(prev_list, prev_level, curr_index, curr_div, curr_mod)
    curr_sum = ccn(curr_div, curr_mod, curr_list, prev_level)
    value = prev_sum + curr_sum
    print("{}={}+{} ({},{},{})".format(value, prev_sum, curr_sum, curr, curr_div, curr_mod))
    return value

def calc_circle(start_gen):
    """ Calculate ew circle values """
    prev_list = [1]
    curr_list = []
    prev_start, prev_level = next(start_gen)
    curr_start, _ = next(start_gen)
    prev = 1
    curr = 2
    while True:
        while curr < curr_start:
            value = calc_value(prev_start, curr, curr_list, prev_list, prev_level)
            curr_list.append(value)
            yield value
            curr += 1
            prev += 1
        prev_start, (curr_start, prev_level) = curr_start, next(start_gen)
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
        DEBUG = "361527"
        print(solution(DEBUG))
