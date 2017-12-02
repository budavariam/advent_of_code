""" Advent of code 2017	day 2/1	"""

import unittest
from code import solution, row

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""
    def test_match(self):
        """ The basic test cases """
        self.assertEqual(row("5	1	9	5"), 8)
        self.assertEqual(row("7	5	3"), 4)
        self.assertEqual(row("2	4	6	8"), 6)
        self.assertEqual(solution("""5	1	9	5
        7	5	3
        2	4	6	8"""), 18)

if __name__ == '__main__':
    unittest.main()
