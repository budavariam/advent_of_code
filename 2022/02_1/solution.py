""" Advent of code 2022 day 02 / 1 """

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
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

beat = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
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


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        print(self.lines)
        total = 0
        for line in self.lines:
            opp = line[0]
            # mine = beat[line[1]]
            mine = line[1]
            score = fight(opp, mine)
            res = mine + score
            total += res
            print(opp, mine, score, res, total)
        return total


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
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
