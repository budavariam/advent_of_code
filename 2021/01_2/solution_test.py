""" Advent of code 2021 day 01/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""199
200
208
210
200
207
240
269
260
263"""), 5)


if __name__ == '__main__':
    unittest.main()
