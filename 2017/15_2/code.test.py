""" Advent of code 2017	day 15/2 """

import unittest
from code import solution, Judge

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("""Generator A starts with 65
Generator B starts with 8921"""), 309)

    def test_judge_cmp(self):
        """ Test compare function """
        judge = Judge([0, 0], 0)
        self.assertEqual(judge.compare(1352636452, 1233683848), False)
        self.assertEqual(judge.compare(1992081072,  862516352), False)
        self.assertEqual(judge.compare( 530830436, 1159784568), False)
        self.assertEqual(judge.compare(1980017072, 1616057672), False)
        self.assertEqual(judge.compare( 740335192, 412269392), False)
        self.assertEqual(judge.compare( 1023762912, 896885216), True)

if __name__ == '__main__':
    unittest.main()
