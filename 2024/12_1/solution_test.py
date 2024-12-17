""" Advent of code 2024 day 12 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""AAAA
BBCD
BBCC
EEEC"""), 140)
        self.assertEqual(solution("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""), 772)
        self.assertEqual(solution("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""), 1930)


if __name__ == "__main__":
    unittest.main()
