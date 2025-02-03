""" Advent of code 2024 day 14 / 2 """

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
        items = set([p for p,_ in positions])
        for y in range(0, self.h):
            line = ""
            for x in range(0, self.w):
                if (x, y) in items:
                    line += "x"
                else:
                    line += "."
            print(line)
        print("-----")

    def find_easter_egg(self, positions):
        items = set([p for p,_ in positions])
        cnt = 0
        for curr in items:
            l_l = add(curr, (-1, 1))
            l_m = add(curr, (0, 1))
            l_r = add(curr, (1, 1))
            if all(map(lambda x: x in items, [l_l, l_m, l_r])):
                cnt += 1
        return cnt >= (len(items) // 4)

    def solve(self):
        # pprint(self.lines)
        positions = self.lines
        t = 0
        condition = False
        while not condition:
            if t%100 == 0:
                print(t)
            t+=1
            new_positions = []
            for p,v in positions:
                n_x, n_y = self.calc_pos(p, v, 1)
                new_positions.append(((n_x, n_y), v))
            condition = self.find_easter_egg(new_positions)
            positions = new_positions
            if condition:
                self.print_map(positions)
        return t
    
    

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
