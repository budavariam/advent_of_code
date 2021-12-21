""" Advent of code 2021 day 21 / 2 """

import math
from os import path
import re
from itertools import product
from collections import Counter, defaultdict


class Player(object):
    def __init__(self, pos, score):
        self.pos = pos
        self.score = score


class Code(object):
    def __init__(self, lines):
        self.players = lines
        self.rolls = Counter(map(sum, product(range(1, 4), repeat=3))).items()

    def solve(self):
        game_states = defaultdict(int)
        game_states[(
            (self.players[0].pos, self.players[0].score),
            (self.players[1].pos, self.players[1].score),
        )] = 1
        wins = [0, 0]
        turn = 0
        while len(game_states) > 0:
            next_state = defaultdict(int)
            for state, uni_cnt in game_states.items():
                for roll, num_rolls in self.rolls:
                    n_pos = (state[turn][0] + roll) % 10  # 0-9
                    n_score = state[turn][1] + (n_pos + 1)  # 1-10

                    if n_score >= 21:
                        wins[turn] += uni_cnt * num_rolls
                    else:
                        n_s = [None, None]
                        n_s[turn] = (n_pos, n_score)  # set  current turn
                        n_s[1-turn] = state[1-turn]   # keep prev val

                        # add splitted res to memo
                        next_state[(n_s[0], n_s[1])] += uni_cnt * num_rolls
            turn = (turn + 1) % 2
            game_states = next_state
        return max(wins)


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
