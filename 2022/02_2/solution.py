""" Advent of code 2022 day 02 / 2 """

from os import path


ROCK = 1
PAPER = 2
SCISSORS = 3

OUTCOME_LOSE = 0
OUTCOME_DRAW = 3
OUTCOME_WIN = 6

mapping = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": OUTCOME_LOSE,
    "Y": OUTCOME_DRAW,
    "Z": OUTCOME_WIN,
}

beat = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}
lose = {
    PAPER: ROCK,
    SCISSORS: PAPER,
    ROCK: SCISSORS
}


def fight(opp, mine):
    if opp == mine:
        print("draw")
        return OUTCOME_DRAW
    elif beat[opp] == mine:
        print("win")
        return OUTCOME_WIN
    elif opp == beat[mine]:
        print("lose")
        return OUTCOME_LOSE
    else:
        print("!!!!!", opp, mine)
        return None

def what_to_choose(opp, score):
    if score == OUTCOME_DRAW:
        return opp
    elif score == OUTCOME_LOSE:
        return lose[opp]
    elif score == OUTCOME_WIN:
        return beat[opp]
    else:
        print("!!!!!", opp, score)
        return None

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        print(self.lines)
        total = 0
        for line in self.lines:
            opp = line[0]
            score = line[1]
            # what should it be, not mine!!
            mine = what_to_choose(opp,score)
            match_score = mine + score
            total += match_score
            print(opp, mine, score, match_score, total)
        return total


def preprocess(raw_data):
    processed_data = []
    for line in raw_data.split("\n"):
        data = line.split(" ")
        processed_data.append(
            [mapping[data[0]], mapping[data[1]]],
        )
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
