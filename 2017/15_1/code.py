""" Advent of code 2017 day 15/1 """
from argparse import ArgumentParser

class Generator(object):
    """ Value generators """
    def __init__(self, factor, initial, name):
        """ Constructor for the object """
        self.factor = factor
        self.prev_value = initial
        self.name = name

    def __next__(self):
        """ To make it iterable """
        return_value = (self.prev_value * self.factor) % 2147483647
        #print(self.name, self.prev_value, return_value)
        self.prev_value = return_value
        return return_value

    def __iter__(self):
        return self

class Judge(object):
    """ Judge of the generators """
    def __init__(self, generators, pair_count):
        self.gen_a, self.gen_b = generators
        self.pair_count = pair_count

    def process(self):
        """ Judge the values of the generators """
        matched = 0
        for index in range(self.pair_count):
            if (index % 1000000) == 0:
                print(index)
            if self.compare(next(self.gen_a), next(self.gen_b)):
                matched += 1
        return matched

    @staticmethod
    def compare(val_1, val_2):
        """ Compare the lowest 16 bits of the values """
        return (val_1 & 0xffff) == (val_2 & 0xffff)

def read_data(data):
    """ Parse the input data """
    return [int(line[line.rfind(" "):]) for line in data.split('\n')]

def solution(data):
    """ Solution to the problem """
    val_a, val_b = read_data(data)
    gen_a = Generator(16807, val_a, 'A')
    gen_b = Generator(48271, val_b, 'B')
    pair_count = 40000000
    return Judge([gen_a, gen_b], pair_count).process()

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
        DEBUG = """Generator A starts with 65
Generator B starts with 8921"""
        print(solution(DEBUG))
