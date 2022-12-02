""" Advent of code 2022 day 02 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""A Y
B X
C Z"""), 12)


if __name__ == "__main__":
    unittest.main()
