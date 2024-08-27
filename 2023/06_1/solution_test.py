""" Advent of code 2023 day 06 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""Time:      7  15   30
Distance:  9  40  200"""), 288)


if __name__ == "__main__":
    unittest.main()
