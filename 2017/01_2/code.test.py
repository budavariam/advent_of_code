""" Advent of code 2017 day 1/2 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""
    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution(1212), 6)
        self.assertEqual(solution(1221), 0)
        self.assertEqual(solution(123425), 4)
        self.assertEqual(solution(123123), 12)
        self.assertEqual(solution(12131415), 4)

if __name__ == '__main__':
    unittest.main()
