""" Advent of code 2021 day 06 / 2 """

from os import path
from collections import deque, defaultdict

class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        fishes = self.lines
        fsh = deque([0]*9)
        for i in fishes:
            fsh[i] += 1 
        # print(fsh)
        for i in range(256):
            nf = fsh.popleft()
            fsh.append(nf) # new fish
            fsh[6] += nf
            # print(fsh)

        return sum(fsh)

def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        processed_data = list(map(int,line.split(",")))
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
