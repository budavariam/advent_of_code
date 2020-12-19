""" Advent of code 2020 day 19/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

aab
aba
aaa
abb
bba
bab\
"""), 2)
        self.assertEqual(solution("""\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb\
"""), 2)


if __name__ == '__main__':
    unittest.main()
