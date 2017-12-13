""" Advent of code 2017	day 10/1	"""

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution(5, "3, 4, 1, 5"), 12)

if __name__ == '__main__':
    unittest.main()
