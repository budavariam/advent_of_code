""" Advent of code 2017	day 16/1 """

import unittest
from code import Dance

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(Dance("""s1,x3/4,pe/b""", 'a', 'e').process(), "baedc")

if __name__ == '__main__':
    unittest.main()
