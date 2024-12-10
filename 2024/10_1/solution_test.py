""" Advent of code 2024 day 10 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""0123
1234
8765
9876"""), 1)
        self.assertEqual(solution("""...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""), 2)
        self.assertEqual(solution("""..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""), 4)
        self.assertEqual(solution("""10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""), 1+2)
        self.assertEqual(solution("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""), 36)


if __name__ == "__main__":
    unittest.main()
