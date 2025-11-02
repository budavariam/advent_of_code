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
###############""",
                50,
            ),
            set(
                [
                    # cnt, saves ps
                    (32, 50),
                    (31, 52),
                    (29, 54),
                    (39, 56),
                    (25, 58),
                    (23, 60),
                    (20, 62),
                    (19, 64),
                    (12, 66),
                    (14, 68),
                    (12, 70),
                    (22, 72),
                    (4, 74),
                    (3, 76),
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
