import unittest
from lab_5_lvl_2 import find_root

class TestGraph(unittest.TestCase):
    def test_example_graph(self):
        graph = {
            0: [1],
            1: [2],
            2: [3],
            3: [0],
            4: [3, 5],
            5: [0]
        }
        n = 6
        self.assertEqual(find_root(graph, n), 4)

    def test_no_root(self):
        graph = {
            0: [1],
            1: [2],
            2: [],
            3: []
        }
        n = 4
        self.assertEqual(find_root(graph, n), -1)

    def test_multiple_roots(self):
        graph = {
            0: [1],
            1: [2],
            2: [0],
            3: [0, 1, 2]
        }
        n = 4
        self.assertEqual(find_root(graph, n), 3)

    def test_every_node_connected(self):
        graph = {
            0: [1, 2],
            1: [2, 0],
            2: [0, 1]
        }
        n = 3
        self.assertIn(find_root(graph, n), [0, 1, 2])  # будь-яка з них може бути

if __name__ == '__main__':
    unittest.main()
