import unittest
from Lab1.utils import time_memory
from Lab2.Task10.src.Is_bst import is_bst


class TestBSTValidation(unittest.TestCase):

    @time_memory
    def test_case_1(self):
        # give
        n = 0
        nodes = []
        expected_output = "YES"

        # when
        result = is_bst(n, nodes)

        # then
        self.assertEqual(result, expected_output)

    @time_memory
    def test_case_2(self):
        # give
        n = 3
        nodes = [(5, 2, 3), (6, 0, 0), (4, 0, 0)]
        expected_output = "NO"

        # when
        result = is_bst(n, nodes)

        # then
        self.assertEqual(result, expected_output)

    @time_memory
    def test_case_3(self):
        # give
        n = 5
        nodes = [(20, 2, 3), (10, 4, 5), (30, 0, 0), (5, 0, 0), (25, 0, 0)]
        expected_output = "NO"

        # when
        result = is_bst(n, nodes)

        # then
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()

