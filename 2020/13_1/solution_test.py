""" Advent of code 2020 day 13/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
939
7,13,x,x,59,x,31,19\
"""), 295)


if __name__ == '__main__':
    unittest.main()
