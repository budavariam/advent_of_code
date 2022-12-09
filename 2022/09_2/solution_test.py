""" Advent of code 2022 day 09 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""), 36)
        self.assertEqual(solution("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""), 1)


if __name__ == "__main__":
    unittest.main()
