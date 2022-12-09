""" Advent of code 2022 day 09 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""), 13)


if __name__ == "__main__":
    unittest.main()
