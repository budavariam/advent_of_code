"""Advent of code 2025 day 09 / 2"""

import math
from pprint import pprint
from os import path
from utils import log, profiler


class Code(object):
    def __init__(self, points):
        self.points = points
        # polygon edges (consecutive pairs, closed)
        self.edges = [
            (points[i], points[(i + 1) % len(points)])
            for i in range(len(points))
        ]

    def area(self, c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

    def rectangle_coords(self, c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        left   = min(x1, x2)
        right  = max(x1, x2)
        top    = min(y1, y2)
        bottom = max(y1, y2)
        return left, right, top, bottom

    def _ccw(self, A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    def segments_intersect(self, seg1, seg2):
        (x1, y1), (x2, y2) = seg1
        (x3, y3), (x4, y4) = seg2
        A, B = (x1, y1), (x2, y2)
        C, D = (x3, y3), (x4, y4)
        return (
            self._ccw(A, C, D) != self._ccw(B, C, D)
            and self._ccw(A, B, C) != self._ccw(A, B, D)
        )

    def point_in_polygon(self, point, polygon):
        """Even-odd rule. src: https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule#Implementation"""
        x, y = point
        c = False
        n = len(polygon)
        for i in range(n):
            ax, ay = polygon[i]
            bx, by = polygon[(i + 1) % n]
            if (x, y) == (ax, ay):  # corner
                return True
            if (ay > y) != (by > y):
                slope = (x - ax) * (by - ay) - (bx - ax) * (y - ay)
                if slope == 0:  # boundary
                    return True
                if (slope < 0) != (by < ay):
                    c = not c
        return c

    def _inner_rect_edges(self, left, right, top, bottom):
        # shrink by 1 in each direction to get interior edges
        inner_left   = left + 1
        inner_right  = right - 1
        inner_top    = top + 1
        inner_bottom = bottom - 1

        if inner_left > inner_right or inner_top > inner_bottom:
            return None

        return [
            ((inner_left,  inner_top),    (inner_right, inner_top)),     # top
            ((inner_right, inner_top),    (inner_right, inner_bottom)),  # right
            ((inner_right, inner_bottom), (inner_left,  inner_bottom)),  # bottom
            ((inner_left,  inner_bottom), (inner_left,  inner_top)),     # left
        ]

    def is_valid_rectangle(self, c1, c2):
        """
        Valid if:
        1. No polygon edge crosses interior of the rectangle.
        2. Rectangle center is inside polygon.
        """
        left, right, top, bottom = self.rectangle_coords(c1, c2)

        rect_edges = self._inner_rect_edges(left, right, top, bottom)
        if rect_edges is None:
            return False

        # Any polygon edge intersecting any interior rect edge => invalid
        for poly_edge in self.edges:
            for rect_edge in rect_edges:
                if self.segments_intersect(poly_edge, rect_edge):
                    return False

        # Center must be inside polygon
        center = ((left + right) // 2, (top + bottom) // 2)
        if not self.point_in_polygon(center, self.points):
            return False

        return True

    def solve(self):
        result = 0
        n = len(self.points)

        for i, c1 in enumerate(self.points):
            for j in range(i + 1, n):
                c2 = self.points[j]

                a = self.area(c1, c2)
                if a <= result:
                    continue

                if self.is_valid_rectangle(c1, c2):
                    result = a

        return result


@profiler
def preprocess(raw_data):
    points = []
    for line in raw_data.split("\n"):
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        points.append((x, y))
    return points



@profiler
def solution(data):
    points = preprocess(data)
    solver = Code(points)
    return solver.solve()



if __name__ == "__main__":
    with open(
        path.join(path.dirname(__file__), "input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        print(solution(input_file.read()))
