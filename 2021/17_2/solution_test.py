""" Advent of code 2021 day 17 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""target area: x=20..30, y=-10..-5"""), 112)


if __name__ == '__main__':
    unittest.main()
