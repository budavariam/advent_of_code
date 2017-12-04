""" Advent of code 2017	day 4/1	"""

import unittest
from code import is_valid

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(is_valid("aa bb cc dd ee"), True)
        self.assertEqual(is_valid("aa bb cc dd aa"), False)
        self.assertEqual(is_valid("aa bb cc dd aaa"), True)

if __name__ == '__main__':
    unittest.main()
