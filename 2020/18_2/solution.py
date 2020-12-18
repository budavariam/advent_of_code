""" Advent of code 2020 day 18/2 """

import math
import sys
from io import StringIO
from os import path
from operator import mul, add
from tokenize import generate_tokens, tok_name, NUMBER, LPAR, RPAR, PLUS, STAR, ENDMARKER, NEWLINE


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def calc_expression(self, expression):
        readline = StringIO(expression).readline
        paren_level = []
        level = 0
        results = [0]
        operations = [add]
        for tok in generate_tokens(readline):
            # print(f"{tok_name[tok.exact_type]} - {repr(tok.string)}")
            if tok.exact_type == NUMBER:
                # for numbers check the last operation, and set the given level of result to that
                current_value = int(tok.string)
                operation = operations.pop()
                results[level] = operation(
                    results[level],
                    current_value
                )
            elif tok.exact_type == PLUS:
                operations.append(add)
                # to have proper precedence, start a new sublevel for each operation
            elif tok.exact_type == STAR:
                level += 1
                operations.append(mul)
                results.append(0)
                operations.append(add)
            elif tok.exact_type == LPAR:
                # for new parentheses, add the first number to 0
                paren_level.append(level)
                level += 1
                results.append(0)
                operations.append(add)
            elif tok.exact_type == RPAR:
                plevel = paren_level.pop()
                # for ending parentheses step as many levels back as the starting parenttheses and calculate the operation result
                while level != plevel:
                    level -= 1
                    parentheses_inner_results = results.pop()
                    operation = operations.pop()
                    results[level] = operation(
                        results[level],
                        parentheses_inner_results
                    )
            elif tok.exact_type in [ENDMARKER, NEWLINE]:
                while level != 0:
                    level -= 1
                    parentheses_inner_results = results.pop()
                    operation = operations.pop()
                    results[level] = operation(
                        results[level],
                        parentheses_inner_results
                    )
                break
            else:
                print("UNHANDLED token", tok)
                sys.exit(1)
            #print(f"--- level: {level} result_stack: {results} op_stack: {operations}")
        return results[level]

    def solve(self):
        result = 0
        for line in self.lines:
            result += self.calc_expression(line)
        return result


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
