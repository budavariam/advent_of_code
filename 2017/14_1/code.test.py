""" Advent of code 2017	day 14/1 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("flqrgnkx"), 8108)

if __name__ == '__main__':
    unittest.main()
