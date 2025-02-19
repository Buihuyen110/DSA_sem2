import unittest
from Lab1.Task20.src.count_palindromes import count_palindromes
from Lab1.utils import time_memory

class TestCountPolindromes(unittest.TestCase):

    @time_memory
    def test_example_1(self):
        # given
        N = 5
        K = 1
        S = "abcde"
        expected_result = 12

        # when
        result = count_palindromes(N, K, S)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_2(self):
        # given
        N = 3
        K = 3
        S = "aaa"
        expected_result = 6

        # when
        result = count_palindromes(N, K, S)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_3(self):
        # given
        N = 200
        K = 2
        S = "a" * N
        expected_result = 20100

        # when
        result = count_palindromes(N, K, S)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()