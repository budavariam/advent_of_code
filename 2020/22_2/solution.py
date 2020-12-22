""" Advent of code 2020 day 22/2 """

import math
from os import path
import re
from collections import defaultdict, deque
from copy import deepcopy


class Code(object):
    def __init__(self, player_deck):
        self.player_deck = player_deck
        self.game_index = 0

    def has_winner(self, decks):
        return any([len(x) == 0 for x in decks.values()])

    def calc_score(self, deck):
        return sum([x * (i + 1) for i, x in enumerate(reversed(deck))])

    def limit_deck(self, deck, limit):
        while len(deck) > limit:
            deck.pop()
        return deck

    def simulate_game(self, decks):
        self.game_index += 1
        game_index = self.game_index
        # print(f"=== Game {game_index} ===")
        round_cache = set()
        round_index = 1
        while not self.has_winner(decks):
            # print(f"-- Round {round_index} (Game {game_index}) --")
            round_index += 1
            p1deck = "".join(map(str, decks[1]))
            p2deck = "".join(map(str, decks[2]))
            # print(f"Player 1's deck: {', '.join(map(str, decks[1]))}")
            # print(f"Player 2's deck: {', '.join(map(str, decks[2]))}")
            if p1deck in round_cache or p2deck in round_cache:
                # print(
                #     f"Repeated play: Player 1 wins round {round_index} of game {game_index}! ")
                return (1, self.calc_score(decks[1]))
            round_cache.add(p1deck)
            round_cache.add(p2deck)

            card_player1 = decks[1].popleft()
            card_player2 = decks[2].popleft()
            # print(f"Player 1 plays: {card_player1}")
            # print(f"Player 2 plays: {card_player2}")

            if len(decks[1]) >= card_player1 and len(decks[2]) >= card_player2:
                # print("Playing a sub-game to determine the winner...")
                newdecks = deepcopy(decks)
                winner_id, _ = self.simulate_game({
                    1: self.limit_deck(newdecks[1], card_player1),
                    2: self.limit_deck(newdecks[2], card_player2),
                })
                # print(f"...anyway, back to game {game_index}.")
                decks[winner_id].append(
                    card_player1
                    if winner_id == 1 else card_player2
                )
                decks[winner_id].append(
                    card_player2
                    if winner_id == 1 else card_player1
                )
            elif card_player1 > card_player2:
                decks[1].append(card_player1)
                decks[1].append(card_player2)
                # print(
                #     f"Player 1 wins round {round_index} of game {game_index}! ")
            elif card_player1 < card_player2:
                decks[2].append(card_player2)
                decks[2].append(card_player1)
                # print(
                #     f"Player 2 wins round {round_index} of game {game_index}! ")
            else:
                print("There should not be two idenntical cards in the two decks.")
        p1score = self.calc_score(decks[1])
        p2score = self.calc_score(decks[2])
        winner = 1 if p1score > p2score else 2
        score = p1score if winner == 1 else p2score
        return winner, score

    def solve(self):
        _, score = self.simulate_game(self.player_deck)
        return score


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
