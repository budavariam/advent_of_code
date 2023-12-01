""" Advent of code 2023 day 01 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""), 142)


if __name__ == "__main__":
    unittest.main()
