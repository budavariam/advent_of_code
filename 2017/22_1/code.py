""" Advent of code 2017 day 22/1 """
from argparse import ArgumentParser
from collections import defaultdict
import matplotlib.pyplot as plt

class Node(object):
    """Node representation"""
    def __init__(self):
        """Constructor"""
        self.infected = False
        self.pos_x = 0
        self.pos_y = 0
        self.plotdot = None

    def infect(self, char):
        """ Set the infection to true if infected, false if not """
        self.infected = True if char == '#' else False
        return self

    def set_pos(self, pos_y, pos_x):
        """ Set the position for plotting """
        self.pos_y = pos_y
        self.pos_x = pos_x
        return self

    def plot(self):
        """ Plot a dot in the plotter """
        self.plotdot = plt.plot(self.pos_x, self.pos_y, 'ro')

    def toggle_infection(self, plot):
        """ If it was infected it cleans if it was not it gets infected """
        self.infected = not self.infected
        if self.infected and plot:
            self.plot()
        elif self.plotdot:
            self.plotdot[0].remove()
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

ARROW = {
    'n': u'$\u2191$',
    'e': u'$\u2192$',
    's': u'$\u2193$',
    'w': u'$\u2190$'
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
                current_map[(p_y, p_x)] = Node().infect(char).set_pos(p_y, p_x)
        return current_map

    @staticmethod
    def plot_infector(pos, direction):
        """ Plot an arrow facing the appropriate direction """
        return plt.plot(pos[1], pos[0], linestyle='none', marker=ARROW[direction], markersize=6)

    def simulate(self, burst_count, speed, plot):
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
        if plot:
            pauseint = 1 / speed
            plt.ion()
            fig = plt.gcf()
            current_plot = self.plot_infector(self.carrier_pos, self.carrier_dir)
            plt.pause(pauseint)
        for index in range(burst_count):
            if plot:
                current_plot[0].remove()
                fig.canvas.set_window_title('Iteration {}'.format(index))
            node = self.map[self.carrier_pos]
            node.pos_y = self.carrier_pos[0]
            node.pos_x = self.carrier_pos[1]
            self.carrier_dir = self.turn_carrier(self.carrier_dir, node.infected)
            node.toggle_infection(plot)
            if node.infected:
                self.burst_infected += 1
            self.carrier_pos = self.move_carrier(self.carrier_pos, DIRECTIONS[self.carrier_dir])
            if plot:
                current_plot = self.plot_infector(self.carrier_pos, self.carrier_dir)
                plt.pause(pauseint)

    @staticmethod
    def get_plot_points(data):
        """ Get infected node coords """
        x_coords = []
        y_coords = []
        for (p_y, p_x), node in data.items():
            if node.infected:
                x_coords.append(p_x)
                y_coords.append(p_y)
        return x_coords, y_coords

    @staticmethod
    def turn_carrier(direction, infected):
        """ Turn the carrier based on node infection """
        return TURN_RIGHT[direction] if infected else TURN_LEFT[direction]

    @staticmethod
    def move_carrier(current_pos, direction):
        """ Move the carrier to the given direction"""
        return tuple(item1 + item2 for item1, item2 in zip(current_pos, direction))

def solution(data, plot=False):
    """ Solution to the problem """
    grid = Grid(data)
    grid.simulate(10000, 10, plot)
    return grid.burst_infected

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(input_file.read(), True))
    elif ARGS.test:
        print(solution(str(ARGS.test), True))
    else:
        DEBUG = """..#
#..
..."""
        print(solution(DEBUG, True))
