""" Advent of code 2020 day 17/1 """

import math
from os import path

STATE_ACTIVE = '#'
STATE_INACTIVE = '.'


def get_neighbours(start_z, start_y, start_x):
    return [
        (start_z-z, start_y-y, start_x-x)
        for z in range(-1, 2)
        for y in range(-1, 2)
        for x in range(-1, 2)
        if (z, x, y) != (0, 0, 0)
    ]


class Simulation(object):
    def __init__(self, parsed_data):
        cubes, dim_z, dim_y, dim_x = parsed_data
        self.cubes = cubes
        self.dim_z = dim_z
        self.dim_y = dim_y
        self.dim_x = dim_x

    def calc_adjacent_space(self, cubes, z, y, x):
        return sum([1 if cubes.get(index) == STATE_ACTIVE else 0 for index in get_neighbours(z, y, x)])

    def calc_next_state(self, is_active, active_neighbour_count):
        """
        If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
        If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
        """
        if is_active:
            return STATE_ACTIVE if (2 <= active_neighbour_count <= 3) else STATE_INACTIVE

        return STATE_ACTIVE if (active_neighbour_count == 3) else STATE_INACTIVE

    def simulate_step(self, iteration, cubes):
        new_state = {}
        for z in range(-iteration, iteration + 1):
            for y in range(-iteration, iteration + self.dim_y):
                for x in range(-iteration, iteration + self.dim_x):
                    prev_state = cubes.get((z, y, x))
                    if prev_state is None:
                        prev_state = STATE_INACTIVE
                    neighbour_count = self.calc_adjacent_space(cubes, z, y, x)
                    next_state = self.calc_next_state(
                        prev_state == STATE_ACTIVE, neighbour_count)
                    new_state[(z, y, x)] = next_state
        return new_state

    def calc_cubes(self):
        return list(self.cubes.values()).count(STATE_ACTIVE)

    def print_map(self, iteration, cubes):
        for z in range(-iteration, iteration + 1):
            print(f"Z: {z}")
            for y in range(-iteration, iteration + self.dim_y):
                line = ''
                for x in range(-iteration, iteration + self.dim_x):
                    cube = cubes.get((z, y, x))
                    line += cube if cube is not None else STATE_INACTIVE
                print(line)
        print("-" * (self.dim_y + 2 * iteration))
        print("PRESS Enter to continue...")
        input()

    def solve(self):
        for iteration in range(1, 7):
            # self.print_map(iteration, self.cubes)
            newState = self.simulate_step(iteration, self.cubes)
            self.cubes = newState
        return self.calc_cubes()


def preprocess(raw_data):
    lines = raw_data.split("\n")
    pocketdimension = {}
    z = 0
    dim_z, dim_y, dim_x = 1, len(lines), len(lines[0])
    for y, line in enumerate(lines):
        for x, cube in enumerate(line):
            pocketdimension[(z, y, x)] = cube
    return (pocketdimension, dim_z, dim_y, dim_x)


def solution(raw_data):
    """ Solution to the problem """
    parsed_data = preprocess(raw_data)
    solver = Simulation(parsed_data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
