""" Advent of code 2020 day 1/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""1721
979
366
299
675
1456"""), 514579)


if __name__ == '__main__':
    unittest.main()
