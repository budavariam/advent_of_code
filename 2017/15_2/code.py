""" Advent of code 2017 day 15/2 """
from argparse import ArgumentParser

def generator(factor, prev_value, name, multiple):
    """ Generator function for the generator """
    while True:
        prev_value *= factor
        prev_value %= 2147483647
        if prev_value % multiple == 0:
            #print(name, prev_value)
            yield prev_value

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
        """ Compare the values """
        return (val_1 & 0xffff) == (val_2 & 0xffff)

def read_data(data):
    """ Parse the input data """
    return [int(line[line.rfind(" "):]) for line in data.split('\n')]

def solution(data):
    """ Solution to the problem """
    val_a, val_b = read_data(data)
    gen_a = generator(16807, val_a, 'A', 4)
    gen_b = generator(48271, val_b, 'B', 8)
    pair_count = 5000000
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
