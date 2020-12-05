""" Advent of code 2020 day 5/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL\
"""), 820)


if __name__ == '__main__':
    unittest.main()
