import unittest
from Lab1.Task17.src.count_phone_numbers import phone_numbers
from Lab1.utils import time_memory

class TestCountPolindromes(unittest.TestCase):

    @time_memory
    def test_example_1(self):
        # given
        N = 1
        expected_result = 8

        # when
        result = phone_numbers(N)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_2(self):
        # given
        N = 2
        expected_result = 16

        # when
        result = phone_numbers(N)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_3(self):
        # given
        N = 500
        expected_result = 915933184

        # when
        result = phone_numbers(N)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()