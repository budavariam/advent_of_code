""" Advent of code 2020 day 22/1 """

import math
from os import path
import re
from collections import defaultdict, deque


class Code(object):
    def __init__(self, player_deck):
        self.player_deck = player_deck

    def has_winner(self):
        return any([len(x) == 0 for x in self.player_deck.values()])

    def calc_score(self, decks):
        return sum([x * (i + 1) for deck in decks.values() for i, x in enumerate(reversed(deck))])

    def simulate_game(self):
        while not self.has_winner():
            card_player1 = self.player_deck[1].popleft()
            card_player2 = self.player_deck[2].popleft()
            if card_player1 > card_player2:
                self.player_deck[1].append(card_player1)
                self.player_deck[1].append(card_player2)
            elif card_player1 < card_player2:
                self.player_deck[2].append(card_player2)
                self.player_deck[2].append(card_player1)
            else:
                print("There should not be two idenntical cards in the two decks.")
        return self.calc_score(self.player_deck)

    def solve(self):
        return self.simulate_game()


PLAYER_PARSER = re.compile(r'^Player (\d+):$')


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    current_player = None
    player_deck = defaultdict(deque)
    for line in processed_data:
        player = PLAYER_PARSER.match(line)
        if player is not None:
            current_player = int(player.group(1))
        elif line != "":
            player_deck[current_player].append(int(line))
    return player_deck


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
