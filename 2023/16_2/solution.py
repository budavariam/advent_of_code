""" Advent of code 2023 day 16 / 1 """

from pprint import pprint
from os import path
from collections import deque
import utils

DIRECTIONS = {  # Y, X
    "N": (-1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
}


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Photon(object):
    def __init__(self, pos, direction, max_y, max_x) -> None:
        self.pos = pos
        self.direction = direction
        self.active = True
        self.max_y = max_y
        self.max_x = max_x

    def __repr__(self) -> str:
        return f"{self.pos} - {self.direction}({'+' if self.active else '.'})"

    def move(self, matrix):
        is_valid = False
        spawns = []
        y, x = self.pos
        if not (0 <= y < self.max_y and 0 <= x < self.max_x):
            self.active = False
            return is_valid, spawns
        curr_tile = matrix[y][x]

        if curr_tile == ".":
            # If the beam encounters empty space (.), it continues in the same direction.
            next_coord = add(self.pos, DIRECTIONS[self.direction])
            is_valid = (
                0 <= next_coord[0] < self.max_y and 0 <= next_coord[1] < self.max_x
            )
            spawns = []
            self.pos = next_coord
        elif curr_tile == "\\":
            # If the beam encounters a mirror (/ or \), the beam is reflected
            # 90 degrees depending on the angle of the mirror. For instance,
            # a rightward-moving beam that encounters a / mirror would
            # continue upward in the mirror's column, while a rightward-moving
            # beam that encounters a \ mirror would continue downward
            # from the mirror's column.
            mirror_bwslash = {
                "N": "W",
                "W": "N",
                "E": "S",
                "S": "E",
            }
            self.direction = mirror_bwslash[self.direction]
            next_coord = add(self.pos, DIRECTIONS[self.direction])
            is_valid = (
                0 <= next_coord[0] < self.max_y and 0 <= next_coord[1] < self.max_x
            )
            spawns = []
            self.pos = next_coord
        elif curr_tile == "/":
            mirror_slash = {
                "N": "E",
                "E": "N",
                "W": "S",
                "S": "W",
            }
            self.direction = mirror_slash[self.direction]
            next_coord = add(self.pos, DIRECTIONS[self.direction])
            is_valid = (
                0 <= next_coord[0] < self.max_y and 0 <= next_coord[1] < self.max_x
            )
            self.pos = next_coord

            spawns = []
        elif curr_tile == "-":
            # If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter
            # as if the splitter were empty space. For instance, a rightward-moving beam that encounters
            # a - splitter would continue in the same direction.
            # If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams
            # going in each of the two directions the splitter's pointy ends are pointing. For instance,
            # a rightward-moving beam that encounters a | splitter would split into two beams:
            # one that continues upward from the splitter's column
            # and one that continues downward from the splitter's column.
            horizontal_splitter = {
                "N": ["W", "E"],
                "W": ["W"],
                "E": ["E"],
                "S": ["W", "E"],
            }
            is_valid = False
            spawns = []
            for new_dir in horizontal_splitter[self.direction]:
                new_pos = add(self.pos, DIRECTIONS[new_dir])
                if 0 <= new_pos[0] < self.max_y and 0 <= new_pos[1] < self.max_x:
                    spawns.append(Photon(new_pos, new_dir, self.max_y, self.max_x))
        elif curr_tile == "|":
            vertical_splitter = {
                "N": ["N"],
                "W": ["N", "S"],
                "E": ["N", "S"],
                "S": ["S"],
            }
            is_valid = False
            spawns = []
            for new_dir in vertical_splitter[self.direction]:
                new_pos = add(self.pos, DIRECTIONS[new_dir])
                if 0 <= new_pos[0] < self.max_y and 0 <= new_pos[1] < self.max_x:
                    spawns.append(Photon(new_pos, new_dir, self.max_y, self.max_x))
        return is_valid, spawns


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def print_map(self, visited):
        empowered_map = []
        count = 0
        for y, line in enumerate(self.lines):
            new_line = []
            for x, c in enumerate(line):
                # if c == ".":
                v = (y, x) in visited
                count += 1 if v else 0
                new_line.append("#" if v else ".")
                # else:
                #     new_line.append(c)
            empowered_map.append(new_line)
        # print("....")
        # for line in empowered_map:
        #     print(line)
        # print("....")
        print(count)

    def solve(self):
        result = 0
        max_y = len(self.lines)
        max_x = len(self.lines[0])
        starts = [
            ("N", zip([max_y] * max_x, range(max_x))),
            ("S", zip([0] * max_y, range(max_x))),
            ("E", zip(range(max_y), [0] * max_x)),
            ("W", zip(range(max_y), [max_x] * max_x)),
        ]

        for start_dir, start_range in starts:
            for start_y, start_x in start_range:
                result = max(
                    result,
                    self.calc_power(
                        Photon((start_y, start_x), start_dir, max_y, max_x)
                    ),
                )
        return result

    def calc_power(self, init_photon):
        # pprint(self.lines)
        visited = set([])
        cache = set([])
        beams = deque([init_photon])
        inactive_beams = []
        i = 0
        while len(beams) > 0:
            i += 1
            curr = beams.popleft()
            cache_key = (curr.direction, curr.pos[0], curr.pos[1])
            if cache_key in cache:
                continue
            if curr.active:
                visited.add(curr.pos)
            cache.add(cache_key)
            is_valid, spawns = curr.move(self.lines)
            beams.extend(spawns)
            if not is_valid:
                inactive_beams.append(curr)
            else:
                beams.append(curr)

        # print(visited)
        result = len(visited)
        return result


@utils.profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = line
        processed_data.append(data)
    return processed_data


@utils.profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        print(solution(input_file.read()))
