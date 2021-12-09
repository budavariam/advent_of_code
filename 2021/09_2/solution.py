""" Advent of code 2021 day 09 / 2 """

from os import path
import math

pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.height = len(lines)
        self.width = len(lines[0])

    def fillpos(self, y, x):
        pl = []
        for (dy, dx) in pos:
            ny = dy+y
            nx = dx + x
            np = (ny, nx)
            if ny >= 0 and ny < self.height and nx >= 0 and nx < self.width:
                pl.append(np)
        return pl

    def lowpoints(self):
        lst = []

        for y, row in enumerate(self.lines):
            for x, c in enumerate(row):
                # print(c)
                shouldadd = [
                    self.lines[ny][nx] > c
                    for [ny, nx]
                    in self.fillpos(y, x)
                ]
                if all(shouldadd):
                    # print(c)
                    lst.append((y, x))
        return lst

    def basin(self, y, x):
        res = 0
        visited = set()
        pl = self.fillpos(y, x)
        while len(pl) > 0:
            nc = pl.pop()
            [ny, nx] = nc
            # print("visit", nc)
            if nc in visited:
                # print("seen", nc)
                continue
            if self.lines[ny][nx] == 9:
                # print("wall", nc)
                continue
            res += 1
            visited.add(nc)
            newcoords = self.fillpos(ny, nx)
            pl += newcoords
            # print("added", res, newcoords, pl)
        # print("finished", res)
        return res

    def solve(self):
        # print(self.lines)
        lp = self.lowpoints()
        sizes = [self.basin(y, x) for [y, x] in lp]
        return math.prod(sorted(sizes, reverse=True)[:3])


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line
        processed_data.append(list(map(int, data)))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
