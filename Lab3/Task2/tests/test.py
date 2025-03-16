import unittest
from Lab3.utils import time_memory
from Lab3.Task2.src.main import find_connected_components

class TestFindComponents(unittest.TestCase):

    @time_memory
    def test1(self):
        # give
        n = 5
        m = 0
        edges = []
        expected_result = 5

        # when
        results = find_connected_components(n, m, edges)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test2(self):
        # give
        n = 6
        m = 3
        edges = [(1, 2), (2, 3), (4, 5)]
        expected_result = 3

        # when
        results = find_connected_components(n, m, edges)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test3(self):
        # give
        n = 6
        m = 4
        edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
        expected_result = 2

        # when
        results = find_connected_components(n, m, edges)

        # then
        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
