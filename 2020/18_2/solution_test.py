""" Advent of code 2020 day 18/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(
            solution("""1 + (2 * 3) + (4 * (5 + 6))"""), 51)
        self.assertEqual(
            solution("""2 * 3 + (4 * 5)"""), 46)
        self.assertEqual(
            solution("""5 + (8 * 3 + 9 + 3 * 4 * 3)"""), 1445)
        self.assertEqual(
            solution("""5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"""), 669060)
        self.assertEqual(
            solution("""((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""), 23340)


if __name__ == '__main__':
    unittest.main()
