""" Advent of code 2023 day 20 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """Test from the task"""
        self.assertEqual(
            solution(
                """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
            ),
            32000000,
        )

    def test_advanced(self):
        # return True
        self.assertEqual(
            solution(
                """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
            ),
            11687500,
        )


if __name__ == "__main__":
    unittest.main()
