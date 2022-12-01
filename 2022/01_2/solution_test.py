""" Advent of code 2022 day 01 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""), 45000)


if __name__ == "__main__":
    unittest.main()
