""" Advent of code 2024 day 14 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import defaultdict
from utils import log, profiler

def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Code(object):
    def __init__(self, lines, w=0, h=0):
        self.lines = lines
        self.w = w
        self.h = h
        self.y_axis = self.w // 2 
        self.x_axis = self.h // 2 

    def calc_pos(self, pos, vel, t):
        pos_x, pos_y = pos
        vel_x, vel_y = vel

        new_pos = ((pos_x + vel_x * t) % self.w,
                    (pos_y + vel_y * t) % self.h)
        
        return new_pos

    def print_map(self, positions):
        items = set(positions)
        for y in range(0, self.h):
            line = ""
            for x in range(0, self.w):
                if (x, y) in items:
                    line += "x"
                else:
                    line += "."
            print(line)
        print("-----")

    def sort_to_quadrants(self, positions):
        quadrant_count = [0,0,0,0]
        for x,y in positions:
            x_l = 0 <= x < self.y_axis
            x_r = self.y_axis < x < self.w
            y_t = 0 <= y < self.x_axis
            y_b = self.x_axis < y < self.h
            quadrant_index = 0
            if x_l and y_t:
                quadrant_index = 0
            elif x_r and y_t:
                quadrant_index = 1
            elif x_l and y_b:
                quadrant_index = 2
            elif x_r and y_b:
                quadrant_index = 3
            else:
                raise(Exception(f"Failed to determine quadrant: ({x},{y}) {[x_l, x_r, y_t, y_b]} ({self.w},{self.h})"))
            
            quadrant_count[quadrant_index] += 1
        return quadrant_count

    def solve(self):
        # pprint(self.lines)
        positions = []
        step = 100
        for p,v in self.lines:
            n_x, n_y = self.calc_pos(p, v, step)
            if n_x == self.y_axis or n_y == self.x_axis:
                continue
            positions.append((n_x, n_y))
        # self.print_map(positions)
        quadrant_positions = self.sort_to_quadrants(positions)
        return math.prod(quadrant_positions)
    
    

def parse_tuple(input_str):
    return tuple(map(int, input_str.split(",")))    

@profiler
def preprocess(raw_data):
    pattern = re.compile(r'^p=([0-9,\-]+) v=([0-9,\-]+)$')
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = tuple(map(parse_tuple, [match.group(1), match.group(2)]))
        processed_data.append(data)
    return processed_data


@profiler
def solution(data, bounds):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines, bounds[0], bounds[1])
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read(), (101, 103)))
