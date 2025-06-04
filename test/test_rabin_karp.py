import unittest
import os
from rabin_karp import rabin_karp_search_from_file

class TestRabinKarpFromFile(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_text.txt'
        self.text = "абракадабра\nбраслет\nнебраконьєр"
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write(self.text)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_found_positions(self):
        expected = [1, 8, 12, 22]
        result = rabin_karp_search_from_file(self.test_file, "бра")
        self.assertEqual(result, expected)


    def test_not_found(self):
        result = rabin_karp_search_from_file(self.test_file, "жаба")
        self.assertEqual(result, [])

    def test_file_not_found(self):
        result = rabin_karp_search_from_file("no_such_file.txt", "бра")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
