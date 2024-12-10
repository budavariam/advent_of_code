""" Advent of code 2024 day 10 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(
            solution(
                """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""
            ),
            3,
        )
        self.assertEqual(
            solution(
                """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
            ),
            13,
        )
        self.assertEqual(
            solution(
                """012345
123456
234567
345678
4.6789
56789."""
            ),
            227,
        )
        self.assertEqual(
            solution(
                """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
            ),
            81,
        )


if __name__ == "__main__":
    unittest.main()
