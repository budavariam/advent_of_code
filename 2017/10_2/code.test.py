""" Advent of code 2017	day 10/2 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution(256, ""), "a2582a3a0e66e6e86e3812dcb672a272")
        self.assertEqual(solution(256, "AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
        self.assertEqual(solution(256, "1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
        self.assertEqual(solution(256, "1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")

if __name__ == '__main__':
    unittest.main()
