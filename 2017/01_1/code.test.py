""" Advent of code 2017 day 1/1 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""
    def test_basic(self):
        """ Summary is good """
        self.assertEqual(solution(1122), 3)

    def test_none(self):
        """ Nothing repeats """
        self.assertEqual(solution(1234), 0)

    def test_allsame(self):
        """ All element is the same """
        self.assertEqual(solution(1111), 4)

    def test_rotate(self):
        """ The only matching elem is in the end """
        self.assertEqual(solution(91212129), 9)

if __name__ == '__main__':
    unittest.main()
