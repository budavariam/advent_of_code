""" Advent of code 2020 day 23/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""389125467"""), 149245887792)


if __name__ == '__main__':
    unittest.main()
