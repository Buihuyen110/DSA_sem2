import unittest
from Lab1.Task7.src.max_repaired_boots import max_repaired_boots
from Lab1.utils import time_memory

class TestMaxRepairedBoots(unittest.TestCase):

    @time_memory
    def test_1(self):
        # give
        K = 10
        repair_time = [6, 2, 8]
        expected_result = 2

        # which
        result = max_repaired_boots(K, repair_time)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_2(self):
        # give
        K = 3
        repair_time = [10, 20]
        expected_result = 0

        # which
        result = max_repaired_boots(K, repair_time)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_3(self):
        # give
        K = 100
        repair_time = [1, 2, 3, 4, 5]
        expected_result = 5

        # which
        result = max_repaired_boots(K, repair_time)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_4(self):
        # give
        K = 1000
        repair_time = [i for i in range(1, 501)]
        expected_result = 44

        # which
        result = max_repaired_boots(K, repair_time)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
