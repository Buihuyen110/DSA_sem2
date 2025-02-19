import unittest
from Lab1.Task13.src.souvenir import partition_subsets
from Lab1.utils import time_memory

class TestPartitionSubsets(unittest.TestCase):

    @time_memory
    def test_example_1(self):
        # given
        souvenirs = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
        expected_result = 1

        # when
        result = partition_subsets(souvenirs)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_2(self):
        # given
        souvenirs = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
        expected_result = 1

        # when
        result = partition_subsets(souvenirs)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_3(self):
        # given
        souvenirs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected_result = 1

        # when
        result = partition_subsets(souvenirs)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()