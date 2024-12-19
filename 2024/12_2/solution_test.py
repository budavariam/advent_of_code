""" Advent of code 2024 day 12 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""), 436)
        self.assertEqual(solution("""AAAA
BBCD
BBCC
EEEC"""), 80)
        self.assertEqual(solution("""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""), 236)
        self.assertEqual(solution("""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""), 368)
        self.assertEqual(solution("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""), 1206)


if __name__ == "__main__":
    unittest.main()
