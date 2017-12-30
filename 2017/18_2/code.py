""" Advent of code 2017 day 18/2 """
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

    def operate(self, p_data):
        """ Run the operation """
        p_data.sent += 1
        p_data.messages.append(p_data.memory[self.val_x])
        return None, p_data.ptr+1

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
        return None, p_data.ptr+1

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
        if self.is_value:
            p_data.memory[self.val_x] *= self.val_y
        else:
            if self.val_y in p_data.memory:
                p_data.memory[self.val_x] *= p_data.memory[self.val_y]
            else:
                p_data.memory[self.val_x] = 0
                p_data.memory[self.val_y] = 0
        return None, p_data.ptr+1

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

    def operate(self, p_data):
        """ Run the operation """
        if self.is_value:
            p_data.memory[self.val_x] %= self.val_y
        else:
            if self.val_y in p_data.memory:
                p_data.memory[self.val_x] %= p_data.memory[self.val_y]
            else:
                p_data.memory[self.val_x] = 0
                p_data.memory[self.val_y] = 0
        return None, p_data.ptr+1

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

    def operate(self, p_data):
        """ Run the operation """
        return self.val_x, p_data.ptr+1

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
        self.is_x_value = self.is_digit(self.val_x)
        if self.is_x_value:
            self.val_x = int(self.val_x)
        self.is_y_value = self.is_digit(self.val_y)
        if self.is_y_value:
            self.val_y = int(self.val_y)

    def operate(self, p_data):
        """ Run the operation """            
        if (self.is_x_value and self.val_x > 0) or ((not self.is_x_value) and self.val_x in p_data.memory and p_data.memory[self.val_x] > 0):
            if self.is_y_value:
                p_data.ptr += self.val_y
            else:
                if self.val_y in p_data.memory:
                    p_data.ptr += p_data.memory[self.val_y]
        else:
            p_data.ptr += 1
        return None, p_data.ptr

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

    def operate(self, p_data):
        """ Run the operation """
        if self.is_value:
            p_data.memory[self.val_x] += self.val_y
        else:
            if self.val_y in p_data.memory:
                p_data.memory[self.val_x] += p_data.memory[self.val_y]
            else:
                #p_data.memory[self.val_x] += 0
                p_data.memory[self.val_y] = 0
        return None, p_data.ptr+1

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
    """ Program implementation """
    def __init__(self, name, data):
        """Constructor for the parser """
        self.instr = self.read_data(data.split('\n'))
        self.ptr = 0
        self.memory = defaultdict(int)
        self.name = name
        self.memory['p'] = name
        self.waiting = False
        self.messages = deque()
        self.needs_value = None
        self.sent = 0

    def __repr__(self):
        """Representation of the parser """
        return "Parser_{}"# waits for {} with {} messages".format(self.name, self.needs_value, len(self.messages))

    @staticmethod
    def read_data(data):
        """ Create the proper instances of the instructions """
        return [Instruction.parse(line) for line in data]

    def process(self):
        """ Process the input data until needs to wait"""
        while not self.needs_value:
            instr = self.instr[self.ptr]
            self.needs_value, self.ptr = instr.operate(self)
        self.waiting = True

    def cont(self, value):
        """ Continue the processing with the necessary value """
        self.memory[self.needs_value] = value
        self.waiting = False
        self.needs_value = None
        self.process()

class Operator(object):
    """ Operator object to run two parsers """
    def __init__(self, data):
        """ Constructor of the operator """
        self.p_a = Parser(0, data)
        self.p_b = Parser(1, data)

    def __repr__(self):
        return "Operator"

    def run(self):
        """ Run the programs """
        cond = True
        self.p_a.process()
        self.p_b.process()
        index = 0
        while cond:
            index += 1
            if index % 100000 == 0:
                print(index)
            if self.p_a.waiting and not self.p_b.messages and \
               self.p_b.waiting and not self.p_a.messages:
                cond = False
            else:
                if self.p_a.waiting and self.p_b.messages:
                    self.p_a.cont(self.p_b.messages.popleft())
                    #print(self.p_a)
                if self.p_b.waiting and self.p_a.messages:
                    self.p_b.cont(self.p_a.messages.popleft())
                    #print(self.p_b)
        return self.p_b.sent

def solution(data):
    """ Solution to the problem """
    return Operator(data).run()

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
        DEBUG = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
        print(solution(DEBUG))
