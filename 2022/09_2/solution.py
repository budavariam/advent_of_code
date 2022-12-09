""" Advent of code 2022 day 09 / 2 """

from os import path
from collections import defaultdict

dirs = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}


def mv(a, b):
    return (a[0] + b[0], a[1] + b[1])


def calcdist(pos):
    hy, hx = pos["H"]
    ty, tx = pos["T"]

    return abs(hx - tx) + abs(hy - ty)


def follow(head, tail):
    # adjust tail
    # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

    # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
    dist_y = head[0] - tail[0]
    dist_x = head[1] - tail[1]
    res = tail
    if abs(dist_y) <= 1 and abs(dist_x) <= 1:
        pass
    elif abs(dist_y) >= 2 and abs(dist_x) >= 2:
        # diagonal
        n_ty = head[0] - 1 if tail[0] < head[0] else head[0] + 1
        n_tx = head[1] - 1 if tail[1] < head[1] else head[1] + 1
        res = (n_ty, n_tx)
    elif abs(dist_y) >= 2:
        # move_y
        n_ty = head[0] - 1 if tail[0] < head[0] else head[0] + 1
        n_tx = head[1]
        res = (n_ty, n_tx)
    elif abs(dist_x) >= 2:
        # move_x
        n_ty = head[0]
        n_tx = head[1] - 1 if tail[1] < head[1] else head[1] + 1
        res = (n_ty, n_tx)
    return res


def move(direction, visited, pos):
    # print(direction, visited, pos)
    pos["H"] = mv(pos["H"], dirs[direction])
    prev = "H"
    for kid in range(1, 9 + 1):
        knot_id = str(kid)
        pos[knot_id] = follow(pos[prev], pos[knot_id])
        visited[knot_id].add(pos[knot_id])
        prev = knot_id
    return visited, pos


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # print(self.lines)
        visited = defaultdict(set)
        pos = {
            "H": (0, 0),
            "1": (0, 0),
            "2": (0, 0),
            "3": (0, 0),
            "4": (0, 0),
            "5": (0, 0),
            "6": (0, 0),
            "7": (0, 0),
            "8": (0, 0),
            "9": (0, 0),
        }
        # places the tail visited
        for (direction, num) in self.lines:
            for _ in range(num):
                visited, pos = move(direction, visited, pos)

        return len(visited["9"])


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = line.split(" ")
        data[1] = int(data[1])
        processed_data.append(data)
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
