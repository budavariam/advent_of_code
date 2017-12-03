""" Advent of code 2017	day 2/2	"""

import unittest
from code import solution, start_point, count_y, side_pos

class MyTest(unittest.TestCase):
    """Unist tests for actual day"""
    def test_start(self):
        """ Test start point """
        self.assertEqual(start_point(52), (50, 5))
        self.assertEqual(start_point(61), (50, 5))
        self.assertEqual(start_point(31), (26, 4))
        self.assertEqual(start_point(47), (26, 4))
        self.assertEqual(start_point(19), (10, 3))
        self.assertEqual(start_point(3), (2, 2))
        self.assertEqual(start_point(1), (1, 1))

    def test_y(self):
        """ Test y value """
        self.assertEquals(count_y(1, 4), 1)
        self.assertEquals(count_y(0, 4), 2)
        self.assertEquals(count_y(4, 4), 2)
        self.assertEquals(count_y(4, 5), 1)
        self.assertEquals(count_y(0, 5), 3)
        self.assertEquals(count_y(1, 2), 1)
        self.assertEquals(count_y(3, 3), 2)
        self.assertEquals(count_y(2, 3), 1)
        self.assertEquals(count_y(1, 3), 0)
        self.assertEquals(count_y(0, 3), 1)

    def test_side(self):
        """ Test side position """
        self.assertEquals(side_pos(4, 2, 2), 0)
        self.assertEquals(side_pos(21, 10, 3), 3)
        self.assertEquals(side_pos(45, 26, 4), 1)
        self.assertEquals(side_pos(69, 50, 5), 3)
        self.assertEquals(side_pos(65, 50, 5), 7)
        self.assertEquals(side_pos(50, 50, 5), 0)
        self.assertEquals(side_pos(21, 10, 3), 3)

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution(12), 3)
        self.assertEqual(solution(23), 2)
        self.assertEqual(solution(1024), 31)
        self.assertEqual(solution(1), 0)

if __name__ == '__main__':
    unittest.main()
