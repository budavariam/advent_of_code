""" Advent of code 2020 day 11/1 """

import math
from os import path

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def get_neighbours(start_y, start_x):
    return [(start_y-y, start_x-x) for y in range(-1, 2) for x in range(-1, 2) if (x, y) != (0, 0)]


class Simulation(object):
    def __init__(self, seats, dim_y, dim_x):
        self.seats = seats
        self.dim_y = dim_y
        self.dim_x = dim_x

    def calc_adjacent_occupied(self, seats, y, x):
        return sum([1 if seats.get(index) == OCCUPIED else 0 for index in get_neighbours(y, x)])

    def calc_movements(self, seats):
        changed_positions = 0
        new_state = {}
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                prev_seat = seats[(y, x)]
                next_seat = FLOOR
                if prev_seat == OCCUPIED:
                    if self.calc_adjacent_occupied(seats, y, x) >= 4:
                        next_seat = EMPTY
                        changed_positions += 1
                    else:
                        next_seat = OCCUPIED
                if prev_seat == EMPTY:
                    if self.calc_adjacent_occupied(seats, y, x) == 0:
                        next_seat = OCCUPIED
                        changed_positions += 1
                    else:
                        next_seat = EMPTY
                new_state[(y, x)] = next_seat
        return new_state, changed_positions

    def print_map(self):
        for y in range(self.dim_y):
            line = ''
            for x in range(self.dim_x):
                line += self.seats.get((y, x))
            print(line)
        print("-" * self.dim_y)

    def calc_occupied(self):
        return list(self.seats.values()).count(OCCUPIED)

    def solve(self):
        shouldContinue = True
        # self.print_map()
        while shouldContinue:
            newState, changed_seats = self.calc_movements(self.seats)
            shouldContinue = changed_seats > 0
            self.seats = newState
            # self.print_map()
        return self.calc_occupied()


def preprocess(raw_data):
    lines = raw_data.split("\n")
    seatmap = {}
    dim_y, dim_x = len(lines), len(lines[0])
    for y, line in enumerate(lines):
        for x, seat in enumerate(line):
            seatmap[(y, x)] = seat
    return (seatmap, dim_y, dim_x)


def solution(data):
    """ Solution to the problem """
    seats, dim_y, dim_x = preprocess(data)
    solver = Simulation(seats, dim_y, dim_x)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
