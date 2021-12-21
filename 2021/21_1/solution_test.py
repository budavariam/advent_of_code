""" Advent of code 2021 day 21 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""Player 1 starting position: 4
Player 2 starting position: 8"""), 739785)


if __name__ == '__main__':
    unittest.main()
