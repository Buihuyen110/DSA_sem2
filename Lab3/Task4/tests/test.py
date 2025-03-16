import unittest
from Lab2.utils import time_memory
from Lab2.Task4.src.main import process_queries


class TestProcessQueries(unittest.TestCase):

    @time_memory
    def test_process_queries1(self):
        # give
        queries = [('+', 5), ('+', 3), ('+', 7), ('?', 1), ('?', 2), ('?', 3)]
        expected_result = [3, 5, 7]

        # when
        results = process_queries(queries)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test_process_queries2(self):
        # give
        queries = [('+', 5), ('+', 3), ('+', 7)]
        expected_result = []

        # when
        results = process_queries(queries)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test_process_queries3(self):
        # give
        queries = [('+', i) for i in range(1000)] + [('?', 500)]
        expected_result = [499]

        # when
        results = process_queries(queries)

        # then
        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
