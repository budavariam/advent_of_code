""" Advent of code 2017	day 2/2	"""

import unittest
from code import solution, start_point, count_y, side_pos

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution(1), 1)
        self.assertEqual(solution(2), 1)
        self.assertEqual(solution(3), 2)
        self.assertEqual(solution(4), 4)
        self.assertEqual(solution(5), 5)

if __name__ == '__main__':
    unittest.main()
