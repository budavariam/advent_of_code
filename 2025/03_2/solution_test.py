""" Advent of code 2025 day 03 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""987654321111111
811111111111119
234234234234278
818181911112111"""), 3121910778619)


if __name__ == "__main__":
    unittest.main()
