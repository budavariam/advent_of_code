""" Advent of code 2017	day 6/1	"""

import unittest
from code import solution, Debugger

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("0\t2\t7\t0"), 4)

if __name__ == '__main__':
    unittest.main()
