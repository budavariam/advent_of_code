""" Advent of code 2021 day 01/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution(""""""), 0)


if __name__ == '__main__':
    unittest.main()
