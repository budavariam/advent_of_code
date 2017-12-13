""" Advent of code 2017 day 10/1 """

from argparse import ArgumentParser

class Knot(object):
    """ Stream of data that has garbage """

    @staticmethod
    def read_data(data):
        """ Read the comma separated list of integers """
        return list(map(int, data.split(',')))

    def __repr__(self):
        return "{},{} - {}".format(self.skipsize, self.current_position, self.data)

    def process_data(self):
        """ Implement the hashing algorithm """
        print(self)
        for length in self.lengths:
            self.reverse(self.current_position, length)
            self.current_position += (self.skipsize + length)
            self.current_position %= self.domain_size
            self.skipsize = (self.skipsize + 1) % self.domain_size
            print(self)

    def reverse(self, start, length):
        """ Connect the ends and do a half twist """
        end = start + length
        overflow = end > (self.domain_size - 1)
        if overflow:
            over_bottom = end % self.domain_size
            over_top = start % self.domain_size
            elements = list(reversed(self.data[over_top:] + self.data[:over_bottom]))
            element_center = self.domain_size - start
            self.data[:over_bottom] = elements[element_center:]
            self.data[over_top:] = elements[:element_center]
        else:
            new_list = list(reversed(self.data[start:end]))
            self.data[start:(end)] = new_list

    def __init__(self, domain_size, input_data):
        """ Constructor for stream """
        self.domain_size = domain_size
        self.lengths = self.read_data(input_data)
        self.data = list(range(self.domain_size))
        self.current_position = 0
        self.skipsize = 0

    def get_result(self):
        """ Get the result for the first question """
        return self.data[0] * self.data[1]

def solution(domain_size, input_data):
    """ Solution to the problem """
    knot = Knot(domain_size, input_data)
    knot.process_data()
    return knot.get_result()

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(256, input_file.read()))
    elif ARGS.test:
        print(solution(256, str(ARGS.test)))
    else:
        DEBUG = """3, 4, 1, 5"""
        print(solution(5, DEBUG))
