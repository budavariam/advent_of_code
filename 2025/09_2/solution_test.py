""" Advent of code 2025 day 09 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""), 24)


if __name__ == "__main__":
    unittest.main()
