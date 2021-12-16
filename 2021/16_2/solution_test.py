""" Advent of code 2021 day 16 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""C200B40A82"""), 3)
        self.assertEqual(solution("""04005AC33890"""), 54)
        self.assertEqual(solution("""880086C3E88112"""), 7)
        self.assertEqual(solution("""CE00C43D881120"""), 9)
        self.assertEqual(solution("""D8005AC2A8F0"""), 1)
        self.assertEqual(solution("""F600BC2D8F"""), 0)
        self.assertEqual(solution("""9C005AC2F8F0"""), 0)
        self.assertEqual(solution("""9C0141080250320F1802104A08"""), 1)


if __name__ == '__main__':
    unittest.main()
