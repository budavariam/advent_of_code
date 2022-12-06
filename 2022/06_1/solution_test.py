""" Advent of code 2022 day 06 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""mjqjpqmgbljsphdztnvjfqwrcgsmlb"""), 7)
        self.assertEqual(solution("""bvwbjplbgvbhsrlpgdmjqwftvncz"""), 5)
        self.assertEqual(solution("""nppdvjthqldpwncqszvftbrmjlhg"""), 6)
        self.assertEqual(solution("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""), 10)
        self.assertEqual(solution("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""), 11)


if __name__ == "__main__":
    unittest.main()
