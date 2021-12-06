""" Advent of code 2021 day 06 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""3,4,3,1,2"""), 5934)


if __name__ == '__main__':
    unittest.main()
