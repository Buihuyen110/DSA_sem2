import unittest
from Lab1.Task2.src.min_refuels import min_refuels
from Lab1.utils import time_memory

class TestMinRefuels(unittest.TestCase):

    @time_memory
    def test_case_long_distance(self):
        # give
        d = 100000
        m = 400
        stops = list(range(400, 100001, 400))
        expected_result = 249

        # which
        result = min_refuels(d, m, stops)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_1(self):
        # give
        d = 950
        m = 400
        stops = [200, 375, 550, 750]
        expected_result = 2

        # which
        result = min_refuels(d, m, stops)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_2(self):
        # give
        d = 10
        m = 3
        stops = [1, 2, 5, 9]
        expected_result = -1

        # which
        result = min_refuels(d, m, stops)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_3(self):
        # give
        d = 200
        m = 250
        stops = [100, 150]
        expected_result = 0

        # which
        result = min_refuels(d, m, stops)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
