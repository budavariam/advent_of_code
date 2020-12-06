""" Advent of code 2020 day 6/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
abc

a
b
c

ab
ac

a
a
a
a

b\
"""), 6)


if __name__ == '__main__':
    unittest.main()
