""" Advent of code 2025 day 05 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""), 14)


if __name__ == "__main__":
    unittest.main()
