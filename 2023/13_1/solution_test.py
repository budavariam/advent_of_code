""" Advent of code 2023 day 13 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""), 405)
        self.assertEqual(solution("""###.#....#.
#..########
...##.##.##
.#..#....#.
.###..##..#
.#.#.#..#.#
.#.#.#..#.#
.###..##..#
.#..#....#.
...##.##.##
#..########
#.#.#....#.
##.#......#
#.....##...
##.##....##"""), 7)


if __name__ == "__main__":
    unittest.main()
