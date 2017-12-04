""" Advent of code 2017	day 4/2	"""

import unittest
from code import is_valid

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(is_valid("abcde fghij"), True)
        self.assertEqual(is_valid("a ab abc abd abf abj"), True)
        self.assertEqual(is_valid("iiii oiii ooii oooi oooo"), True)
        self.assertEqual(is_valid("abcde xyz ecdab"), False)
        self.assertEqual(is_valid("oiii ioii iioi iiio"), False)

if __name__ == '__main__':
    unittest.main()
