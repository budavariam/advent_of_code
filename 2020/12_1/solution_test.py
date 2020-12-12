""" Advent of code 2020 day 12/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
F10
N3
F7
R90
F11\
"""), 25)


if __name__ == '__main__':
    unittest.main()
