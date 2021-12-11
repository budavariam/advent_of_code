""" Advent of code 2021 day 11 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
#         self.assertEqual(solution("""11111
# 19991
# 19191
# 19991
# 11111"""), 9)
        self.assertEqual(solution("""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""), 1656)


if __name__ == '__main__':
    unittest.main()
