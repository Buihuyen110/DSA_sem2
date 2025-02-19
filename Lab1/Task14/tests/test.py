import unittest
from Lab1.Task14.src.max_value import max_value
from Lab1.utils import time_memory

class TestMaxValue(unittest.TestCase):

    @time_memory
    def test_example_1(self):
        # given
        expression = "1+5"
        expected_result = 6

        # when
        result = max_value(expression)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_2(self):
        # given
        expression = "5-8+7*4-8+9"
        expected_result = 200

        # when
        result = max_value(expression)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_large_input(self):
        # given
        expression = "1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1"
        expected_result = 29  # (1+2)*3 - 4*5 + 6*(7-8)*9 + 10*(11-12)*13 + 14

        # when
        result = max_value(expression)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()