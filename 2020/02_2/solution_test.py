""" Advent of code 2020 day 2/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""), 1)


if __name__ == '__main__':
    unittest.main()
