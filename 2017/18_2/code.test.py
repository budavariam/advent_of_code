""" Advent of code 2017	day 18/2 """

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("""snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""), 3)

if __name__ == '__main__':
    unittest.main()
