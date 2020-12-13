""" Advent of code 2020 day 13/2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
939
7,13,x,x,59,x,31,19\
"""), 1068781)
        self.assertEqual(solution("""\

17,x,13,19\
"""), 3417)
        self.assertEqual(solution("""\

67,7,59,61\
"""), 754018)
        self.assertEqual(solution("""\

67,x,7,59,61\
"""), 779210)
        self.assertEqual(solution("""\

67,7,x,59,61\
"""), 1261476)
        self.assertEqual(solution("""\

1789,37,47,1889\
"""), 1202161486)


if __name__ == '__main__':
    unittest.main()
