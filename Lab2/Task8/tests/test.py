import unittest
from Lab1.utils import time_memory
from Lab2.Task8.src.tree_height import main


class TestBSTHeight(unittest.TestCase):

    @time_memory
    def test_case_1(self):
        input_data = "3\n10 2 3\n5 0 0\n15 0 0\n"
        expected_output = "2\n"
        with open("../txtf/input.txt", "w") as f:
            f.write(input_data)
        main()
        with open("../txtf/output.txt", "r") as f:
            result = f.read()
        self.assertEqual(result, expected_output)

    @time_memory
    def test_case_2(self):
        input_data = "5\n20 2 3\n10 4 5\n30 0 0\n5 0 0\n15 0 0\n"
        expected_output = "3\n"
        with open("../txtf/input.txt", "w") as f:
            f.write(input_data)
        main()
        with open("../txtf/output.txt", "r") as f:
            result = f.read()
        self.assertEqual(result, expected_output)

    @time_memory
    def test_case_3(self):
        input_data = "7\n50 2 3\n30 4 5\n70 6 7\n20 0 0\n40 0 0\n60 0 0\n80 0 0\n"
        expected_output = "3\n"
        with open("../txtf/input.txt", "w") as f:
            f.write(input_data)
        main()
        with open("../txtf/output.txt", "r") as f:
            result = f.read()
        self.assertEqual(result, expected_output)



if __name__ == '__main__':
    unittest.main()
