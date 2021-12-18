""" Advent of code 2021 day 18 / 1 """

import unittest
from solution import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution("""[1,2]"""), 7)
        self.assertEqual(solution("""[1,[1,2]]"""), 17)
        self.assertEqual(solution("""[[1,2],[[3,4],5]]"""), 143)
        self.assertEqual(
            solution("""[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"""), 1384)
        self.assertEqual(solution("""[[[[1,1],[2,2]],[3,3]],[4,4]]"""), 445)
        self.assertEqual(solution("""[[[[3,0],[5,3]],[4,4]],[5,5]]"""), 791)
        self.assertEqual(solution("""[[[[5,0],[7,4]],[5,5]],[6,6]]"""), 1137)
        self.assertEqual(
            solution("""[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"""), 3488)
        self.assertEqual(solution("""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""), 4140)


if __name__ == '__main__':
    unittest.main()
