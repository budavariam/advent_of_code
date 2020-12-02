""" Advent of code 2019 day 4/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Summary is good """
        self.assertEqual(solution("111111-111112"), 1)
        self.assertEqual(solution("2233450-2233451"), 0)
        self.assertEqual(solution("123789-123790"), 0)


if __name__ == '__main__':
    unittest.main()
