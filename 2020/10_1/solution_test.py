""" Advent of code 2020 day 10/1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""\
16
10
15
5
1
11
7
19
6
12
4\
"""), 35)

        self.assertEqual(solution("""\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3\
"""), 220)


if __name__ == '__main__':
    unittest.main()
