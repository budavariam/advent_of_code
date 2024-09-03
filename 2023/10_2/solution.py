""" Advent of code 2023 day 10 / 2 """

from os import path
import utils

OPP_DIRECTIONS = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W",
}
DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}
DIR_8 = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1),
]

DARK_MATTER = ","
EXPANDED_BORDER = "X"
OUTSIDE = "O"


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        for y, l in enumerate(lines):
            try:
                x = l.index("S")
                if x > -1:
                    self.curr = (y, x)
                    break
            except ValueError:
                pass
        self.start = self.curr
        self.maxw = len(lines[0])
        self.maxh = len(lines)

    def move(self, end_1, end_2, c_y, c_x, direction, symbol):
        """Move along the loop"""
        y, x = c_y, c_x
        next_d = direction
        if direction == end_1:
            # y, x = add((c_y, c_x), DIRECTIONS[end_2])
            next_d = end_2
        elif direction == end_2:
            # y, x = add((c_y, c_x), DIRECTIONS[end_1])
            next_d = end_1
        else:
            raise ValueError(
                f"  NOT PASSABLE: '{symbol}' at {(c_y, c_x)} with direction: '{direction}' (only from '{end_1}' or '{end_2}')"
            )
        return y, x, next_d

    def expand_original_map(self):
        """Rerturn the map by expanding each pixel to 3x3"""
        new_map = [
            ["" for x in range(0, self.maxw * 3)] for y in range(0, self.maxh * 3)
        ]
        for y, line in enumerate(self.lines):
            for x, symbol in enumerate(line):
                msg = ""
                match symbol:
                    case "|":
                        msg = "| is a vertical pipe connecting north and south."
                    case "-":
                        msg = "- is a horizontal pipe connecting east and west."
                    case "L":
                        msg = "L is a 90-degree bend connecting north and east."
                    case "J":
                        msg = "J is a 90-degree bend connecting north and west."
                    case "7":
                        msg = "7 is a 90-degree bend connecting south and west."
                    case "F":
                        msg = "F is a 90-degree bend connecting south and east."
                    case ".":
                        msg = ". is ground; there is no pipe in this tile."
                    case "S":
                        msg = "start is irrelevant, put in north,west,south,east"
                expanded_pixel = [
                    [
                        DARK_MATTER,
                        EXPANDED_BORDER if msg.find("north") > -1 else DARK_MATTER,
                        DARK_MATTER,
                    ],
                    [
                        EXPANDED_BORDER if msg.find("west") > -1 else DARK_MATTER,
                        EXPANDED_BORDER,
                        EXPANDED_BORDER if msg.find("east") > -1 else DARK_MATTER,
                    ],
                    [
                        DARK_MATTER,
                        EXPANDED_BORDER if msg.find("south") > -1 else DARK_MATTER,
                        DARK_MATTER,
                    ],
                ]

                for d_y in range(3):
                    for d_x in range(3):
                        new_y = y * 3
                        new_x = x * 3
                        new_map[new_y + d_y][new_x + d_x] = expanded_pixel[d_y][d_x]

        return new_map

    def step_on_matrix(
        self, curr: tuple[int, int], direction: str
    ) -> tuple[int, int, str]:
        c_y, c_x = curr
        y, x = c_y, c_x
        msg = "..."
        symbol = self.lines[c_y][c_x]
        d = direction
        match symbol:
            case "|":
                msg = "| is a vertical pipe connecting north and south."
                y, x, d = self.move("N", "S", c_y, c_x, direction, symbol)
            case "-":
                msg = "- is a horizontal pipe connecting east and west."
                y, x, d = self.move("E", "W", c_y, c_x, direction, symbol)
            case "L":
                msg = "L is a 90-degree bend connecting north and east."
                y, x, d = self.move("N", "E", c_y, c_x, direction, symbol)
            case "J":
                msg = "J is a 90-degree bend connecting north and west."
                y, x, d = self.move("N", "W", c_y, c_x, direction, symbol)
            case "7":
                msg = "7 is a 90-degree bend connecting south and west."
                y, x, d = self.move("S", "W", c_y, c_x, direction, symbol)
            case "F":
                msg = "F is a 90-degree bend connecting south and east."
                y, x, d = self.move("S", "E", c_y, c_x, direction, symbol)
            case ".":
                msg = ". is ground; there is no pipe in this tile."
                y, x, d = c_y, c_x, direction
            case "S":
                msg = "S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has."
                raise NameError(f" . START POSITION {self.curr}")
            case _:
                raise ValueError(f" . ERROR at {self.curr}")
        # print("  " + msg)

        return (y, x, d)

    def fill_expanded_map(self, map_to_fill):
        """Fill the map starting from the outside"""
        maxh = len(map_to_fill)
        maxw = len(map_to_fill[0])
        new_map = [[x for x in line] for line in map_to_fill]
        queue = []
        queue.extend([(0, x) for x in range(maxw)])
        queue.extend([(y, 0) for y in range(maxh)])
        queue.extend([(maxh-1, x) for x in range(maxw)])
        queue.extend([(y, maxw-1) for y in range(maxh)])
        visited = set()
        while queue:
            check = queue.pop()
            c_y, c_x = check
            # ignore if seen
            if check in visited:
                continue
            # ignore if nonpassable
            if new_map[c_y][c_x] == EXPANDED_BORDER:
                continue
            # find neighbors
            for d_y, d_x in DIR_8:
                next_y, next_x = add(check, (d_y, d_x))
                if (
                    next_y >= maxh
                    or next_y < 0
                    or next_x >= maxw
                    or next_x < 0
                ):
                    continue
                queue.append((next_y, next_x))
            # visit logic
            if new_map[c_y][c_x] == DARK_MATTER:
                new_map[c_y][c_x] = OUTSIDE
            visited.add(check)
        return new_map

    def persist_map(self, map_to_persist, filename="map.txt"):
        """Print the map to the filesystem"""
        with open(filename, "w", encoding="utf-8") as f:
            res = ""
            for l in map_to_persist:
                res += "".join(l)
                res += "\n"
            f.write(res)

    def count_holes(self, map_to_use):
        maxh = len(map_to_use)
        maxw = len(map_to_use[0])

        result = 0
        for y in range(0, maxh, 3):
            for x in range(0, maxw, 3):
                corners = [
                    map_to_use[y][x],
                    map_to_use[y][x + 2],
                    map_to_use[y + 2][x],
                    map_to_use[y + 2][x + 2],
                ]
                inside = all([c == DARK_MATTER for c in corners])
                if inside:
                    result += 1
        return result

    def explore_map(self, border):
        # NOTE: the txt looks awesome
        # self.persist_map(self.lines, "10_2/1.txt")
        expanded_map = self.expand_original_map()
        #self.persist_map(expanded_map, "10_2/2.txt")
        expanded_map = self.fill_expanded_map(expanded_map)
        #self.persist_map(expanded_map, "10_2/3.txt")
        hole_count = self.count_holes(expanded_map)

        return hole_count

    def solve(self):
        queue = []
        result = []
        for d in DIRECTIONS.keys():
            queue.append((self.start, d, set(self.start)))
        while queue:
            curr, next_d, border = queue.pop()
            try:
                next_y, next_x = add(curr, DIRECTIONS[next_d])
                direction = OPP_DIRECTIONS[next_d]
                # print(f"ENTERING ({next_y},{next_x}) from {direction} #{len(border)}")
                if (
                    next_y >= self.maxh
                    or next_y < 0
                    or next_x >= self.maxw
                    or next_x < 0
                ):
                    # print(f"  Over bounds!")
                    continue
                y, x, d = self.step_on_matrix((next_y, next_x), direction)
                border.add((y, x))
                queue.append(((y, x), d, border))
            except NameError:
                # print(f"  Back to start {n}, {curr}, {next_d}")
                result.append(border)
            except ValueError:
                # print(v)
                pass
        loop_items = result[0]
        # self.replace_start(loop_items)
        return self.explore_map(loop_items)


@utils.profiler
def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        data = list(line)
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
