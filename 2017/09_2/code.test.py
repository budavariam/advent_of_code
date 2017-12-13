""" Advent of code 2017	day 9/1	"""

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("<>"), 0)
        self.assertEqual(solution("<random characters>"), 17)
        self.assertEqual(solution("<<<<>"), 3)
        self.assertEqual(solution("<{!>}>"), 2)
        self.assertEqual(solution("<!!>"), 0)
        self.assertEqual(solution("<!!!>>"), 0)
        self.assertEqual(solution("""<{o"i!a,<{i<a>"""), 10)

if __name__ == '__main__':
    unittest.main()
