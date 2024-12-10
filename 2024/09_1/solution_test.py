""" Advent of code 2024 day 09 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""2333133121414131402"""), 1928)


if __name__ == "__main__":
    unittest.main()
