""" Advent of code 2021 day 07 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""16,1,2,0,4,2,7,1,2,14"""), 168)


if __name__ == '__main__':
    unittest.main()
