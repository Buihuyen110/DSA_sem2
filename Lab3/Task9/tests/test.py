import unittest
from Lab3.Task9.src.main import bellman_ford
from Lab3.utils import time_memory

class TestBellmanFord(unittest.TestCase):

    @time_memory
    def test_case_1(self):
        # give
        n = 3
        edges = [(1, 2, -2), (2, 3, -2), (3, 1, -2)]
        expected_result = 1

        # when
        results = bellman_ford(n, edges)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test_case_2(self):
        # give
        n = 4
        edges = [(1, 2, 3), (2, 3, 4), (3, 4, -8), (4, 1, -2)]
        expected_result = 1

        # when
        results = bellman_ford(n, edges)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test_case_3(self):
        # give
        n = 5
        edges = []
        expected_result = 0

        # when
        results = bellman_ford(n, edges)

        # then
        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
