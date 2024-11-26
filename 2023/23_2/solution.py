""" Advent of code 2023 day 23 / 2 """

from pprint import pprint
from os import path
from collections import defaultdict, deque
from utils import log, profiler

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

FOUR_NEIGHBOR = DIRECTIONS.values()


def add(a, b):
    return tuple(map(sum, zip(a, b)))


class Room:
    def __init__(self, index, start_pos, length) -> None:
        self.index = index
        self.connections = [start_pos]
        self.length = length

    def __repr__(self) -> str:
        return f"#{self.index}: {','.join(self.connections)} ({self.length})"

    def add_connection(self, r):
        self.connections.append(r)


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.maxh = len(self.lines) - 1
        self.maxw = len(self.lines[0]) - 1
        self.start = (0, 1)
        self.final = (self.maxh, self.maxw - 1)

    def print_map(self, visited):
        result = []
        for y, line in enumerate(self.lines):
            new_line = []
            for x, c in enumerate(line):
                v = (y, x) in visited
                new_line.append("o" if v else c)
            result.append(new_line)
        print("....")
        for line in result:
            print("".join(line))
        print("....")

    def get_foyers(self):
        # NOTE: the input has small rooms that distribute the load, find the positions of that and calc the distance between them
        # do 2 pass. first go around and get these small rooms. on the second pass calc distance between them
        foyers = {self.start: [self.start], self.final: [self.final]}

        ## FIRST PASS
        queue = deque([self.start])
        visited = set([])
        while queue:
            curr_pos = queue.pop()
            # curr_y, curr_x = curr_pos
            if curr_pos in visited:
                continue
            visited.add(curr_pos)

            nearby_doors = []
            for d in FOUR_NEIGHBOR:
                new_y, new_x = add(d, curr_pos)
                new_pos = (new_y, new_x)
                if (
                    0 <= new_y <= self.maxh
                    and 0 <= new_x <= self.maxw
                    and new_pos not in visited
                ):
                    next_val = self.lines[new_y][new_x]
                    if next_val == "#":
                        # skip the walls
                        continue
                    else:
                        if next_val in ["^", "v", "<", ">"]:
                            nearby_doors.append(new_pos)
                        # move inside the room
                        queue.append((new_y, new_x))
            if len(nearby_doors) > 1:
                foyers[curr_pos] = nearby_doors
        return foyers

    def build_room_graph(self, foyers):
        init_list = []
        for foyer_pos, first_cells in foyers.items():
            for start_cell in first_cells:
                init_list.append((foyer_pos, start_cell, 0))

        queue = deque(init_list)
        graph = defaultdict(set)
        visited = set([])
        while queue:
            prev_foyer, curr_pos, d = queue.pop()
            if curr_pos in visited:
                continue
            visited.add(curr_pos)
            distance = d + 1

            for d in FOUR_NEIGHBOR:
                new_y, new_x = add(d, curr_pos)
                new_pos = (new_y, new_x)

                if (
                    0 <= new_y <= self.maxh
                    and 0 <= new_x <= self.maxw
                    and new_pos not in visited
                ):
                    next_val = self.lines[new_y][new_x]
                    inside_room = new_pos not in foyers
                    if next_val == "#":
                        # skip the walls
                        continue
                    elif inside_room:
                        # move one step inside the room
                        queue.append((prev_foyer, (new_y, new_x), distance))
                    elif not inside_room:
                        # do not add new movement if reached the end of the room
                        # extend a graph with bidirectional movement
                        graph[new_pos].add((prev_foyer, distance + 1))
                        graph[prev_foyer].add((new_pos, distance + 1))
        return graph

    def calc_longest_path(self, graph):
        longest_path = -1
        stack = [(self.start, 0, set())]
        while stack:
            curr_node, distance, visited = stack.pop()
            visited.add(curr_node)
            if curr_node == self.final:
                longest_path = max(longest_path, distance)

            for next_node, edge_length in graph[curr_node]:
                if next_node not in visited:
                    stack.append((next_node, distance + edge_length, set(visited)))
        return longest_path - 1

    def solve(self):
        foyers = self.get_foyers()
        graph = self.build_room_graph(foyers)
        longest_path = self.calc_longest_path(graph)
        return longest_path


@profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = list(line)
        processed_data.append(data)
    return processed_data


@profiler
def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
