""" Advent of code 2024 day 22 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""1"""), 8685429)
        self.assertEqual(solution("""10"""), 4700978)
        self.assertEqual(solution("""100"""), 15273692)
        self.assertEqual(solution("""2024"""), 8667524)
        self.assertEqual(solution("""1
10
100
2024"""), 37327623)


if __name__ == "__main__":
    unittest.main()
