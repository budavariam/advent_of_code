""" Advent of code 2021 day 21 / 1 """

import math
from os import path
import re

roll_cnt = 0


def det_dice():
    val = -1
    global roll_cnt
    while True:
        val += 1
        roll_cnt += 1
        val %= 100
        yield val+1


class Player(object):
    def __init__(self, pos, score):
        self.pos = pos
        self.score = score


class Code(object):
    def __init__(self, lines):
        self.players = lines

    def solve(self):
        tablesize = 10
        # print(self.lines)
        turn = 0
        d = det_dice()
        players = self.players
        c = players[turn]
        while True:
            roll = sum(
                [d.__next__(),
                 d.__next__(),
                 d.__next__(),
                 ])
            c.pos = ((c.pos + roll) % 10) # 0-9
            c.score += c.pos + 1 # 1-10
            print(
                f"Player {turn} rolled {roll} and moves to {c.pos + 1} for a total score of {c.score}"
            )
            if c.score >= 1000:
                break
            turn = (turn + 1) % 2
            c = players[turn]
        return roll_cnt * players[1 - turn].score


def preprocess(raw_data):
    pattern = re.compile(r'Player (\d+) starting position: (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        match = re.match(pattern, line)
        data = Player(
            int(match.group(2)) - 1, 
            0,
        )
        processed_data.append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
