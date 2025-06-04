import unittest
from src.cable_planner import minimum_cable_length


class TestCablePlanner(unittest.TestCase):
    def test_small_graph(self):
        matrix = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0],
        ]
        self.assertEqual(minimum_cable_length(matrix), 16)

    def test_two_nodes(self):
        matrix = [
            [0, 1],
            [1, 0],
        ]
        self.assertEqual(minimum_cable_length(matrix), 1)

    def test_single_node(self):
        matrix = [[0]]
        self.assertEqual(minimum_cable_length(matrix), 0)


if __name__ == "__main__":
    unittest.main()
