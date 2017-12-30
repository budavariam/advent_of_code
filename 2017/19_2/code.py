""" Advent of code 2017 day 19/2 """
from argparse import ArgumentParser

class Maze(object):
    """ Maze representation """
    def __init__(self, data):
        self.data = self.read_data(data)
        self.p_x = self.data[0].index('|')
        self.p_y = 0
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.directions = {
            's': (1, 0),
            'n': (-1, 0),
            'e': (0, 1),
            'w': (0, -1)
        }
        self.turns = {
            's': ['e', 'w'],
            'n': ['e', 'w'],
            'e': ['n', 's'],
            'w': ['n', 's']
        }
        self.dir = 's'
        self.turn = False

    @staticmethod
    def read_data(data):
        """ REad the data from the input """
        return data.split('\n')

    def move(self):
        """ Move the pointer forward and return the next character """
        if not self.turn:
            n_y, n_x = self.directions[self.dir]
            self.p_y += n_y
            self.p_x += n_x
            if self.p_y < self.height and self.p_x < self.width and self.p_y >= 0 and self.p_x >= 0:
                next_char = self.data[self.p_y][self.p_x]
                if next_char == '+':
                    self.turn = True
                elif next_char == ' ':
                    next_char = None
            else:
                next_char = None
        else:
            self.turn = False
            next_char, self.dir = self.check_turn()
            n_y, n_x = self.directions[self.dir]
            self.p_y += n_y
            self.p_x += n_x
        return next_char

    def check_turn(self):
        """ Check which direction can be used to turn to """
        directions = self.turns[self.dir]
        next_char = None
        for next_dir in directions:
            condition, next_char = self.check_dir(next_dir)
            if condition:
                break
        else:
            next_dir = None
        return next_char, next_dir

    def check_dir(self, direction):
        """ Check if the direction is valid """
        n_y, n_x = self.directions[direction]
        p_y = self.p_y + n_y
        p_x = self.p_x + n_x
        in_boundaries = p_y < self.height and p_x < self.width and p_y >= 0 and p_x >= 0
        elem = ' '
        if in_boundaries:
            elem = self.data[p_y][p_x]
        return (in_boundaries and elem != ' ', elem)

    def walk(self):
        """ Walk through the line until the end """
        condition = True
        letters = []
        steps = 0
        while condition:
            next_char = self.move()
            #print(next_char)
            steps += 1
            if next_char is None:
                condition = False
            elif next_char.isalpha():
                letters.append(next_char)
        return steps

def solution(data):
    """ Solution to the problem """
    parser = Maze(data)
    return parser.walk()

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(input_file.read()))
    elif ARGS.test:
        print(solution(str(ARGS.test)))
    else:
        DEBUG = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """
        print(solution(DEBUG))
