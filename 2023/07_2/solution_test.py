""" Advent of code 2023 day 07 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""), 5905)


if __name__ == "__main__":
    unittest.main()
