import unittest
from Lab4.utils import time_memory
from Lab4.Task1.src.kmp_search import kmp_search


class TestFindOccurrences(unittest.TestCase):

    @time_memory
    def test1(self):
        # give
        p = 'a'
        t = 'banana'
        expected_result = [2, 4, 6]

        # when
        results = kmp_search(t, p)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test2(self):
        # give
        p = 'aba'
        t = 'abacabaababa'
        expected_result = [1, 5, 8, 10]

        # when
        results = kmp_search(t, p)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test3(self):
        # give
        p = 'aaa'
        t = 'aaaaaaaaaa'
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8]

        # when
        results = kmp_search(t, p)

        # then
        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
