import unittest
from main import is_valid_triangle

class TriangleTest(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(is_valid_triangle(3, 4, 5))
        self.assertTrue(is_valid_triangle(5, 12, 13))
        self.assertTrue(is_valid_triangle(8, 15, 17))
        self.assertTrue(is_valid_triangle(7, 10, 12))

    def test_invalid_triangle(self):
        self.assertFalse(is_valid_triangle(0, 4, 5))
        self.assertFalse(is_valid_triangle(3, 4, -5))
        self.assertFalse(is_valid_triangle(2, 2, 4))
        self.assertFalse(is_valid_triangle(5, 10, 20))


if __name__ == '__main__':
    unittest.main()



