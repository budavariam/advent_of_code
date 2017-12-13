""" Advent of code 2017	day 9/1	"""

import unittest
from code import solution

class MyTest(unittest.TestCase):
    """Unit tests for actual day"""

    def test_match(self):
        """ The basic test cases """
        self.assertEqual(solution("{}"), 1)
        self.assertEqual(solution("{{{}}}"), 6)
        self.assertEqual(solution("{{},{}}"), 5)
        self.assertEqual(solution("{{{},{},{{}}}}"), 16)
        self.assertEqual(solution("{<a>,<a>,<a>,<a>}"), 1)
        self.assertEqual(solution("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
        self.assertEqual(solution("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
        self.assertEqual(solution("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)

if __name__ == '__main__':
    unittest.main()
