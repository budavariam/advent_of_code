""" Advent of code 2022 day 20 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""1
2
-3
3
-2
0
4"""), 3)


if __name__ == "__main__":
    unittest.main()
