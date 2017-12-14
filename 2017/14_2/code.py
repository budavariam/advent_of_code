""" Advent of code 2017 day 14/2 """
from argparse import ArgumentParser
from knot import Knot

def convert(line):
    """ Convert a line to binary representation """
    return bin(int(line, 16))[2:].zfill(128)

class Graph(object):
    """ Graph representation of the matrix """
    def __init__(self, matrix):
        """ Constructor for the object """
        self.data = self.parse_matrix(matrix)
        self.size = 128
        self.visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    @staticmethod
    def parse_matrix(matrix):
        """ Load values for the fields """
        return [[int(char) for char in line] for line in matrix]

    def count_islands(self):
        """ Count the distinct regions """
        island_count = 0
        for row in range(self.size):
            for col in range(self.size):
                if (not self.visited[row][col]) and (self.data[row][col]):
                    self.search(row, col)
                    island_count += 1
        return island_count

    def search(self, row, col):
        """ Mark the elements in the island """
        self.visited[row][col] = True
        for n_row, n_col in self.neighbours:
            if self.is_valid(row + n_row, col + n_col):
                self.search(row + n_row, col + n_col)

    def is_valid(self, row, col):
        """ A function to check if a given cell (row, col) can be included in the search """
        return (row >= 0 and row < self.size and
                col >= 0 and col < self.size and
                not self.visited[row][col] and self.data[row][col])

def solution(data):
    """ Solution to the problem """
    matrix = [convert(Knot(256, '{}-{}'.format(data, index)).knot_hash()) for index in range(128)]
    return Graph(matrix).count_islands()

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
        DEBUG = """flqrgnkx"""
        print(solution(DEBUG))
