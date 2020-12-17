""" Advent of code 2020 day 15/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""0,3,6"""), 436)
        self.assertEqual(solution("""1,3,2"""), 1)
        self.assertEqual(solution("""2,1,3"""), 10)
        self.assertEqual(solution("""1,2,3"""), 27)
        self.assertEqual(solution("""2,3,1"""), 78)
        self.assertEqual(solution("""3,2,1"""), 438)
        self.assertEqual(solution("""3,1,2"""), 1836)


if __name__ == '__main__':
    unittest.main()
