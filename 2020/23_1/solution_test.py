""" Advent of code 2020 day 23/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""389125467"""), "67384529")


if __name__ == '__main__':
    unittest.main()
