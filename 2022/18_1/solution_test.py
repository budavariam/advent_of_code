""" Advent of code 2022 day 18 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""1,1,1
2,1,1"""), 10)
        self.assertEqual(solution("""2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""), 64)


if __name__ == "__main__":
    unittest.main()
