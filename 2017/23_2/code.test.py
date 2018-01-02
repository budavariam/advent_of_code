""" Advent of code 2017	day 23/1 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("""set b 81"""), 909)
        self.assertEqual(solution("""set b 79"""), 907)

if __name__ == '__main__':
    unittest.main()
