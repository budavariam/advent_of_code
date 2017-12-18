""" Advent of code 2017 day 18/1 """
from argparse import ArgumentParser
import re
from collections import defaultdict

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

    def operate(self, memory, sounds, pointer):
        """ Abstract method for the operation """
        raise NotImplementedError

class OperationSnd(Instruction):
    """ snd X plays a sound with a frequency equal to the value of X."""
    pattern = re.compile(r'snd (\w)')

    def __repr__(self):
        return self.repr

    def __init__(self, line):
        """ Constructor """
        self.repr = line
        match = re.match(self.pattern, line)
        self.val_x = match.group(1)

    def operate(self, memory, sounds, pointer):
        """ Run the operation """
        sounds.append(memory[self.val_x])
        return None, pointer+1

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

    def operate(self, memory, sounds, pointer):
        """ Run the operation """
        if self.is_value:
            memory[self.val_x] = self.val_y
        else:
            if self.val_y in memory:
                memory[self.val_x] = memory[self.val_y]
            else:
                memory[self.val_x] = 0
                memory[self.val_y] = 0
        return None, pointer+1

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

    def operate(self, memory, sounds, pointer):
        """ Run the operation """
        if self.is_value:
            memory[self.val_x] *= self.val_y
        else:
            if self.val_y in memory:
                memory[self.val_x] *= memory[self.val_y]
            else:
                memory[self.val_x] = 0
                memory[self.val_y] = 0
        return None, pointer+1

class OperationMod(Instruction):
    """mod X Y sets register X to the remainder of dividing
    the value contained in register X by the value of Y
    (that is, it sets X to the result of X modulo Y)."""
    pattern = re.compile(r'mod (\w) (.+)')

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

    def operate(self, memory, sounds, pointer):
        """ Run the operation """
        if self.is_value:
            memory[self.val_x] %= self.val_y
        else:
            if self.val_y in memory:
                memory[self.val_x] %= memory[self.val_y]
            else:
                memory[self.val_x] = 0
                memory[self.val_y] = 0
        return None, pointer+1

class OperationRcv(Instruction):
    """rcv X recovers the frequency of the last sound played,
    but only when the value of X is not zero. (If it is zero, the command does nothing.)"""
    pattern = re.compile(r'rcv (\w)')

    def __repr__(self):
        return self.repr

    def __init__(self, line):
        """ Constructor """
        self.repr = line
        match = re.match(self.pattern, line)
        self.val_x = match.group(1)

    def operate(self, memory, sounds, pointer):
        """ Run the operation """
        recovered = None
        if self.val_x in memory and memory[self.val_x] > 0:
            print("Sound({}) is recovered because {}({}) is greater than 0"
                  .format(sounds[-1], self.val_x, memory[self.val_x]))
            recovered = sounds[-1]
        return recovered, pointer+1

class OperationJgz(Instruction):
    """jgz X Y jumps with an offset of the value of Y,
    but only if the value of X is greater than zero.
    (An offset of 2 skips the next instruction,
    an offset of -1 jumps to the previous instruction, and so on.)"""
    pattern = re.compile(r'jgz (\w) (.+)')

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

    def operate(self, memory, sounds, pointer):
        """ Run the operation """
        if self.val_x in memory and memory[self.val_x] > 0:
            if self.is_value:
                pointer += self.val_y
            else:
                if self.val_y in memory:
                    pointer += memory[self.val_y]
        else:
            pointer += 1
        return None, pointer

class OperationAdd(Instruction):
    """add X Y increases register X by the value of Y."""
    pattern = re.compile(r'add (\w) (.+)')

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

    def operate(self, memory, sounds, pointer):
        """ Run the operation """
        if self.is_value:
            memory[self.val_x] += self.val_y
        else:
            if self.val_y in memory:
                memory[self.val_x] += memory[self.val_y]
            else:
                #memory[self.val_x] += 0
                memory[self.val_y] = 0
        return None, pointer+1

OPERATION = {
    'snd': OperationSnd,
    'set': OperationSet,
    'mul': OperationMul,
    'mod': OperationMod,
    'rcv': OperationRcv,
    'jgz': OperationJgz,
    'add': OperationAdd,
}

class Parser(object):
    """ Spinlock implementation """
    def __init__(self, data):
        """Constructor for the parser """
        self.instr = self.read_data(data.split('\n'))
        self.ptr = 0
        self.memory = defaultdict(int)
        self.sounds = []

    def __repr__(self):
        """Representation of the parser """
        return "Parser"

    @staticmethod
    def read_data(data):
        """ Create the proper instances of the instructions """
        return [Instruction.parse(line) for line in data]

    def process(self):
        """ Process the input data """
        recovered = False
        while not recovered:
            instr = self.instr[self.ptr]
            recovered, self.ptr = instr.operate(self.memory, self.sounds, self.ptr)
        return recovered

def solution(data):
    """ Solution to the problem """
    parser = Parser(data)
    parser.process()
    return parser.sounds[-1]

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
        DEBUG = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""
        print(solution(DEBUG))
