""" Advent of code 2022 day 14 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""), 24)


if __name__ == "__main__":
    unittest.main()
