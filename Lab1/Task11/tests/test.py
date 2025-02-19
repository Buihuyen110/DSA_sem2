import unittest
from Lab1.Task11.src.max_gold import max_gold
from Lab1.utils import time_memory

class TestMaxGold(unittest.TestCase):

    @time_memory
    def test_1(self):
        # give
        W = 10
        n = 3
        weights = [1, 4, 8]
        expected_result = 9

        # which
        result = max_gold(W, n, weights)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_2(self):
        # give
        W = 15
        n = 4
        weights = [2, 3, 4, 5]
        expected_result = 14

        # which
        result = max_gold(W, n, weights)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_3(self):
        # give
        W = 100
        n = 3
        weights = [1, 2, 98]
        expected_result = 100

        # which
        result = max_gold(W, n, weights)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_4(self):
        # give
        W = 10000
        n = 300
        weights = [i for i in range(1, 301)]
        expected_result = 10000

        # which
        result = max_gold(W, n, weights)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
