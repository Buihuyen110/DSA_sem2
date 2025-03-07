import unittest
from Lab1.utils import time_memory
from Lab2.Task9.src.delete_subtree import build_tree, process_queries


class TestTreeDeletion(unittest.TestCase):

    @time_memory
    def test_case_1(self):
        # give
        nodes_data = [
            [5, 2, 3],
            [3, 0, 0],
            [7, 0, 0]
        ]
        queries = [3, 7]

        # when
        root = build_tree(3, nodes_data)
        results = process_queries(root, queries)

        # then
        self.assertEqual(results, [2, 1])


    @time_memory
    def test_case_2(self):
        # give
        nodes_data = [
            [10, 2, 3],
            [5, 4, 5],
            [15, 6, 7],
            [3, 0, 0],
            [7, 0, 0],
            [12, 0, 0],
            [17, 0, 0]
        ]
        queries = [5, 15, 3, 17]

        # when
        root = build_tree(7, nodes_data)
        results = process_queries(root, queries)

        # then
        self.assertEqual(results, [4, 1, 1, 1])


    @time_memory
    def test_case_3(self):
        # give
        nodes_data = [
            [8, 2, 3],
            [4, 4, 5],
            [12, 6, 7],
            [2, 0, 0],
            [6, 0, 0],
            [10, 0, 0],
            [14, 0, 0]
        ]
        queries = [1, 4, 13, 12, 8]

        # when
        root = build_tree(7, nodes_data)
        results = process_queries(root, queries)

        # then
        self.assertEqual(results, [7, 4, 4, 1, 0])


if __name__ == '__main__':
    unittest.main()
