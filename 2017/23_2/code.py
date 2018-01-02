""" Advent of code 2017 day 23/2 """
from argparse import ArgumentParser

'''
"The key to understanding what this code does is starting from the end and working backwards:
    If the program has exited, g had a value of 0 at line 29.
    g==0 at line 29 when b==c.
    If g!=0 at line 29, b increments by 17.
    b increments no other times on the program.
    Thus, lines 25 through 31 will run 1000 times,
    on values of b increasing by 17, before the program finishes.

So, given that there is no jnz statement between lines 25 and 28 that could affect things:
    If f==0 at line 25, h will increment by 1.
    This can happen once and only once for any given value of b.
    f==0 if g==0 at line 15.
    g==0 at line 15 if d*e==b.
    Since both d and e increment by 1 each in a loop,
    this will check every possible value of d and e less than b.
    Therefore, if b has any prime factors other than itself, f will be set to 1 at line 25.

Looking at this, then h is the number of composite
    numbers between the lower limit and the upper limit, counting by 17."

Written by DFreiberg on https://www.reddit.com/r/adventofcode/
Video by Michael Gilliland: https://www.youtube.com/watch?v=AqXTZo6o34s
'''

def solution(data):
    """ Solution to the problem """
    raw = data.split('\n')[0].split(' ')[2]
    reg_b = int(raw) * 100 + 100000 # line 5-6
    reg_c = reg_b + 17000 # line 8
    reg_h = 0
    for reg_d in range(reg_b, reg_c + 1, 17): #line 31
        reg_h += any(True for reg_e in range(2, reg_d) if reg_d % reg_e == 0)
    return reg_h

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
        DEBUG = """set b 81"""
        print(solution(DEBUG))
