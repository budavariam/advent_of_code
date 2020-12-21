""" Advent of code 2020 day 21/1 """

import math
from os import path
import re
from collections import defaultdict
from copy import deepcopy


class AllergenAssessment(object):
    def __init__(self, data):
        self.lines, self.allergenes, self.ingredients = data

    def solve(self):
        # original_lines = deepcopy(self.lines)
        mapping = {}
        while len(mapping) < len(self.allergenes):
            for name, appearance in self.allergenes.items():
                possible_ingredients = self.ingredients
                for location in appearance:
                    possible_ingredients = possible_ingredients.intersection(
                        self.lines[location]["ingredients"])
                if len(possible_ingredients) == 1:
                    # save result
                    mapping[name] = list(possible_ingredients)[0]
                    # clear from ingredient list
                    for index, line in enumerate(self.lines):
                        new_ingredients = line["ingredients"].difference(
                            set(list(possible_ingredients)))
                        self.lines[index]["ingredients"] = new_ingredients
        result = 0
        for item in self.lines:
            result += len(item["ingredients"])
        return result


ALLERGEN_PARSER = re.compile(r'^(.*) \(contains (.*)\)$')


def preprocess(raw_data):
    processed_data = raw_data.split("\n")
    result = []
    all_ingredients = set()
    allergen_locations = defaultdict(set)
    for index, line in enumerate(processed_data):
        match = ALLERGEN_PARSER.match(line)
        ingredients = set(match.group(1).split(" "))
        all_ingredients = all_ingredients.union(ingredients)
        allergens = set(match.group(2).split(", "))
        for alg in allergens:
            allergen_locations[alg] = allergen_locations[alg].union(
                set([index]))
        result.append({
            "ingredients": ingredients,
            "allergens": allergens,
        })
    return result, allergen_locations, all_ingredients


def solution(raw_data):
    """ Solution to the problem """
    data = preprocess(raw_data)
    solver = AllergenAssessment(data)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
