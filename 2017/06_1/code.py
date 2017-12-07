""" Advent of code 2017	day 6/1	"""

from argparse import ArgumentParser

class Debugger(object):
    """ Memory management class """
    memory = []
    memory_size = -1

    @staticmethod
    def read_data(input_data):
        """ Read the input data """
        return list(map(int, input_data.split("\t")))

    def find_largest_bank(self):
        """ Find the largest element the lowest index wins on a tie """
        max_val = max(self.memory)
        max_indexes = [(index, elem) for index, elem in enumerate(self.memory) if elem == max_val]
        return max_indexes[0]

    def stringify_memory(self):
        """ Create a string from the memory array"""
        return ','.join(map(str, self.memory))

    def add_values(self, add_all, add_rem, from_where):
        """ Add common values to all and others only if necessary """
        outofbound_indices = range(from_where + 1, from_where + add_rem +1)
        rem_indices = set(map(lambda elem: elem % self.memory_size, outofbound_indices))
        enum = enumerate(self.memory)
        return [(elem + add_all + (1 if (index in rem_indices) else 0)) for index, elem in enum]

    def redistribution_cycle(self):
        """ Redistribute the memory """
        largest_index, largest_value = self.find_largest_bank()
        add_to_all, add_to_remaining = divmod(largest_value, self.memory_size)
        self.memory[largest_index] = 0
        self.memory = self.add_values(add_to_all, add_to_remaining, largest_index)
        return self.stringify_memory()

    def __init__(self, input_data):
        memory_dump = self.read_data(input_data)
        self.memory = memory_dump
        self.memory_size = len(memory_dump)
        self.largest_bank = self.find_largest_bank()

def solution(input_data):
    """ Solution to the problem """
    debugger = Debugger(input_data)
    step = 0
    memory_state = set()
    last_state = debugger.stringify_memory()
    while last_state not in memory_state:
        memory_state.add(last_state)
        last_state = debugger.redistribution_cycle()
        step += 1
    return step


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
        DEBUG = "0	2	7	0"
        print(solution(DEBUG))
