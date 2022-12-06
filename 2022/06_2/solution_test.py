""" Advent of code 2022 day 06 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(solution("""mjqjpqmgbljsphdztnvjfqwrcgsmlb"""), 19)
        self.assertEqual(solution("""bvwbjplbgvbhsrlpgdmjqwftvncz"""), 23)
        self.assertEqual(solution("""nppdvjthqldpwncqszvftbrmjlhg"""), 23)
        self.assertEqual(solution("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""), 29)
        self.assertEqual(solution("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""), 26)


if __name__ == "__main__":
    unittest.main()
