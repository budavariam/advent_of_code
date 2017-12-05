""" Advent of code 2017	day 5/1	"""

from argparse import ArgumentParser

def read_data(input_data):
    return {key: int(value) for key, value in enumerate(input_data.split('\n'))}

class CPU(object):
    def jump(self):
        current_index = self.index
        self.index += self.data[current_index]
        self.data[current_index] += 1

    def __init__(self, data):
        self.data = data
        self.index = 0


def solution(input_data):
    """ Solution to the problem """
    data = read_data(input_data)
    array_length = len(data)
    cpu = CPU(data)
    step = 0
    while cpu.index < array_length and cpu.index >= 0:
        #print(step, cpu.data)
        cpu.jump()
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
        DEBUG = "0\n3\n0\n1\n-3"
        print(solution(DEBUG))
