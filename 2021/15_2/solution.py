""" Advent of code 2021 day 15 / 2 """

import math
from os import path
import heapq as hq

pos = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    # (-1, 1), (-1, -1), (1, -1), (1, 1)
]


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.height = len(lines)
        self.width = len(lines[0])

        largemap = []
        for y in range(5 * self.height):
            line = []
            for x in range(5 * self.width):
                # position in original
                o_y = y % self.height
                o_x = x % self.width
                # which tile are we looking at
                tile_y = math.floor(y / self.height)
                tile_x = math.floor(x / self.width)
                # new value
                n_t = self.lines[o_y][o_x] + tile_x + tile_y
                line.append(((n_t - 1) % 9) + 1)
            largemap.append(line)

        self.lines = largemap
        self.height = len(largemap)
        self.width = len(largemap[0])

    def fillpos(self, y, x):
        pl = []
        for (dy, dx) in pos:
            ny = dy + y
            nx = dx + x
            np = (ny, nx)
            if ny >= 0 and ny < self.height and nx >= 0 and nx < self.width:
                pl.append(np)
        return pl

    def printlines(self, msg):
        print(msg)
        for line in self.lines:
            print("".join([str(x) for x in line]))

    def paths(self, s, e):
        deq = [(0, s)]

        while deq:
            [c_risk, c_pos] = hq.heappop(deq)
            if c_pos == e:
                # greedy get last item
                return c_risk
            y, x = c_pos
            next_pos = self.fillpos(y, x)
            for neighbour in next_pos:
                n_y, n_x = neighbour
                chk = self.lines[n_y][n_x]
                if chk >= 0:
                    # consider onlz visited numbers, and keep the added values within 1-9
                    newrisk = (c_risk + ((chk-1) % 9)) + 1
                    hq.heappush(deq, (newrisk, neighbour))
                    # mark visited
                    self.lines[n_y][n_x] = -1
        return None

    def solve(self):
        # print(self.lines)
        # self.printlines("")
        return self.paths((0, 0), (self.height-1, self.width-1))


def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = line
        processed_data.append([int(x) for x in data])
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
