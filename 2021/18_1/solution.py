""" Advent of code 2021 day 18 / 1 """
import json
import math
from os import path
import re
from collections import deque


class Node(object):
    def __init__(self, left=None, rght=None, parent=None, value=None):
        self.p = parent
        self.l = None
        self.r = None
        self.v = None

        if left is not None and isinstance(left, Node):
            self.l = left
            self.l.p = self
        elif left is not None and isinstance(left, list):
            self.l = parse_tree(left, self)
        elif left is not None:
            self.l = Node(None, None, self, left)

        if rght is not None and isinstance(rght, Node):
            self.r = rght
            self.r.p = self
        elif rght is not None and isinstance(rght, list):
            self.r = parse_tree(rght, self)
        elif rght is not None:
            self.r = Node(None, None, self, rght)

        if isinstance(value, int):
            self.v = value

    def prnt(self):
        if self.v is not None:
            return self.v
        else:
            return [self.l.prnt(), self.r.prnt()]

    def __repr__(self):
        return str(self.prnt())

    def find_rightmost(self):
        if self.r is None:
            return self
        return self.r.find_rightmost()

    def find_leftmost(self):
        if self.l is None:
            return self
        return self.l.find_leftmost()

    def find_root(self):
        if self.p is None:
            return self

        p = self.p
        while p.p is not None:
            p = p.p
        return p

    def find_left_neighbour(self):
        if self.p is None:
            return None

        if self.find_root().find_leftmost() == self:
            # if this is the leftmost negihbor of root then finish
            return None

        # go up until it can go down left
        prev = self
        p = self.p
        while True:
            if p.l != prev:
                break
            prev = p
            p = p.p
        return p.l.find_rightmost()

    def find_right_neighbour(self):
        if self.p is None:
            return None

        if self.find_root().find_rightmost() == self:
            # if this is the rightmost negihbor of root then finish
            return None

        # go up until you can go down right
        prev = self
        p = self.p
        while True:
            if p.r != prev:
                break
            prev = p
            p = p.p
        return p.r.find_leftmost()

    def find_explodable(self, level=0):
        if level == 4 and self.v is None:
            return self

        has_l = None
        has_r = None
        if self.l is not None:
            has_l = self.l.find_explodable(level + 1)
            if has_l is not None:
                return has_l
        if self.r is not None:
            has_r = self.r.find_explodable(level + 1)
            if has_r is not None:
                return has_r
        return None

    def find_largenum(self):
        if self.v is not None and self.v >= 10:
            return self

        if self.v is not None:
            return None

        if self.l is not None:
            res_l = self.l.find_largenum()
            if res_l is not None:
                return res_l

        if self.r is not None:
            res_r = self.r.find_largenum()
            if res_r is not None:
                return res_r

    def explode(self):
        node = self.find_explodable()
        if node is None:
            return False

        left_n = node.l.find_left_neighbour()
        if left_n is not None:
            left_n.v += node.l.v
        right_n = node.r.find_right_neighbour()
        if right_n is not None:
            right_n.v += node.r.v
        node.l = None
        node.r = None
        node.v = 0
        return True

    def split(self):
        n = self.find_largenum()
        if n is None:
            return False
        l = n.v // 2
        r = n.v - l
        n.l = Node(value=l, parent=n)
        n.r = Node(value=r, parent=n)
        n.v = None
        
        return True

    def reduce(self):
        condition = True
        while condition:
            condition = False
            if self.explode():
                condition = True
            elif self.split():
                condition = True

    def add(self, a,b):
        n = Node(a, b, None, None)
        n.reduce()
        return n

    def magnitude(self):
        res = 0
        if self.l is not None:
            res += 3*self.l.magnitude()
        if self.r is not None:
            res += 2*self.r.magnitude()
        if self.v is not None:
            res += self.v
        return res


class Code(object):
    def __init__(self, lines):
        self.lines = lines

    def solve(self):
        print("start")
        num = self.lines[0]
        print(num)
        for nextnum in self.lines[1:]:
            num = num.add(num, nextnum)
            print(num)
        final_magnitude = num.magnitude()
        return final_magnitude


def parse_tree(jdata, parent=None):
    if jdata is None:
        return jdata
    return Node(jdata[0], jdata[1], parent)


def preprocess(raw_data):
    # pattern = re.compile(r'(\w+) (\d+)')
    processed_data = []
    for line in raw_data.split("\n"):
        # match = re.match(pattern, line)
        # data = [match.group(1), match.group(2)]
        data = parse_tree(json.loads(line))
        processed_data.append(data)
    return processed_data


def solution(data):
    """ Solution to the problem """
    lines = preprocess(data)
    solver = Code(lines)
    return solver.solve()


if __name__ == "__main__":
    with(open(path.join(path.dirname(__file__), 'input.txt'), 'r')) as input_file:
        print(solution(input_file.read()))
