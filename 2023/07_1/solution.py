""" Advent of code 2023 day 07 / 1 """

import math
from pprint import pprint
from os import path
import re
from collections import Counter
import utils
from functools import total_ordering

CARD_STRENGTH = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

HAND_NAME = [
    "Five of a kind",
    "Four of a kind",
    "Full house",
    "Three of a kind",
    "Two pair",
    "One pair",
    "High card",
]


@total_ordering
class CamelCard(object):
    def convert_card(self, c: str) -> int:
        return CARD_STRENGTH[c]

    def get_handtype(self, hand: str) -> int:
        c = Counter(hand)
        values = sorted(c.values(), reverse=True)
        if values[0] == 5:
            # Five of a kind, where all five cards have the same label: AAAAA
            return 0
        elif values[0] == 4:
            # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
            return 1
        elif values[0] == 3 and values[1] == 2:
            # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
            return 2
        elif values[0] == 3 and values[1] == 1 and values[2] == 1:
            # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the # hand: TTT98
            return 3
        elif values[0] == 2 and values[1] == 2 and values[2] == 1:
            # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
            return 4
        elif values[0] == 2 and values[1] == 1:
            # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
            return 5
        elif values[0] == 1:
            # High card, where all cards' labels are distinct: 23456
            return 6
        else:
            return -1

    def __init__(self, hand: str, bid=0):
        self.bid = bid
        self.hand = hand
        self.handtype = self.get_handtype(hand)

    # def __eq__(self, other):
    #     return self.hand == other.hand

    def __lt__(self, other):
        res = 0
        if self.handtype < other.handtype:
            # self has a better combination
            res = False
        elif self.handtype > other.handtype:
            # self has a worse combination
            res = True
        elif self.handtype == other.handtype:
            cmp = zip(self.hand, other.hand)
            for card_self, card_other in cmp:
                val_self = self.convert_card(card_self)
                val_other = self.convert_card(card_other)
                if val_self == val_other:
                    continue
                elif val_self < val_other:
                    # self has a worse combination
                    res = True
                    break
                elif val_self > val_other:
                    # self has a better combination
                    res = False
                    break
            else:
                res = True
        else:
            res = True
        # print(f"cmp: {self} - {other} = {res}")
        return res

    def __repr__(self):
        # return f"{self.handtype}:{self.hand} {self.bid}"
        return f"{HAND_NAME[self.handtype]}:{self.hand}"


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        # pprint(self.lines)
        cards = []
        result = 0
        for hand, bid in self.lines:
            cards.append(CamelCard(hand=hand, bid=bid))
        cards = sorted(cards)

        for rank, c in enumerate(cards, start=1):
            curr = c.bid * rank
            # print(f"{c}: {rank}*{c.bid}={curr}")
            result += curr
        return result


@utils.profiler
def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = line.split(" ")
        processed_data.append((data[0], int(data[1])))
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
