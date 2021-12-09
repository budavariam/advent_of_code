""" Advent of code 2021 day 09 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""2199943210
3987894921
9856789892
8767896789
9899965678"""), 1134)


if __name__ == '__main__':
    unittest.main()
