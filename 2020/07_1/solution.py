""" Advent of code 2020 day 07/1 """

import math
from os import path
import re
import logging

line_parser = re.compile(
    r'^(?P<container>\w+ \w+) bags contain (?P<content>[^.]+)\.$')
content_parser = re.compile(r'(\d*)\s*(\w+ \w+) bags?(?:, )?')


class Bag(object):
    def __init__(self, color, number):
        self.color = color
        self.contents = dict()
        self.parents = []

    def __repr__(self):
        contents = ', '.join(f"{v}: {k}" for [k, v] in self.contents.items())
        return f"{self.color}: {contents}"

    def add_content(self, content):
        if content is None:
            return
        for match in content:
            color = match.group(2)
            if color == "no other":
                continue
            str_number = match.group(1)
            if str_number is None:
                number = None
            elif str_number == "":
                number = 0
            else:
                number = int(str_number)
            self.contents[color] = number

    def set_parents_for_content(self, parent_color, all_bags):
        if parent_color is not None:
            self.parents.append(parent_color)
        else:
            for content_color in self.contents.keys():
                traverse_top = all_bags.get(content_color)
                traverse_top.set_parents_for_content(self.color, all_bags)


class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.bag_map = dict()
        self.graph = []

    def fill_bag(self, line):
        match = line_parser.match(line)
        if match is None:
            logging.error("Did not match line: %s", line)
            return
        container_group = match.groupdict()
        container_color = container_group["container"]
        bags_inside = content_parser.finditer(container_group["content"])
        flyweight_bag = Bag(container_color, None)
        flyweight_bag.add_content(bags_inside)
        self.bag_map[container_color] = flyweight_bag

    def build_graph(self, all_bags):
        for bag in all_bags.values():
            bag.set_parents_for_content(None, self.bag_map)

    def prepare_graph(self):
        for line in self.lines:
            self.fill_bag(line)
        self.build_graph(self.bag_map)

    def count_paths(self, initial_item):
        self.prepare_graph()

        queue = [x for x in self.bag_map.get(initial_item).parents]
        visited = set()
        path_count = 0
        while len(queue) > 0:
            next_item = queue.pop()
            if next_item in visited:
                continue
            queue.extend(self.bag_map.get(next_item).parents)
            visited.add(next_item)
            path_count += 1
        return path_count


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.count_paths("shiny gold")


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
