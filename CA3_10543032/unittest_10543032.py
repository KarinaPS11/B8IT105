"""
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 3        10% - 10 Functional Calculator with Map Reduce Filter & Generator
"""



from calculator_10543032 import *
import unittest

test_items = np.arange(1, 5)
test_items2 = np.arange(1, 9, 2)

class TestCalculator(unittest.TestCase):
       

    def test_add_all_values(self):
        self.assertTrue(10, Calculator().add_all_values(test_items))
        
    def test_subtract_all_values(self):
        self.assertTrue(-8, Calculator().subtract_all_values(test_items))

    def test_multiply_all_values_all_values(self):
        self.assertTrue(24, Calculator().multiply_all_values(test_items))

    def test_divide_all_values(self):
        self.assertTrue(0.041666666666666664, Calculator().divide_all_values(test_items))

    def test_maximum(self):
        self.assertTrue(4, Calculator().maximum(test_items))

    def test_minimum(self):
        self.assertTrue(1, Calculator().minimum(test_items))

    def test_add_lists(self):
        self.assertTrue([2, 5, 8, 11], Calculator().add_lists(test_items, test_items2))

    def test_minus_lists(self):
        self.assertTrue([0, -1, -2, -3], Calculator().minus_lists(test_items, test_items2))

    def test_multiply_lists(self):
        self.assertTrue([1, 6, 15, 28], Calculator().multiply_lists(test_items, test_items2))

    def test_divide_lists(self):
        self.assertTrue([1.0, 0.6666666666666666, 0.6, 0.5714285714285714], Calculator().divide_lists(test_items, test_items2))
        
    def test_is_even(self):
        self.assertTrue([2, 4], Calculator().is_even(test_items))

    def test_is_odd(self):
        self.assertTrue([1, 3], Calculator().is_odd(test_items))
        
    def test_greater_than_mean(self):
        self.assertTrue([3, 4], Calculator().greater_than_mean(test_items))
        
    def test_toKM(self):
        self.assertTrue([1.6, 3.2, 4.8, 6.4], Calculator().toKM(test_items))

    def test_toMiles(self):
        self.assertTrue([0.625, 1.25, 1.875, 2.5], Calculator().toMiles(test_items))

if __name__ == '__main__':
    unittest.main()       


