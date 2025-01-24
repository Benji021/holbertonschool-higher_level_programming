#!/usr/bin/python3


import unittest

from your_module_name import max_integer  # Replace 'your_module_name' with the actual name of your module

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_identical_elements(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 5000000, 10000000]), 10000000)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

if __name__ == '__main__':
    unittest.main()
