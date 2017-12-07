""" Advent of code 2017	day 6/1	"""

import unittest
from code import solution, Debugger

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("0\t2\t7\t0"), 5)

    def test_debugger(self):
        """ Test distribution cycle result """
        self.assertEqual(Debugger("0\t2\t7\t0").redistribution_cycle(), "2,4,1,2")
        self.assertEqual(Debugger("2\t4\t1\t2").redistribution_cycle(), "3,1,2,3")
        self.assertEqual(Debugger("3\t1\t2\t3").redistribution_cycle(), "0,2,3,4")
        self.assertEqual(Debugger("0\t2\t3\t4").redistribution_cycle(), "1,3,4,1")
        self.assertEqual(Debugger("1\t3\t4\t1").redistribution_cycle(), "2,4,1,2")

if __name__ == '__main__':
    unittest.main()
