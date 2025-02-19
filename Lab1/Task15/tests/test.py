import unittest
from Lab1.Task15.src.delete_bracket import delete_bracket
from Lab1.utils import time_memory

class TestDeleteBracket(unittest.TestCase):

    @time_memory
    def test_example_1(self):
        # given
        s = '{{[(])}}'
        expected_result = '{{()}}'

        # when
        result = delete_bracket(s)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_2(self):
        # given
        s = '(]{[})'
        expected_result = '({})'

        # when
        result = delete_bracket(s)

        # then
        self.assertEqual(result, expected_result)

    @time_memory
    def test_example_3(self):
        # given
        s = '((())]]][[[[{}{}]]])'
        expected_result = '((())[[[{}{}]]])'

        # when
        result = delete_bracket(s)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()