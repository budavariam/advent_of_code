""" Advent of code 2022 day 12 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""), 29)


if __name__ == "__main__":
    unittest.main()
