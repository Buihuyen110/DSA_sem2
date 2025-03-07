import unittest
from Lab2.Task11.src.balanced_bst import main
from Lab2.utils import time_memory


class TestAVLTreeOperations(unittest.TestCase):

    @time_memory
    def test_case_1(self):
        # give
        input_data = """insert 10
insert 20
insert 30
exists 20
prev 25
next 15"""
        expected_output = """true
20
20"""

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
        input_data = """insert 50
insert 30
insert 70
delete 30
exists 30
prev 50
next 50"""
        expected_output = """false
none
70"""

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
        input_data = """insert 100
insert 200
insert 50
insert 150
delete 100
exists 100
prev 200
next 50"""
        expected_output = """false
150
150"""

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

