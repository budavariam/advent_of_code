""" Advent of code 2020 day 25/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
5764801
17807724\
"""), 14897079)


if __name__ == '__main__':
    unittest.main()
