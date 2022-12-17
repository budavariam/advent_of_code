""" Advent of code 2022 day 17 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution(""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""), 1514285714288)


if __name__ == "__main__":
    unittest.main()
