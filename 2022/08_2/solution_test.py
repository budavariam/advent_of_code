""" Advent of code 2022 day 08 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""30373
25512
65332
33549
35390"""), 8)


if __name__ == "__main__":
    unittest.main()
