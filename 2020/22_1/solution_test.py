""" Advent of code 2020 day 22/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10\
"""), 306)


if __name__ == '__main__':
    unittest.main()
