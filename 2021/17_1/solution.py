""" Advent of code 2021 day 17 / 1 """

import math
from os import path
import re


class Code(object):
    def __init__(self, lines):
        self.target = lines[0]  # xa xb ya yb

    def printmap(self, pts):
        ly, lx = set(), set()
        for [y,x] in pts:
            ly.add(y)
            lx.add(x)
        for y in range(max(ly), min(ly)-1, -1):
            line = ""
            for x in range(min(lx), max(lx)+1):
                line += "#" if (y,x) in pts else " "
            print(line)

    def step(self, curr, velocity):
        [y_v, x_v] = velocity
        curr[0] += y_v
        curr[1] += x_v
        velocity[0] -= 1
        velocity[1] -= 0 if x_v == 0 else (1 if x_v > 0 else -1)
        return curr, velocity

    def search(self, v_y, v_x):
        # print(f"Initial velocity: {v_y}, {v_x}")
        curr = [0, 0]  # y,x
        velocity = [v_y, v_x]
        t_points = {}
        path = set()
        for y in range(self.target[2], self.target[3]):
            for x in range(self.target[0], self.target[1]):
                t_points[(y, x)] = True
        found = False
        can_find = True
        t_points[(curr[0], curr[1])] = True
        i = 0
        while not found and can_find:
            i += 1
            curr, velocity = self.step(curr, velocity)
            path.add(curr[0])
            # print(f"Initial velocity: {v_y}, {v_x}")
            # print(f"Current pos: {curr[0]}, {curr[1]}")
            # print(f"Current velocity: {velocity[0]}, {velocity[1]}")
            # print(f"Target: {self.target}")
            t_points[(curr[0], curr[1])] = True
            # self.printmap(t_points)

            if (curr[1] >= self.target[0] 
                and curr[1] <= self.target[1] 
                and curr[0] >= self.target[2]
                and curr[0] <= self.target[3]):
                found = True
                can_find = True
                print(f"Found: {v_y}, {v_x}, {max(path)}")
            elif (curr[1] > self.target[1] 
                and curr[0] < self.target[3]):
                # print(f"Can not find1: {v_y}, {v_x}")
                can_find = False
            elif (velocity[1] == 0 and curr[1] < self.target[0]):
                # print(f"Can not find2: {v_y}, {v_x}")
                can_find = False
            elif i == 1000:
                print("OVERSHOOT", velocity, curr)
                can_find = False
        return found, max(path)

    def solve(self):
        # print(self.lines)
        res = set()
        # for [x,y] in [
        #          (6,9)
        #         ,(7,2)
        #         ,(6,3)
        #         ,(9,0)
        #         ,(17,-4)
        # ]:
        for y in range(1,217):
            for x in range(1, 217):
                r_f, r_y = self.search(y,x)
                if r_f:
                    res.add(r_y)
        return max(res)

def preprocess(raw_data):
    pattern = re.compile(
        r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = [
            int(match.group(1)), int(match.group(2)), int(
                match.group(3)), int(match.group(4))
        ]
        processed_data.append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
