""" Advent of code 2020 day 23/2 """

import math
from os import path


class CupNode(object):
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.id} (p: {'-' if self.prev is None else self.prev.id} n: {'-' if self.next is None else self.next.id})"


class Code(object):
    def __init__(self, data, move_count):
        self.cups, self.first_cup = data
        self.move_count = move_count
        self.lowest_cup_label = min(self.cups.keys())
        self.highest_cup_label = max(self.cups.keys())

    def print_cups(self, start):
        result = ""
        cup = self.cups[start]
        for _ in range(len(self.cups) - 1): # do not print the first item
            cup = cup.next
            result += str(cup.id)
        return result

    def pick_cups(self, start_cup):
        """
        The crab picks up the three cups that are immediately clockwise of the current cup. 
        They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
        """
        first_cut_cup = start_cup.next
        second_cut_cup = first_cut_cup.next
        last_cut_cup = second_cut_cup.next
        cut_ids = [
            first_cut_cup.id,
            second_cut_cup.id,
            last_cut_cup.id
        ]

        # cut them out of the chain
        first_cut_cup.prev.next = last_cut_cup.next
        last_cut_cup.next.prev = first_cut_cup.prev
        # Set their approprate values to empty
        first_cut_cup.prev = None
        last_cut_cup.next = None
        return first_cut_cup, last_cut_cup, cut_ids

    def find_destination_cup_id(self, current_id, excluded_labels):
        """
        The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. 
            If this would select one of the cups that was just picked up, 
            the crab will keep subtracting one until it finds a cup that wasn't just picked up. 
            If at any point in this process the value goes below the lowest value on any cup's label, 
            it wraps around to the highest value on any cup's label instead.
        """
        destination = current_id - 1
        if destination < self.lowest_cup_label:
            destination = self.highest_cup_label
        while destination in excluded_labels:
            destination -= 1
            if destination < self.lowest_cup_label:
                destination = self.highest_cup_label
        return destination

    def insert_cups_to_destination(self, destination_cup, first_cut_cup, last_cut_cup):
        """
        The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. 
        They keep the same order as when they were picked up.
        """
        first_cut_cup.prev = destination_cup
        last_cut_cup.next = destination_cup.next
        destination_cup.next.prev = last_cut_cup
        destination_cup.next = first_cut_cup

    def move_cups(self, current_cup):
        """
        See `self.pick_cups`

        See `self.find_destination_cup_id`

        See `self.insert_cups_to_destination`

        The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
        """
        first_cut, last_cut, cut_cup_ids = self.pick_cups(current_cup)
        destination_cup_id = self.find_destination_cup_id(
            current_cup.id, cut_cup_ids)
        self.insert_cups_to_destination(self.cups[destination_cup_id], first_cut, last_cut)
        return current_cup.next

    def solve(self):
        current = self.first_cup
        for step in range(self.move_count):
            if step % 500000 == 0:
                print("Move", step)
            current = self.move_cups(current)
        cup_label_one = self.cups[1]
        return cup_label_one.next.id * cup_label_one.next.next.id


def preprocess(raw_data):
    processed_data = list(map(int, raw_data.split("\n")[0]))
    prev_cup = None
    first_cup = None
    cups = {}
    cup_ids = processed_data + list(range(max(processed_data) + 1, 1000001))
    for cup_id in cup_ids:
        identifier = cup_id
        current_cup = CupNode(identifier)
        cups[identifier] = current_cup
        if prev_cup is not None:
            current_cup.prev = prev_cup
            prev_cup.next = current_cup
        else:
            first_cup = current_cup
        prev_cup = current_cup
    current_cup.next = first_cup
    first_cup.prev = current_cup
    print("Preprocess done")
    return cups, first_cup


def solution(raw_data):
    """ Solution to the problem """
    data = preprocess(raw_data)
    move_count = 10000000
    solver = Code(data, move_count)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
