""" Advent of code 2025 day 01 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""), 6)


if __name__ == "__main__":
    unittest.main()
