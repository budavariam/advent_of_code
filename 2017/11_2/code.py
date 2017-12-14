""" Advent of code 2017 day 11/2 """
from argparse import ArgumentParser

class HexGrid(object):
    """ Representation of the infinite grid """
    def __init__(self, travel):
        """ Constructor of the grid """
        self.data = self.parse_input(travel)
        self.steps = {
            'sw': 0,
            'se': 0,
            's': 0,
            'nw': 0,
            'ne': 0,
            'n': 0
        }
        self.directions = {
            'sw': (-1, 0),
            'se': (1, -1),
            's': (0, -1),
            'nw': (-1, +1),
            'ne': (+1, 0),
            'n': (0, 1)
        }

    @staticmethod
    def parse_input(data):
        """ Load the travel data """
        return data.split(',')

    @staticmethod
    def distance(start, end):
        """ Calculate distance """
        z_start = 0-sum(start)
        z_end = 0-sum(end)
        return max(end[0] - start[0], end[1] - start[1], z_end - z_start)

    def furthest_distance(self):
        """ Count the different directions """
        start = (0, 0)
        current = (0, 0)
        dist = 0
        furthest_distance = -1
        for direction in self.data:
            self.steps[direction] += 1
            current = tuple(map(sum, zip(current, self.directions[direction])))
            dist = self.distance(start, current)
            furthest_distance = max(dist, furthest_distance)
        return furthest_distance

def solution(input_data):
    """ Solution to the problem """
    return HexGrid(input_data).furthest_distance()

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
        DEBUG = """se,sw,se,sw,sw"""
        print(solution(DEBUG))
