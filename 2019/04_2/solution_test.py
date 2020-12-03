""" Advent of code 2019 day 4/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Summary is good """
        self.assertEqual(solution("112233-112234"), 1)
        self.assertEqual(solution("123444-123445"), 0)
        self.assertEqual(solution("111122-111123"), 1)


if __name__ == '__main__':
    unittest.main()
