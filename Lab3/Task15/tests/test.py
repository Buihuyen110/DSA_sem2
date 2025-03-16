import unittest
from Lab3.utils import time_memory
from Lab3.Task15.src.main import bfs

class TestBFS(unittest.TestCase):

    @time_memory
    def test_case_1(self):
        # give
        n = 5
        m = 5
        garden = [
            "11111",
            "10001",
            "10001",
            "10001",
            "11111"
        ]
        qx, qy, L = 4, 4, 10
        musketeers = [(2, 2, 1), (2, 3, 2), (3, 2, 3), (3, 3, 4)]
        expected_result = 10

        # When
        qx, qy = qx - 1, qy - 1
        musketeers = [(x - 1, y - 1, p) for x, y, p in musketeers]
        total_pendants = 0
        for Ax, Ay, Pa in musketeers:
            min_time = bfs(Ax, Ay, qx, qy, garden, n, m)  # Приводим к 0-индексации
            if min_time <= L:
                total_pendants += Pa

        # Then
        self.assertEqual(total_pendants, expected_result)

    @time_memory
    def test_case_2(self):
        # give
        n = 5
        m = 5
        garden = [
            "11111",
            "10001",
            "10111",
            "10101",
            "11111"
        ]
        qx, qy, L = 4, 4, 10
        musketeers = [(2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4)]
        expected_result = 0

        # When
        qx, qy = qx - 1, qy - 1
        musketeers = [(x - 1, y - 1, p) for x, y, p in musketeers]
        total_pendants = 0
        for Ax, Ay, Pa in musketeers:
            min_time = bfs(Ax, Ay, qx, qy, garden, n, m)  # Приводим к 0-индексации
            if min_time <= L:
                total_pendants += Pa

        # then
        self.assertEqual(total_pendants, expected_result)

    @time_memory
    def test_case_3(self):
        # give
        n = 5
        m = 5
        garden = [
            "11111",
            "10001",
            "10101",
            "10001",
            "11111"
        ]
        qx, qy, L = 4, 4, 3
        musketeers = [(2, 2, 1), (2, 3, 2), (3, 2, 3), (3, 3, 4)]
        expected_result = 9

        # When
        qx, qy = qx - 1, qy - 1
        musketeers = [(x - 1, y - 1, p) for x, y, p in musketeers]
        total_pendants = 0
        for Ax, Ay, Pa in musketeers:
            min_time = bfs(Ax, Ay, qx, qy, garden, n, m)  # Приводим к 0-индексации
            if min_time <= L:
                total_pendants += Pa

        # then
        self.assertEqual(total_pendants, expected_result)


if __name__ == "__main__":
    unittest.main()