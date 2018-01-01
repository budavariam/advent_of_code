""" Advent of code 2017 day 23/1 """
from argparse import ArgumentParser
import re
from collections import defaultdict, deque

class Instruction(object):
    """ Instruction for the parser """

    @staticmethod
    def parse(line):
        """ Create the proper instance for the parser """
        return OPERATION[line[:3]](line)

    @staticmethod
    def is_digit(value):
        """ Returns True if the given string represents a number """
        return value.lstrip('-').isdigit()

    def operate(self, p_data):
        """ Abstract method for the operation """
        raise NotImplementedError

class OperationSet(Instruction):
    """set X Y sets register X to the value of Y."""
    pattern = re.compile(r'set (\w) (.+)')

    def __repr__(self):
        return self.repr

    def __init__(self, line):
        """ Constructor """
        self.repr = line
        match = re.match(self.pattern, line)
        self.val_x = match.group(1)
        self.val_y = match.group(2)
        self.is_value = self.is_digit(self.val_y)
        if self.is_value:
            self.val_y = int(self.val_y)

    def operate(self, p_data):
        """ Run the operation """
        if self.is_value:
            p_data.memory[self.val_x] = self.val_y
        else:
            if self.val_y in p_data.memory:
                p_data.memory[self.val_x] = p_data.memory[self.val_y]
            else:
                p_data.memory[self.val_x] = 0
                p_data.memory[self.val_y] = 0
        return p_data.ptr+1

class OperationMul(Instruction):
    """mul X Y sets register X to the result of multiplying
    the value contained in register X by the value of Y."""
    pattern = re.compile(r'mul (\w) (.+)')

    def __repr__(self):
        return self.repr

    def __init__(self, line):
        """ Constructor """
        self.repr = line
        match = re.match(self.pattern, line)
        self.val_x = match.group(1)
        self.val_y = match.group(2)
        self.is_value = self.is_digit(self.val_y)
        if self.is_value:
            self.val_y = int(self.val_y)

    def operate(self, p_data):
        """ Run the operation """
        p_data.mulinvoked += 1
        if self.is_value:
            p_data.memory[self.val_x] *= self.val_y
        else:
            if self.val_y in p_data.memory:
                p_data.memory[self.val_x] *= p_data.memory[self.val_y]
            else:
                p_data.memory[self.val_x] = 0
                p_data.memory[self.val_y] = 0
        return p_data.ptr+1

class OperationJnz(Instruction):
    """jnz X Y jumps with an offset of the value of Y,
    but only if the value of X is not zero.
    (An offset of 2 skips the next instruction,
    an offset of -1 jumps to the previous instruction, and so on.)"""
    pattern = re.compile(r'jnz (\w) (.+)')

    def __repr__(self):
        return self.repr

    def __init__(self, line):
        """ Constructor """
        self.repr = line
        match = re.match(self.pattern, line)
        self.val_x = match.group(1)
        self.val_y = match.group(2)
        self.is_x_value = self.is_digit(self.val_x)
        if self.is_x_value:
            self.val_x = int(self.val_x)
        self.is_y_value = self.is_digit(self.val_y)
        if self.is_y_value:
            self.val_y = int(self.val_y)

    def operate(self, p_data):
        """ Run the operation """            
        if (self.is_x_value and self.val_x > 0) or ((not self.is_x_value) and self.val_x in p_data.memory and p_data.memory[self.val_x] != 0):
            if self.is_y_value:
                p_data.ptr += self.val_y
            else:
                if self.val_y in p_data.memory:
                    p_data.ptr += p_data.memory[self.val_y]
        else:
            p_data.ptr += 1
        return p_data.ptr

class OperationSub(Instruction):
    """add X Y decreases register X by the value of Y."""
    pattern = re.compile(r'sub (\w) (.+)')

    def __repr__(self):
        return self.repr

    def __init__(self, line):
        """ Constructor """
        self.repr = line
        match = re.match(self.pattern, line)
        self.val_x = match.group(1)
        self.val_y = match.group(2)
        self.is_value = self.is_digit(self.val_y)
        if self.is_value:
            self.val_y = int(self.val_y)

    def operate(self, p_data):
        """ Run the operation """
        if self.is_value:
            p_data.memory[self.val_x] -= self.val_y
        else:
            if self.val_y in p_data.memory:
                p_data.memory[self.val_x] -= p_data.memory[self.val_y]
            else:
                #p_data.memory[self.val_x] += 0
                p_data.memory[self.val_y] = 0
        return p_data.ptr+1

OPERATION = {
    'set': OperationSet,
    'mul': OperationMul,
    'jnz': OperationJnz,
    'sub': OperationSub,
}

class Parser(object):
    """ Program implementation """
    def __init__(self, name, data):
        """Constructor for the parser """
        self.instr = self.read_data(data.split('\n'))
        self.ptr = 0
        self.memory = defaultdict(int)
        self.name = name
        self.mulinvoked = 0

    def __repr__(self):
        """Representation of the parser """
        return "Parser_{}"# waits for {} with {} messages".format(self.name, self.needs_value, len(self.messages))

    @staticmethod
    def read_data(data):
        """ Create the proper instances of the instructions """
        return [Instruction.parse(line) for line in data]

    def process(self):
        """ Process the input data until the end"""
        condition = True
        max_ptr = len(self.instr)
        while condition:
            if self.ptr >= max_ptr or self.ptr < 0:
                condition = False
            else:
                instr = self.instr[self.ptr]
                self.ptr = instr.operate(self)
        return condition

def solution(data):
    """ Solution to the problem """
    parser = Parser(0, data)
    parser.process()
    return parser.mulinvoked

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
        DEBUG = """set b 81
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""
        print(solution(DEBUG))
