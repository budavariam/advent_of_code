""" Advent of code 2022 day 11 / 2 """

from os import path
import re


class Monkey(object):
    def __init__(self, m_id, items, operation, test, if_true, if_false):
        self.m_id = m_id
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.activity_cnt = 0

    def __repr__(self):
        return f"{self.m_id}: {self.activity_cnt} (#{len(self.items)})"

    def round(self):
        result = []
        # pylint: disable=unused-variable
        for item_value in self.items:
            self.activity_cnt += 1

            math_op = self.operation[0]
            other_val = self.operation[1].replace("old", "item_value")
            # pylint: disable=eval-used
            new_level = eval(f"item_value {math_op} {other_val}")

            who = self.if_true if new_level % self.test == 0 else self.if_false
            what = new_level
            result.append((who, what))
        # throw all away
        self.items = []
        return result


class Code(object):
    def __init__(self, lines):
        self.monkeys = lines

    def solve(self):

        around_lkkt = 1
        for m in self.monkeys:
            around_lkkt *= m.test

        print(self.monkeys)
        for _ in range(10000):
            for m_id in range(len(self.monkeys)):
                thrown_items = self.monkeys[m_id].round()
                for (which_m, what) in thrown_items:
                    self.monkeys[which_m].items.append(what % around_lkkt)
        self.monkeys.sort(key=lambda x: x.activity_cnt, reverse=True)

        return self.monkeys[0].activity_cnt * self.monkeys[1].activity_cnt


def preprocess(raw_data):
    processed_data = []
    for m_data in raw_data.split("\n\n"):
        data = m_data.split("\n")
        m_id = int(re.match(r"Monkey (\d+):", data[0]).group(1))
        start_items = [int(x) for x in data[1].split(": ")[1].split(", ")]

        ops = data[2].split("new = old ")[1].split(" ")
        operation = (ops[0], ops[1])

        test = int(data[3].split("divisible by ")[1])

        if_true = int(data[4].split("monkey ")[1])
        if_false = int(data[5].split("monkey ")[1])

        m = Monkey(m_id, start_items, operation, test, if_true, if_false)
        processed_data.append(m)
    return processed_data


def solution(data):
    """Solution to the problem"""
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with (open(path.join(path.dirname(__file__), "input.txt"), "r")) as input_file:
        print(solution(input_file.read()))
