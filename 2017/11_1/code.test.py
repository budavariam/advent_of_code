""" Advent of code 2017	day 11/1 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("ne,ne,ne"), 3)
        self.assertEqual(solution("ne,ne,sw,sw"), 0)
        self.assertEqual(solution("ne,ne,s,s"), 2)
        self.assertEqual(solution("se,sw,se,sw,sw"), 3)


if __name__ == '__main__':
    unittest.main()
