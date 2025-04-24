import unittest
from govern import process_dependencies

class TestGovSort(unittest.TestCase):
    def test_example1(self):
        lines = [
            "visa foreignpassport\n",
            "visa hotel\n",
            "visa bankstatement\n",
            "bankstatement nationalpassport\n",
            "hotel creditcard\n",
            "creditcard nationalpassport\n",
            "nationalpassport birthcertificate\n",
            "foreignpassport nationalpassport\n",
            "foreignpassport militarycertificate\n",
            "militarycertificate nationalpassport\n"
        ]
        result = process_dependencies(lines)
        expected = [
            "birthcertificate",
            "nationalpassport",
            "militarycertificate",
            "foreignpassport",
            "creditcard",
            "hotel",
            "bankstatement",
            "visa"
        ]
        self.assertEqual(result, expected)

    def test_example2(self):
        lines = ["visa foreignpassport\n"]
        result = process_dependencies(lines)
        expected = ["foreignpassport", "visa"]
        self.assertEqual(result, expected)

    def test_multiple_independent(self):
        lines = [
            "b a\n",
            "d c\n"
        ]
        result = process_dependencies(lines)
        self.assertTrue(result.index("a") < result.index("b"))
        self.assertTrue(result.index("c") < result.index("d"))

if __name__ == "__main__":
    unittest.main()