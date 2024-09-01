""" Advent of code 2023 day 10 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""), 4)
        self.assertEqual(solution("""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""), 8)


if __name__ == "__main__":
    unittest.main()
