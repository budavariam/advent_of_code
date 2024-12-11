""" Advent of code 2024 day 11 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""125 17""", 1), 3)
        self.assertEqual(solution("""125 17""", 2), 4)
        self.assertEqual(solution("""125 17""", 3), 5)
        self.assertEqual(solution("""125 17""", 4), 9)
        self.assertEqual(solution("""125 17""", 5), 13)
        self.assertEqual(solution("""125 17""", 6), 22)


if __name__ == "__main__":
    unittest.main()
