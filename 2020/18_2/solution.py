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

    def step_level_forward(self, level, results, operations):
        """ Beware! It mutates the given array parameters, returned them to make it clear """
        level += 1
        results.append(0)
        operations.append(add)
        return level, results, operations

    def step_level_backward(self, target_level, level, results, operations):
        """ Beware! It mutates the given array parameters, returned them to make it clear """
        while level != target_level:
            level -= 1
            parentheses_inner_results = results.pop()
            operation = operations.pop()
            results[level] = operation(
                results[level],
                parentheses_inner_results
            )
        return level, results, operations

    def calc_expression(self, expression):
        readline = StringIO(expression).readline
        paren_level = []
        level = -1
        results = []
        operations = []
        level, results, operations = self.step_level_forward(level, results, operations)
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
            elif tok.exact_type == STAR:
                operations.append(mul)
                # to have proper precedence, start a new sublevel for each of this operation
                level, results, operations = self.step_level_forward(level, results, operations)
            elif tok.exact_type == LPAR:
                # for new parentheses, add the first number to 0
                paren_level.append(level)
                level, results, operations = self.step_level_forward(level, results, operations)
            elif tok.exact_type == RPAR:
                plevel = paren_level.pop()
                # for ending parentheses step as many levels back as the starting parenttheses and calculate the operation result
                level, results, operations = self.step_level_backward(plevel, level, results, operations)
            elif tok.exact_type in [ENDMARKER, NEWLINE]:
                level, results, operations = self.step_level_backward(0, level, results, operations)
                break
            else:
                print("UNHANDLED token", tok)
                sys.exit(1)
            # print(f"--- level: {level} result_stack: {results} op_stack: {operations}")
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
