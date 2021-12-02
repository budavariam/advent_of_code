""" Advent of code 2021 day 02/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""forward 5
down 5
forward 8
up 3
down 8
forward 2"""), 150)


if __name__ == '__main__':
    unittest.main()
