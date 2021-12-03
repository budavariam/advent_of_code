""" Advent of code 2021 day 03/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""), 230)


if __name__ == '__main__':
    unittest.main()
