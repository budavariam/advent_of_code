""" Advent of code 2023 day 21 / 2 """

import unittest
from solution import solution


INFINITE_MAP = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""


def generate_test_case(input_value, expected_value):
    def test(self):
        """Test from the task"""
        self.assertEqual(
            solution(data=INFINITE_MAP, remaining_steps=input_value), expected_value
        )

    return test


for idx, (param, expected) in enumerate(
    [
        (6, 16),
        (10, 50),
        (50, 1594),
        (100, 6536),
        (500, 167004),
        (1000, 668697),
        (5000, 16733044),
    ]
):
    setattr(MyTest, f"test_{idx + 1}", generate_test_case(param, expected))

if __name__ == "__main__":
    unittest.main()
