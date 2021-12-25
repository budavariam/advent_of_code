""" Advent of code 2021 day 25 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        # self.assertEqual(solution("""...>>>>>..."""), None)
#         self.assertEqual(solution("""..........
# .>v....v..
# .......>..
# .........."""), None)
#         self.assertEqual(solution("""...>...
# .......
# ......>
# v.....>
# ......>
# .......
# ..vvv.."""), None)
        self.assertEqual(solution("""v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""), 58)


if __name__ == '__main__':
    unittest.main()
