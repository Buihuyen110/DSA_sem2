import unittest
from Lab3.utils import time_memory
from Lab3.Task4.src.main import topological_sort

class TestTopologicalSort(unittest.TestCase):

    @time_memory
    def test1(self):
        # give
        n = 4
        edges = [(3, 1)]
        expected_result = [4, 3, 2, 1]

        # when
        results = topological_sort(n, edges)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test2(self):
        # give
        n = 5
        edges = [(2, 1), (3, 2), (3, 1), (4, 3), (4, 1), (5, 2), (5, 3)]
        expected_result = [5, 4, 3, 2, 1]

        # when
        results = topological_sort(n, edges)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test3(self):
        # give
        n = 6
        edges = [(6, 3), (6, 1), (5, 1), (5, 2), (3, 4), (4, 2)]
        expected_result = [6, 5, 3, 4, 2, 1]

        # when
        results = topological_sort(n, edges)

        # then
        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
