""" Advent of code 2020 day 20/2 """

import math
import re
from os import path

seamonster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]


def turn(lines, turns):
    if turns == 0:
        return lines
    elif turns == 2:
        return [line[::-1] for line in reversed(lines)]
    elif turns == 1:
        turn = []
        for y in range(len(lines)):
            turn.append(''.join([line[y] for line in reversed(lines)]))
        return turn
    elif turns == 3:
        turn = []
        for y in range(len(lines)):
            turn.append(''.join([line[y] for line in lines]))
        return turn
    return lines


def rotate_all(lines):
    return [
        *[
            turn(lines, turn_cnt)
            for turn_cnt in range(4)
        ],
        *[
            turn([line[::-1] for line in lines], turn_cnt)
            for turn_cnt in range(4)
        ],
    ]


class Code(object):
    def __init__(self, data):
        self.data = data

    def generate_picture(self):
        data, borders, border_connections, flips = self.data
        final_picture_size = int(len(data.keys())**0.5)
        picture = [[[] for x in range(final_picture_size)]
                   for y in range(final_picture_size)]
        used = None
        for current_index, current_flip in flips.items():
            if border_connections[current_index] == min(border_connections.values()):
                others = sum([other_border for other_index, other_border in borders.items(
                ) if current_index != other_index], [])
                for flip_border in current_flip:
                    if ''.join([d[-1] for d in flip_border]) in others and flip_border[-1] in others:
                        picture[0][0] = flip_border
                        used = set([current_index])
                        break
        for y in range(len(picture)):
            if y == 0:
                for x in range(1, len(picture)):
                    for key in flips.keys():
                        if key not in used:
                            for i in range(len(flips[key])):
                                if ''.join([t[0] for t in flips[key][i]]) == ''.join([j[-1] for j in picture[y][x-1]]):
                                    picture[y][x] = flips[key][i]
                                    used.add(key)

            else:
                for x in range(len(picture[0])):
                    for key in flips.keys():
                        if key not in used:
                            for i in range(len(flips[key])):
                                if flips[key][i][0] == picture[y-1][x][-1]:
                                    picture[y][x] = flips[key][i]
                                    used.add(key)
        for y in range(len(picture)):
            for x in range(len(picture[0])):
                picture[y][x] = [f[1:-1] for f in picture[y][x][1:-1]]
        result = []
        for y in picture:
            for x in range(len(y[0])):
                result.append(''.join([line[x] for line in y]))
        return result

    def rotate_picture(self, picture):
        return rotate_all(picture)

    def calc_picture_marks(self, picture):
        return len(
            [water
             for water in ''.join(picture)
             if water == '#'
             ]
        )

    def calc_monster_marks(self, picture):
        seamonster_mark_coords = [
            (x, y)
            for y in range(len(seamonster))
            for x in range(len(seamonster[0]))
            if seamonster[y][x] == '#'
        ]
        rotated_images = self.rotate_picture(picture)
        seamonster_mark_cnt = len([
            water
            for water in ''.join(seamonster)
            if water == '#'
        ])

        dim_seamonster_y = len(seamonster)
        dim_seamonster_x = len(seamonster[0])

        monster_marks = 0
        for img in rotated_images:
            for y in range(len(img)-dim_seamonster_y):
                for x in range(len(img[y])-dim_seamonster_x):
                    monster_marks += seamonster_mark_cnt if all(
                        [img[y+j][x+i] == '#' for i, j in seamonster_mark_coords]) else 0
        return monster_marks

    def solve(self):
        picture = self.generate_picture()
        return self.calc_picture_marks(picture) - self.calc_monster_marks(picture)


TILE_ID_REGEX = re.compile(r'^Tile (\d+):$')


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    tiles = {}
    borders, flips = {}, {}
    index = 0
    length = len(processed_data)
    while True:
        if index >= length:
            break
        match = TILE_ID_REGEX.match(processed_data[index])
        if match is not None:
            tile_id = int(match.group(1))
            lines = processed_data[index+1:index+11]
            tiles[tile_id] = lines
            flips[tile_id] = rotate_all(lines)
            borders[tile_id] = [x[0] for x in flips[tile_id]]
            index += 12

    border_connections = {
        index: len([
            border
            for border in currentborders
            if any([
                border in otherborders
                for otherindex, otherborders in borders.items()
                if index != otherindex
            ])
        ])
        for index, currentborders in borders.items()
    }

    return tiles, borders, border_connections, flips


def solution(raw_data):
    """ Solution to the problem """
    data = preprocess(raw_data)
    solver = Code(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
