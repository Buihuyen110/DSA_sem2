import unittest

from Lab4.Task7.src.find_max_substring import common_substring
from Lab4.utils import time_memory

class TestFindCommonSubstring(unittest.TestCase):

    @time_memory
    def test1(self):
        # give
        s = 'abcdefg'
        t = 'abcxyz'
        expected_result = ([(0, 0)], 3)

        # when
        results = common_substring(s, t)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test2(self):
        # give
        s = 'abcd'
        t = 'xyz'
        expected_result = ([(0, 0)], 0)

        # when
        results = common_substring(s, t)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test3(self):
        # give
        s = 'aabbaahkafhkafhkndndjerwwfgsgvss'
        t = 'jerww'
        expected_result =  ([(20, 0)], 5)

        # when
        results = common_substring(s, t)

        # then
        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
