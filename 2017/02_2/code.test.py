""" Advent of code 2017	day 2/2	"""

import unittest
from code import solution, row

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""
    def test_match(self):
        """ The basic test cases """
        self.assertEqual(row("5	9	2	8"), 4)
        self.assertEqual(row("9	4	7	3"), 3)
        self.assertEqual(row("3	8	6	5"), 2)
        self.assertEqual(solution("""5	9	2	8
                9	4	7	3
                3	8	6	5"""), 9)

if __name__ == '__main__':
    unittest.main()
