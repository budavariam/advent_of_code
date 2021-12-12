""" Advent of code 2021 day 12 / 2 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""start-A
start-b
A-c
A-b
b-d
A-end
b-end"""), 36)
        self.assertEqual(solution("""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""), 103)
        self.assertEqual(solution("""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""), 3509)


if __name__ == '__main__':
    unittest.main()
