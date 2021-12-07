""" Advent of code 2021 day 07 / 2 """

from os import path

class Code(object):
    def __init__(self, lines):
        self.lines = lines
        self.cache = {}

    def cch(self, lim):
        if not lim in self.cache:
            self.cache[lim] = int((lim*(lim+1))/2)
        # print(self.cache)
        return self.cache[lim]

    def solve(self):
        fuels = []
        for i, val in enumerate(self.lines):
            fuel = 0
            for val in self.lines:
                fuel += self.cch(abs(i-val))
            fuels.append(fuel)
        return min(fuels)


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        processed_data = list(map(int, line.split(",")))
        # processed_data.append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
