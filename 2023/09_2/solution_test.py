""" Advent of code 2023 day 09 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""), 2)


if __name__ == "__main__":
    unittest.main()
