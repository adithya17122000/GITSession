# test_main.py
import unittest
from main import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_addition(self):
        a = 1
        b = 2
        expected_result = 3
        self.assertEqual(add_numbers(a, b), expected_result, "Should be 3")

if __name__ == "__main__":
    unittest.main()
