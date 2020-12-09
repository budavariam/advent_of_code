""" Advent of code 2020 day 09/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution(5, """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576\
"""), 62)


if __name__ == '__main__':
    unittest.main()
