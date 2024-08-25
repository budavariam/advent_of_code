""" Advent of code 2023 day 04 / 2 """

import math
from pprint import pprint
from os import path
import re
from collections import deque
import utils


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # pprint(self.lines)
        result = {}
        max_id = self.lines["max_cardnum"]
        queue = deque(range(1, max_id + 1))
        for x in queue:
            result[x] = 1

        while len(queue) > 0:
            c = queue.popleft()
            # print(f"Evaluating {c}:")
            if c in self.lines:
                curr = self.lines[c]
                # wins cards
                won_card_num = len(curr["next_card"])
                card_ids_to_win = list(
                    range(
                        curr["id"] + 1,
                        min(max_id + 1, curr["id"] + won_card_num + 1),
                    )
                )
                # print(f"  won {won_card_num} cards: {card_ids_to_win}")
                for n in card_ids_to_win:
                    result[n] += 1
                    if n in self.lines:
                        queue.append(n)
                # print(f"  result: {result}")
        return sum(result.values())


def parse_numbers(lst):
    return [int(x) for x in lst.split(" ") if x != ""]


@utils.profiler
def preprocess(raw_data):
    processed_data = {}
    for line in raw_data.split("\n"):
        strip_1 = line.split(":")
        cid = int(strip_1[0].strip("Card "))
        winning, cards = map(parse_numbers, strip_1[1].split("|"))
        next_cards = set(winning).intersection(set(cards))
        if len(next_cards) > 0:
            processed_data[cid] = {"id": cid, "next_card": next_cards}
    processed_data["max_cardnum"] = cid
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
