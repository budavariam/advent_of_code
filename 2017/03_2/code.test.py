""" Advent of code 2017	day 2/2	"""

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution(2), 4)
        self.assertEqual(solution(3), 4)
        self.assertEqual(solution(4), 5)
        self.assertEqual(solution(5), 10)

    def test_custom(self):
        """ My test cases """
        self.assertEqual(solution(57), 59)

if __name__ == '__main__':
    unittest.main()
