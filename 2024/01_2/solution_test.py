""" Advent of code 2023 day 01 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""3   4
4   3
2   5
1   3
3   9
3   3"""), 31)


if __name__ == "__main__":
    unittest.main()
