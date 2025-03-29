import unittest
from Lab4.Task6.src.z_function import z_function
from Lab4.utils import time_memory

class TestZFunction(unittest.TestCase):

    @time_memory
    def test1(self):
        # give
        s = 'aaaaa'
        expected_result = [0, 4, 3, 2, 1]

        # when
        results = z_function(s)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test2(self):
        # give
        s = 'abacabab'
        expected_result = [0, 0, 1, 0, 3, 0, 2, 0]

        # when
        results = z_function(s)

        # then
        self.assertEqual(results, expected_result)


    @time_memory
    def test3(self):
        # give
        s = 'abcdefgh'
        expected_result = [0, 0, 0, 0, 0, 0, 0, 0]

        # when
        results = z_function(s)

        # then
        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
