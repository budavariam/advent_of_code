""" Advent of code 2020 day 15/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""0,3,6"""), 175594)
        self.assertEqual(solution("""1,3,2"""), 2578)
        self.assertEqual(solution("""2,1,3"""), 3544142)
        self.assertEqual(solution("""1,2,3"""), 261214)
        self.assertEqual(solution("""2,3,1"""), 6895259)
        self.assertEqual(solution("""3,2,1"""), 18)
        self.assertEqual(solution("""3,1,2"""), 362)


if __name__ == '__main__':
    unittest.main()
