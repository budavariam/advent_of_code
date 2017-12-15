""" Advent of code 2017	day 15/1 """

import unittest
from code import solution, Judge

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("""Generator A starts with 699
Generator B starts with 124"""), 588)

    def test_judge_cmp(self):
        """ Test compare function """
        judge = Judge([0, 0], 0)
        self.assertEqual(judge.compare(1092455, 430625591), False)
        self.assertEqual(judge.compare(1181022009, 1233683848), False)
        self.assertEqual(judge.compare(245556042, 1431495498), True)
        self.assertEqual(judge.compare(1744312007, 137874439), False)
        self.assertEqual(judge.compare(1352636452, 285222916), False)

if __name__ == '__main__':
    unittest.main()
