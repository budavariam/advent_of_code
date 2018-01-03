""" Advent of code 2017	day 24/1 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("""0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""), 31)

if __name__ == '__main__':
    unittest.main()
