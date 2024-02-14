#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import main

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
        self.assertEqual(main.add(-1, 1), 0)
        self.assertEqual(main.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(main.subtract(5, 3), 2)
        self.assertEqual(main.subtract(10, 7), 3)
        self.assertEqual(main.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)
        self.assertEqual(main.multiply(-1, 1), -1)
        self.assertEqual(main.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(main.divide(6, 3), 2)
        self.assertEqual(main.divide(10, 5), 2)
        self.assertEqual(main.divide(5, 2), 2.5)
        self.assertEqual(main.divide(10, 0), "Error: Cannot divide by zero")

    def test_power(self):
        self.assertEqual(main.power(2, 3), 8)
        self.assertEqual(main.power(3, 2), 9)
        self.assertEqual(main.power(0, 5), 0)

    def test_square_root(self):
        self.assertEqual(main.square_root(4), 2)
        self.assertEqual(main.square_root(9), 3)
        self.assertEqual(main.square_root(16), 4)

    def test_modulus(self):
        self.assertEqual(main.modulus(5, 2), 1)
        self.assertEqual(main.modulus(10, 3), 1)
        self.assertEqual(main.modulus(4, 2), 0)

if __name__ == '__main__':
    unittest.main()

