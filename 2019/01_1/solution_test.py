""" Advent of code 2019 day 1/1 """

import unittest
from solution import solution

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""
    def test_basic(self):
        """ Summary is good """
        self.assertEqual(solution("12"), 2)
        self.assertEqual(solution("14"), 2)
        self.assertEqual(solution("1969"), 654)
        self.assertEqual(solution("100756"), 33583)

if __name__ == '__main__':
    unittest.main()
