""" Advent of code 2017	day 9/1	"""

from argparse import ArgumentParser
from enum import Enum
from functools import reduce

VERBOSE = False

class State(Enum):
    """ State for the Stream """
    GARBAGED = 1
    ESCAPED = 2
    NORMAL = 3

class Stream(object):
    """ Stream of data that has garbage """

    def enter_escaped(self):
        """ Set to escaped state and save the prev state if appropriate """
        if VERBOSE:
            print("--enter_escaped")
        if self.state != State.ESCAPED:
            self.prev_nonesc_state = self.state
        self.state = State.ESCAPED

    def leave_escaped(self):
        """ Leave escaped mode """
        if VERBOSE:
            print("--leave_escaped")
        self.state = self.prev_nonesc_state

    def enter_group(self):
        """ Entered into a new group in normal mode"""
        if VERBOSE:
            print("--enter_group")
        self.group_level += 1
        self.groups.append(self.group_level)

    def leave_group(self):
        """ Leave a group in normal mode """
        if VERBOSE:
            print("--leave_group")
        self.group_level -= 1

    def enter_garbage(self):
        """ Enter garbage mode """
        if VERBOSE:
            print("--enter_garbage")
        self.state = State.GARBAGED
        self.prev_nonesc_state = State.GARBAGED

    def leave_garbage(self):
        """ Leave garbage mode """
        if VERBOSE:
            print("--leave_garbage")
        self.normal_mode()

    def normal_mode(self):
        """ Leave garbage mode """
        if VERBOSE:
            print("--normal_mode")
        self.state = State.NORMAL
        self.prev_nonesc_state = State.NORMAL

    def __repr__(self):
        return "{}({}) level:{} groups: {}".format(
            self.state,
            self.prev_nonesc_state,
            self.group_level,
            self.groups)

    def process_data(self):
        """ Process the text in the stream """
        for char in self.data:
            if VERBOSE:
                print("{} - {}".format(char, self))
            if self.state == State.ESCAPED:
                self.leave_escaped()
            elif self.state == State.GARBAGED:
                if char in self.garbaged_behaviour:
                    self.garbaged_behaviour[char]()
            elif self.state == State.NORMAL:
                if char in self.normal_behaviour:
                    self.normal_behaviour[char]()
        if VERBOSE:
            print(self)

    def total_score(self):
        """ return the total score of the groups """
        return reduce(lambda acc, elem: acc + elem, self.groups, 0)

    def __init__(self, input_data):
        """ Constructor for stream """
        self.data = input_data
        self.prev_nonesc_state = State.NORMAL
        self.state = State.NORMAL
        self.group_level = 0
        self.groups = []

        self.normal_behaviour = {
            '{': self.enter_group,
            '}': self.leave_group,
            '<': self.enter_garbage
        }
        self.garbaged_behaviour = {
            '!': self.enter_escaped,
            '>': self.leave_garbage
        }

        self.process_data()

def solution(input_data):
    """ Solution to the problem """
    stream = Stream(input_data)
    return stream.total_score()

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
        DEBUG = """{{<ab>},{<ab>},{<ab>},{<ab>}}"""
        print(solution(DEBUG))
