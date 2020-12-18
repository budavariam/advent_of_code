""" Advent of code 2020 day 18/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(
            solution("""2 * 3 + (4 * 5)"""), 26)
        self.assertEqual(
            solution("""5 + (8 * 3 + 9 + 3 * 4 * 3)"""), 437)
        self.assertEqual(
            solution("""5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"""), 12240)
        self.assertEqual(
            solution("""((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""), 13632)


if __name__ == '__main__':
    unittest.main()
