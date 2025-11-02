"""Advent of code 2024 day 20 / 1"""

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(
            solution(
                """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""", 0
            ),
            set(
                [
                    # cnt, saves ps
                    (14, 2),
                    (14, 4),
                    (2, 6),
                    (4, 8),
                    (2, 10),
                    (3, 12),
                    (1, 20),
                    (1, 36),
                    (1, 38),
                    (1, 40),
                    (1, 64),
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
