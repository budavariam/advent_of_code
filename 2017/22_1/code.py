""" Advent of code 2017 day 22/1 """
from argparse import ArgumentParser
from collections import defaultdict

class Node(object):
    """Node representation"""
    def __init__(self):
        """Constructor"""
        self.infected = False

    def infect(self, char):
        """ Set the infection to true if infected, false if not """
        self.infected = True if char == '#' else False
        return self

    def toggle_infection(self):
        """ If it was infected it cleans if it was not it gets infected """
        self.infected = not self.infected
        return self.infected

    def __repr__(self):
        """ Representation of the node """
        return "Node({})".format('#' if self.infected else '.')

DIRECTIONS = {
    's': (-1, 0),
    'n': (1, 0),
    'e': (0, 1),
    'w': (0, -1)
}
TURN_LEFT = {
    'n': 'w',
    'e': 'n',
    's': 'e',
    'w': 's'
}
TURN_RIGHT = {
    'n': 'e',
    'e': 's',
    's': 'w',
    'w': 'n'
}

class Grid(object):
    """ Fractal representation """
    def __init__(self, data):
        """Constructor"""
        current_map = self.read_data(data)
        self.map = current_map
        self.carrier_pos = (0, 0)
        self.carrier_dir = 'n'
        self.burst_infected = 0

    def __repr__(self):
        """ representation of the Grid """
        return "Grid({})".format(self.carrier_pos)

    @classmethod
    def read_data(cls, data):
        """ Read the data from the input """
        input_map = data.split('\n')
        width = len(input_map[0])
        height = len(input_map)
        start = (width//2 + 1, height//2 + 1)
        current_map = defaultdict(Node)
        for i_y, line in enumerate(input_map):
            p_y = start[1] - (i_y + 1)
            for i_x, char in enumerate(line):
                p_x = (i_x - start[0]) + 1
                current_map[(p_y, p_x)] = Node().infect(char)
        return current_map

    def simulate(self, burst_count):
        """ Simulate the bursts of activities
                * If the current node is infected, it turns to its right.
                  Otherwise, it turns to its left.
                  (Turning is done in-place; the current node does not change.)
                * If the current node is clean, it becomes infected.
                  Otherwise, it becomes cleaned.
                  (This is done after the node is considered
                   for the purposes of changing direction.)
                * The virus carrier moves forward one node in the direction it is facing.
        """
        for _ in range(burst_count):
            node = self.map[self.carrier_pos]
            self.carrier_dir = self.turn_carrier(self.carrier_dir, node.infected)
            node.toggle_infection()
            if node.infected:
                self.burst_infected += 1
            self.carrier_pos = self.move_carrier(self.carrier_pos, DIRECTIONS[self.carrier_dir])

    @staticmethod
    def turn_carrier(direction, infected):
        """ Turn the carrier based on node infection """
        return TURN_RIGHT[direction] if infected else TURN_LEFT[direction]

    @staticmethod
    def move_carrier(current_pos, direction):
        """ Move the carrier to the given direction"""
        return tuple(item1 + item2 for item1, item2 in zip(current_pos, direction))

def solution(data):
    """ Solution to the problem """
    grid = Grid(data)
    grid.simulate(10000)
    return grid.burst_infected

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
        DEBUG = """..#
#..
..."""
        print(solution(DEBUG))
