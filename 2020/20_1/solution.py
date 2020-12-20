""" Advent of code 2020 day 20/1 """

import math
from os import path
import re
from collections import defaultdict, Counter


class Code(object):
    def __init__(self, data):
        self.tiles, self.edge_collection = data

    def solve(self):
        corner_ids = [k for k, v in Counter(
            [list(v)[0] for k, v in self.edge_collection.items() if len(v) == 1]).items() if v == 4]
        result = 1
        for c_id in corner_ids:
            result *= c_id
        return result


TILE_ID_REGEX = re.compile(r'^Tile (\d+):$')


def preprocess(raw_data):
    def get_edges(lines):
        """Assume that the map pieces are squares"""
        length = len(lines)
        return [
            lines[0],
            lines[0][::-1],
            "".join(map(lambda x: x[0], lines)),
            "".join(map(lambda x: x[0], lines))[::-1],
            "".join(map(lambda x: x[length - 1], lines)),
            "".join(map(lambda x: x[length - 1], lines))[::-1],
            lines[length - 1],
            lines[length - 1][::-1],
        ]

    processed_data = raw_data.split("\n")
    tiles = {}
    edge_collection = defaultdict(set)
    index = 0
    length = len(processed_data)
    while True:
        if index >= length:
            break
        match = TILE_ID_REGEX.match(processed_data[index])
        if match is not None:
            tile_id = int(match.group(1))
            lines = processed_data[index+1:index+11]
            edges = get_edges(lines)
            for edge in edges:
                edge_collection[edge].add(tile_id)
            tiles[tile_id] = {
                "id": tile_id,
                "lines": lines,
                "edges": edges,
            }
            index += 12

    return (tiles, edge_collection)


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))

# set([list(v)[0] for k, v in edge_collection.items() if len(v) == 1])
