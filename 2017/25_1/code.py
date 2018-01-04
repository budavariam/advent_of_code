""" Advent of code 2017 day 25/1 """
from argparse import ArgumentParser
import re
from collections import defaultdict, deque

class TuringMachine(object):
    """ Turing machine for the CPU"""

    def __init__(self, data):
        """ Constructor """
        self.state, self.steps, self.states = self.read_data(data)
        self.tape = deque([0])
        self.tape_length = 0
        self.pointer = 0

    @staticmethod
    def parse_state(patterns, values):
        """ Parse the states by variables """
        curr_val = re.search(patterns['p_check'], values).group(1)
        write_val = re.search(patterns['p_write'], values).group(1)
        move_dir = re.search(patterns['p_move'], values).group(1)
        next_state = re.search(patterns['p_next'], values).group(1)
        return (curr_val, write_val, move_dir, next_state)

    def read_data(self, data):
        """ Read data blocks """
        states = defaultdict(dict)
        parsed = data.split('\n\n')
        start = re.search(r'Begin in state (\w)', parsed[0]).group(1)
        chksum = int(re.search(r'Perform a diagnostic checksum after (\d+) steps', parsed[0]).group(1))
        patterns = {
            'p_state': re.compile(r'In state (\w)'),
            'p_check': re.compile(r'the current value is (\d)'),
            'p_write': re.compile(r'Write the value (\d)'),
            'p_move': re.compile(r'Move one slot to the (left|right)'),
            'p_next': re.compile(r'Continue with state (\w)')
        }
        for block in parsed[1:]:
            curr_state = re.match(patterns['p_state'], block).group(1)
            states[curr_state] = {
                int(val): (
                    int(write),
                    move,
                    next_val
                ) for (val, write, move, next_val) in [
                    self.parse_state(patterns, values) for values in block.split('If')[1:]
                ]
            }
        return start, chksum, states

    def run(self):
        """ Pass"""
        for index in range(self.steps):
            if index % 10000 == 0:
                print(index)
            curr_val = self.tape[self.pointer]
            operations = self.states[self.state][curr_val]
            self.operate(*operations)
        return True

    def operate(self, write, move_direction, next_val):
        """ Do the instructions on the turing machine

        It is not a universal solution, only works if the instructions are in this order:
        * Write to the machine
        * Move the tape
        * Continue with another state
        """
        self.tape[self.pointer] = write
        self.move(move_direction)
        self.state = next_val

    def move(self, direction):
        """ Move on the infinite tape left or right """
        if direction == 'left':
            if self.pointer == 0:
                self.tape_length += 1
                self.tape.appendleft(0)
            else:
                self.pointer -= 1
        else:
            if self.pointer == self.tape_length:
                self.tape_length += 1
                self.tape.append(0)
            self.pointer += 1

    def get_checksum(self):
        """ Count the ones in the tape """
        return self.tape.count(1)

def solution(data):
    """ Solution to the problem """
    machine = TuringMachine(data)
    machine.run()
    return machine.get_checksum()

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
        DEBUG = """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""
        print(solution(DEBUG))
