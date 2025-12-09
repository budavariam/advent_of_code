""" Advent of code 2025 day 06 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """), 4277556)


if __name__ == "__main__":
    unittest.main()
