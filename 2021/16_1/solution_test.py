""" Advent of code 2021 day 16 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        # self.assertEqual(solution("""D2FE28"""), 6)
        self.assertEqual(solution("""8A004A801A8002F478"""), 16)
        self.assertEqual(solution("""620080001611562C8802118E34"""), 12)
        self.assertEqual(solution("""C0015000016115A2E0802F182340"""), 23)
        self.assertEqual(solution("""A0016C880162017C3686B18A3D4780"""), 31)
        # self.assertEqual(solution("""38006F45291200"""), 0)


if __name__ == '__main__':
    unittest.main()
