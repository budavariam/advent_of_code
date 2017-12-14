""" Advent of code 2017	day 13/1 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("""0: 3
1: 2
4: 4
6: 4"""), 24)

if __name__ == '__main__':
    unittest.main()
