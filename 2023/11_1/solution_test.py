""" Advent of code 2023 day 11 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""), 374)


if __name__ == "__main__":
    unittest.main()