""" Advent of code 2021 day {{cookiecutter.day}} / {{cookiecutter.part}} """

import unittest
from {{cookiecutter.main}} import solution


class MyTest(unittest.TestCase):
    """Unist tests for actual day"""

    def test_basic(self):
        """ Test from the task """
        self.assertEqual(solution(""""""), 0)


if __name__ == '__main__':
    unittest.main()
