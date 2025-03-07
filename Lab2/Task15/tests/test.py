import unittest

from Lab2.utils import time_memory
from Lab2.Task15.src.tree_avl import main

class TestAVLTree(unittest.TestCase):

    @time_memory
    def test_case_1(self):
        # give
        input_data = "3\n10 2 3\n5 0 0\n15 0 0\n10\n"
        expected_output = "2\n5 0 2\n15 0 0\n"

        # when
        with open("../txtf/input.txt", "w") as f:
            f.write(input_data)

        main()

        with open("../txtf/output.txt", "r") as f:
            result = f.read()

        # then
        self.assertEqual(result.strip(), expected_output.strip())

    @time_memory
    def test_case_2(self):
        # give
        input_data = "5\n20 2 3\n10 4 5\n30 0 0\n5 0 0\n15 0 0\n10\n"
        expected_output = "4\n20 2 4\n5 0 3\n15 0 0\n30 0 0\n"

        # when
        with open("../txtf/input.txt", "w") as f:
            f.write(input_data)

        main()

        with open("../txtf/output.txt", "r") as f:
            result = f.read()

        # then
        self.assertEqual(result.strip(), expected_output.strip())

    @time_memory
    def test_case_3(self):
        # give
        input_data = "7\n50 2 3\n30 4 5\n70 6 7\n20 0 0\n40 0 0\n60 0 0\n80 0 0\n30\n"
        expected_output = "6\n50 2 4\n20 0 3\n40 0 0\n70 5 6\n60 0 0\n80 0 0\n"

        # when
        with open("../txtf/input.txt", "w") as f:
            f.write(input_data)

        main()

        with open("../txtf/output.txt", "r") as f:
            result = f.read()

        # then
        self.assertEqual(result.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()