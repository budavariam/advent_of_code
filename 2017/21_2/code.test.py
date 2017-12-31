""" Advent of code 2017	day 21/2 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("""../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""", 2), 12)

if __name__ == '__main__':
    unittest.main()
