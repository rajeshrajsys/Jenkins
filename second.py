import unittest
from main import reverse_string

class TestStringReverse(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("123"), "321")

if __name__ == '__main__':
    unittest.main()
